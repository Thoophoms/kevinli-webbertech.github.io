# Jenkins Integration in Kubernetes

This document compiles the integration of Jenkins into K8s. After the installation we can briefly see what Jenkins is and hopefully we can automate the build process with Github later.

## K8s Integration with Jenkins

A Kubernetes cluster adds a new automation layer to Jenkins. Kubernetes makes sure that resources are used effectively and that your servers and underlying infrastructure are not overloaded. Kubernetes' ability to orchestrate container deployment ensures that Jenkins always has the right amount of resources available.

Hosting Jenkins on a Kubernetes Cluster is beneficial for Kubernetes-based deployments and dynamic container-based scalable Jenkins agents. Here, we see a step-by-step process for setting up Jenkins on a Kubernetes Cluster.

**Setup Jenkins On Kubernetes**

For setting up a Jenkins Cluster on Kubernetes, we will do the following:

* Create a Namespace

`kubectl create namespace devops-tools`

* Create a service account with Kubernetes admin permissions. (serviceAccount.yaml)

```yaml
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: jenkins-admin
rules:
  - apiGroups: [""]
    resources: ["*"]
    verbs: ["*"]
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: jenkins-admin
  namespace: devops-tools
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: jenkins-admin
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: jenkins-admin
subjects:
- kind: ServiceAccount
  name: jenkins-admin
  namespace: devops-tools
```

The `serviceAccount.yaml` creates a `jenkins-admin` clusterRole, `jenkins-admin` ServiceAccount and binds the `clusterRole` to the service account.

The 'jenkins-admin' cluster role has all the permissions to manage the cluster components. You can also restrict access by specifying individual resource actions.

Now create the service account using kubectl.

`kubectl apply -f serviceAccount.yaml`

* Create local persistent volume for persistent Jenkins data on Pod restarts.

Create `volume.yaml` and copy the following persistent volume manifest.

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: local-storage
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: jenkins-pv-volume
  labels:
    type: local
spec:
  storageClassName: local-storage
  claimRef:
    name: jenkins-pv-claim
    namespace: devops-tools
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  local:
    path: /mnt
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - worker-node01
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: jenkins-pv-claim
  namespace: devops-tools
spec:
  storageClassName: local-storage
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 3Gi
```

Important Note: Replace 'worker-node01' with any one of your cluster worker nodes hostname.

You can get the worker node hostname using the kubectl.

`kubectl get nodes`

For volume, we are using the 'local' storage class for the purpose of demonstration. Meaning, it creates a 'PersistentVolume' volume in a specific node under the '/mnt' location.

As the 'local' storage class requires the node selector, you need to specify the worker node name correctly for the Jenkins pod to get scheduled in the specific node.

If the pod gets deleted or restarted, the data will get persisted in the node volume. However, if the node gets deleted, you will lose all the data. Ideally, you should use a persistent volume using the available storage class with the cloud provider, or the one provided by the cluster administrator to persist data on node failures.

`kubectl create -f volume.yaml`

* Create a deployment YAML and deploy it. (deployment.yaml)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jenkins
  namespace: devops-tools
spec:
  replicas: 1
  selector:
    matchLabels:
      app: jenkins-server
  template:
    metadata:
      labels:
        app: jenkins-server
    spec:
      securityContext:
            fsGroup: 1000
            runAsUser: 1000
      serviceAccountName: jenkins-admin
      containers:
        - name: jenkins
          image: jenkins/jenkins:lts
          resources:
            limits:
              memory: "2Gi"
              cpu: "1000m"
            requests:
              memory: "500Mi"
              cpu: "500m"
          ports:
            - name: httpport
              containerPort: 8080
            - name: jnlpport
              containerPort: 50000
          livenessProbe:
            httpGet:
              path: "/login"
              port: 8080
            initialDelaySeconds: 90
            periodSeconds: 10
            timeoutSeconds: 5
            failureThreshold: 5
          readinessProbe:
            httpGet:
              path: "/login"
              port: 8080
            initialDelaySeconds: 60
            periodSeconds: 10
            timeoutSeconds: 5
            failureThreshold: 3
          volumeMounts:
            - name: jenkins-data
              mountPath: /var/jenkins_home
      volumes:
        - name: jenkins-data
          persistentVolumeClaim:
              claimName: jenkins-pv-claim
```

In this Jenkins Kubernetes deployment we have used the following:

'securityContext' for Jenkins pod to be able to write to the local persistent volume.

Liveness and readiness probe to monitor the health of the Jenkins pod.

Local persistent volume based on local storage class that holds the Jenkins data path '/var/jenkins_home'.

The deployment file uses local storage class persistent volume for Jenkins data. For production use cases, you should add a cloud-specific storage class persistent volume for your Jenkins data.
If you don’t want the local storage persistent volume, you can replace the volume definition in the deployment with the host directory as shown below.

```shell
volumes:
- name: jenkins-data
  emptyDir: \{}
```

Create the deployment using kubectl.

`kubectl apply -f deployment.yaml`

Check the deployment status.

`kubectl get deployments -n devops-tools`

Now, you can get the deployment details using the following command.

`kubectl describe deployments --namespace=devops-tools`

* Create a service YAML and deploy it. (service.yaml)

We have now created a deployment. However, it is not accessible to the outside world. For accessing the Jenkins deployment from the outside world, we need to create a service and map it to the deployment. To access Jenkins Using Kubernetes Service,

```yaml
apiVersion: v1
kind: Service
metadata:
  name: jenkins-service
  namespace: devops-tools
  annotations:
      prometheus.io/scrape: 'true'
      prometheus.io/path:   /
      prometheus.io/port:   '8080'
spec:
  selector:
    app: jenkins-server
  type: NodePort
  ports:
    - port: 8080
      targetPort: 8080
      nodePort: 32000
```

Here, we are using the type as 'NodePort' which will expose Jenkins on all kubernetes node IPs on port 32000. If you have an ingress setup, you can create an ingress rule to access Jenkins. Also, you can expose the Jenkins service as a Loadbalancer if you are running the cluster on AWS, Google, or Azure cloud.

Create the Jenkins service using kubectl.

`kubectl apply -f service.yaml`

Now, when browsing to any one of the Node IPs on port 32000, you will be able to access the Jenkins dashboard.

`http://<node-ip>:32000`

Jenkins will ask for the initial Admin password when you access the dashboard for the first time.

You can get that from the pod logs either from the Kubernetes dashboard or CLI. You can get the pod details using the following CLI command.

`kubectl get pods --namespace=devops-tools`

With the pod name, you can get the logs as shown below. Replace the pod name with your pod name.

`kubectl logs jenkins-deployment-2539456353-j00w5 --namespace=devops-tools`

The password can be found at the end of the log.

Alternatively, you can run the exec command to get the password directly from the location as shown below.

`kubectl exec -it jenkins-559d8cd85c-cfcgk cat /var/jenkins_home/secrets/initialAdminPassword -n devops-tools`

* https://www.jenkins.io/doc/book/installing/kubernetes/
* https://plugins.jenkins.io/kubernetes/

## K8s

## K8s Tools

Rancher desktop [a good dashboard client]

### Ref

- https://www.youtube.com/watch?v=ZXaorni-icg&t=1113s
- https://stackoverflow.com/questions/73799893/jenkins-pipeline-how-to-use-multiple-docker-containers-each-one-being-specified
# K8s Configuration

# Updating Configuration via a ConfigMap

This tutorial demonstrates updating Pod configurations using ConfigMaps in Kubernetes.

## Prerequisites

- `kubectl`
- `curl` (optional, for HTTP requests)

## Objectives

- Update configuration via a ConfigMap mounted as a Volume.
- Update environment variables of a Pod via a ConfigMap.
- Update configuration via a ConfigMap in a multi-container Pod.
- Update configuration via a ConfigMap in a Pod possessing a Sidecar Container.
- Update configuration via an immutable ConfigMap that is mounted as a volume.

## Update configuration via a ConfigMap mounted as a Volume

1.  **Create ConfigMap:**

    - Creates a ConfigMap named `sport` with a key-value pair.

    ```shell
    kubectl create configmap sport --from-literal=sport=football
    ```

    Example of a deployment yaml with the ConfigMap sport as a volume
    
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: configmap-volume
  labels:
    app.kubernetes.io/name: configmap-volume
spec:
  replicas: 3
  selector:
    matchLabels:
  template:
    metadata:
      labels:
        app.kubernetes.io/name: configmap-volume
    spec:
      containers:
        - name: alpine
          image: alpine:3
          command:
            - /bin/sh
            - -c
            - while true; do echo "$(date) My preferred sport is $(cat /etc/config/sport)";
              sleep 10; done;
          ports:
            - containerPort: 80
          volumeMounts:
            - name: config-volume
              mountPath: /etc/config
      volumes:
        - name: config-volume
          configMap:
             name: sport
```

2.  **Apply Deployment:**

    - Deploys a Pod that mounts the ConfigMap as a volume.

    ```shell
    kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-as-volume.yaml
    ```

3.  **Check Pods:**

    - Verifies the Pods are running.

    ```shell
    kubectl get pods --selector=app.kubernetes.io/name=configmap-volume
    ```

4.  **View Logs:**

    - Displays the Pod's output, showing the ConfigMap data.

    ```shell
    kubectl logs deployments/configmap-volume
    ```

5.  **Edit ConfigMap:**

    - Modifies the ConfigMap's value.

    ```shell
    kubectl edit configmap sport
    ```

    - Change `sport` value to `cricket`.

    ```shell
      apiVersion: v1
      data:
        sport: cricket
      kind: ConfigMap
      # You can leave the existing metadata as they are.
      # The values you'll see won't exactly match these.
      metadata:
        creationTimestamp: "2024-01-04T14:05:06Z"
        name: sport
        namespace: default
        resourceVersion: "1743935"
        uid: 024ee001-fe72-487e-872e-34d6464a8a23
    ```

6.  **Tail Logs:**
    - Monitors the Pod's logs for updates.
    ```shell
    kubectl logs deployments/configmap-volume --follow
    ```

7. Get configmap object

```shell
bash-3.2$ kubectl get configmap
NAME               DATA   AGE
kube-root-ca.crt   1      4d22h
sport              1      11m
```




## Update environment variables of a Pod via a ConfigMap

1.  **Create ConfigMap:**

    - Creates a ConfigMap named `fruits` with a key-value pair.

    ```shell
    kubectl create configmap fruits --from-literal=fruits=apples
    ```

    Example of a deployment yaml with an environment variable configured via the ConfigMap fruits.

    ```shell
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: configmap-env-var
      labels:
        app.kubernetes.io/name: configmap-env-var
    spec:
      replicas: 3
      selector:
        matchLabels:
          app.kubernetes.io/name: configmap-env-var
      template:
        metadata:
          labels:
            app.kubernetes.io/name: configmap-env-var
        spec:
          containers:
            - name: alpine
              image: alpine:3
              env:
                - name: FRUITS
                  valueFrom:
                    configMapKeyRef:
                      key: fruits
                      name: fruits
              command:
                - /bin/sh
                - -c
                - while true; do echo "$(date) The basket is full of $FRUITS";
                    sleep 10; done;
              ports:
                - containerPort: 80
    ```

2.  **Apply Deployment:**

    - Deploys a Pod that uses the ConfigMap to set an environment variable.

    ```shell
    kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-as-envvar.yaml
    ```

3.  **Check Pods:**

    - Verifies the Pods are running.

    ```shell
    kubectl get pods --selector=app.kubernetes.io/name=configmap-env-var
    ```

4.  **View Logs:**

    - Displays the Pod's output, showing the environment variable.

    ```shell
    kubectl logs deployment/configmap-env-var
    ```

5.  **Edit ConfigMap:**

    - Modifies the ConfigMap's value.

    ```shell
    kubectl edit configmap fruits
    ```

    - Change `fruits` value to `mangoes`.

    ```shell
    apiVersion: v1
    data:
      fruits: mangoes
    kind: ConfigMap
    # You can leave the existing metadata as they are.
    # The values you'll see won't exactly match these.
    metadata:
      creationTimestamp: "2024-01-04T16:04:19Z"
      name: fruits
      namespace: default
      resourceVersion: "1749472"
    ```

6.  **Tail Logs (Observe no change):**

    - Monitors the Pod's logs (no immediate change).

    ```shell
    kubectl logs deployments/configmap-env-var --follow
    ```

7.  **Trigger Rollout:**

    - Restarts the Pods to apply the ConfigMap change.

    ```shell
    kubectl rollout restart deployment configmap-env-var
    kubectl rollout status deployment configmap-env-var --watch=true
    ```

8.  **Check Deployment:**

    - Verifies the Deployment status.

    ```shell
    kubectl get deployment configmap-env-var
    ```

9.  **Check Pods:**

    - Verifies the new Pods are running.

    ```shell
    kubectl get pods --selector=app.kubernetes.io/name=configmap-env-var
    ```

10. **View Logs (After Rollout):**
    - Displays the Pod's output with the updated environment variable.
    ```shell
    kubectl logs deployment/configmap-env-var
    ```

## Update configuration via a ConfigMap in a multi-container Pod

1.  **Create ConfigMap:**

    - Creates a ConfigMap named `color` with a key-value pair.

    ```shell
    kubectl create configmap color --from-literal=color=red
    ```

2.  **Apply Deployment:**

    - Deploys a Pod with two containers sharing a volume, using the ConfigMap.

    ```shell
    kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-two-containers.yaml
    ```

    Below is an example manifest for a Deployment that manages a set of Pods, each with two containers. The two containers share an emptyDir volume that they use to communicate. The first container runs a web server (nginx). The mount path for the shared volume in the web server container is /usr/share/nginx/html. The second helper container is based on alpine, and for this container the emptyDir volume is mounted at /pod-data. The helper container writes a file in HTML that has its content based on a ConfigMap. The web server container serves the HTML via HTTP.

    ```shell
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: configmap-two-containers
      labels:
        app.kubernetes.io/name: configmap-two-containers
    spec:
      replicas: 3
      selector:
        matchLabels:
          app.kubernetes.io/name: configmap-two-containers
      template:
        metadata:
          labels:
            app.kubernetes.io/name: configmap-two-containers
        spec:
          volumes:
            - name: shared-data
              emptyDir: {}
            - name: config-volume
              configMap:
                name: color
          containers:
            - name: nginx
              image: nginx
              volumeMounts:
                - name: shared-data
                  mountPath: /usr/share/nginx/html
            - name: alpine
              image: alpine:3
              volumeMounts:
                - name: shared-data
                  mountPath: /pod-data
                - name: config-volume
                  mountPath: /etc/config
              command:
                - /bin/sh
                - -c
                - while true; do echo "$(date) My preferred color is $(cat /etc/config/color)" > /pod-data/index.html;
                  sleep 10; done;
    ```

3.  **Check Pods:**

    - Verifies the Pods are running.

    ```shell
    kubectl get pods --selector=app.kubernetes.io/name=configmap-two-containers
    ```

4.  **Expose Deployment:**

    - Creates a Service to access the Pod.

    ```shell
    kubectl expose deployment configmap-two-containers --name=configmap-service --port=8080 --target-port=80
    ```

5.  **Port Forward:**

    - Forwards a local port to the Service.

    ```shell
    kubectl port-forward service/configmap-service 8080:8080 &
    ```

6.  **Access Service:**

    - Requests the service to see the initial ConfigMap value.

    ```shell
    curl http://localhost:8080
    ```

    Output example:
    Fri May 5 18:08:22 UTC 2025 My preferred color is red

7.  **Edit ConfigMap:**

    - Modifies the ConfigMap's value.

    ```shell
    kubectl edit configmap color
    ```

    - Change `color` value to `blue`.

    ```shell
    apiVersion: v1
    data:
      color: blue
    kind: ConfigMap
    # You can leave the existing metadata as they are.
    # The values you'll see won't exactly match these.
    metadata:
      creationTimestamp: "2024-01-05T08:12:05Z"
      name: color
      namespace: configmap
      resourceVersion: "1801272"
      uid: 80d33e4a-cbb4-4bc9-ba8c-544c68e425d6
    ```

8.  **Loop Service URL:**
    - Continuously requests the service to observe the update.
    ```shell
    while true; do curl --connect-timeout 7.5 http://localhost:8080; sleep 10; done
    ```

## Update configuration via a ConfigMap in a Pod possessing a sidecar container

1.  **Create ConfigMap (If not already created):**

    - Creates or reuses the ConfigMap named `color`.

    ```shell
    kubectl create configmap color --from-literal=color=blue
    ```

    Below is an example manifest for a Deployment that manages a set of Pods, each with a main container and a sidecar container. The two containers share an `emptyDir` volume that they use to communicate. The main container runs a web server (NGINX). The mount path for the shared volume in the web server container is /usr/share/nginx/html. The second container is a Sidecar Container based on Alpine Linux which acts as a helper container. For this container the emptyDir volume is mounted at /pod-data. The Sidecar Container writes a file in HTML that has its content based on a ConfigMap. The web server container serves the HTML via HTTP.

    ```shell
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: configmap-sidecar-container
      labels:
        app.kubernetes.io/name: configmap-sidecar-container
    spec:
      replicas: 3
      selector:
        matchLabels:
          app.kubernetes.io/name: configmap-sidecar-container
      template:
        metadata:
          labels:
            app.kubernetes.io/name: configmap-sidecar-container
        spec:
          volumes:
            - name: shared-data
              emptyDir: {}
            - name: config-volume
              configMap:
                name: color
          containers:
            - name: nginx
              image: nginx
              volumeMounts:
                - name: shared-data
                  mountPath: /usr/share/nginx/html
          initContainers:
            - name: alpine
              image: alpine:3
              restartPolicy: Always
              volumeMounts:
                - name: shared-data
                  mountPath: /pod-data
                - name: config-volume
                  mountPath: /etc/config
              command:
                - /bin/sh
                - -c
                - while true; do echo "$(date) My preferred color is $(cat /etc/config/color)" > /pod-data/index.html;
                  sleep 10; done;
    ```

2.  **Apply Deployment:**

    - Deploys a Pod with a main and sidecar container, using the ConfigMap.

    ```shell
    kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-and-sidecar-container.yaml
    ```

3.  **Check Pods:**

    - Verifies the Pods are running.

    ```shell
    kubectl get pods --selector=app.kubernetes.io/name=configmap-sidecar-container
    ```

4.  **Expose Deployment:**

    - Creates a Service to access the Pod.

    ```shell
    kubectl expose deployment configmap-sidecar-container --name=configmap-sidecar-service --port=8081 --target-port=80
    ```

5.  **Port Forward:**

    - Forwards a local port to the Service.

    ```shell
    kubectl port-forward service/configmap-sidecar-service 8081:8081 &
    ```

6.  **Access Service:**

    - Requests the service to see the initial ConfigMap value.

    ```shell
    curl http://localhost:8081
    ```

7.  **Edit ConfigMap:**

    - Modifies the ConfigMap's value.

    ```shell
    kubectl edit configmap color
    ```

    - Change `color` value to `green`.

    ```shell
      apiVersion: v1
      data:
        color: green
      kind: ConfigMap
      # You can leave the existing metadata as they are.
      # The values you'll see won't exactly match these.
      metadata:
        creationTimestamp: "2024-02-17T12:20:30Z"
        name: color
        namespace: default
        resourceVersion: "1054"
        uid: e40bb34c-58df-4280-8bea-6ed16edccfaa
    ```

8.  **Loop Service URL:**
    - Continuously requests the service to observe the update.
    ```shell
    while true; do curl --connect-timeout 7.5 http://localhost:8081; sleep 10; done
    ```

## Update configuration via an immutable ConfigMap that is mounted as a volume

**Note:**
Immutable ConfigMaps are especially used for configuration that is constant and is not expected to change over time. Marking a ConfigMap as immutable allows a performance improvement where the kubelet does not watch for changes.

If you do need to make a change, you should plan to either:

- change the name of the ConfigMap, and switch to running Pods that reference the new name
- replace all the nodes in your cluster that have previously run a Pod that used the old value
- restart the kubelet on any node where the kubelet previously loaded the old ConfigMap

1.  **Create Immutable ConfigMap:**

    - Creates an immutable ConfigMap.

    ```shell
    apiVersion: v1
    data:
      company_name: "ACME, Inc." # existing fictional company name
    kind: ConfigMap
    immutable: true
    metadata:
      name: company-name-20150801
    ```

    ```shell
    kubectl apply -f https://k8s.io/examples/configmap/immutable-configmap.yaml
    ```

2.  **Apply Deployment:**

    - Deploys a Pod that mounts the immutable ConfigMap as a volume.

    ```shell
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: immutable-configmap-volume
      labels:
        app.kubernetes.io/name: immutable-configmap-volume
    spec:
      replicas: 3
      selector:
        matchLabels:
          app.kubernetes.io/name: immutable-configmap-volume
      template:
        metadata:
          labels:
            app.kubernetes.io/name: immutable-configmap-volume
        spec:
          containers:
            - name: alpine
              image: alpine:3
              command:
                - /bin/sh
                - -c
                - while true; do echo "$(date) The name of the company is $(cat /etc/config/company_name)";
                  sleep 10; done;
              ports:
                - containerPort: 80
              volumeMounts:
                - name: config-volume
                  mountPath: /etc/config
          volumes:
            - name: config-volume
              configMap:
                name: company-name-20150801
    ```

    ```shell
    kubectl apply -f https://k8s.io/examples/deployments/deployment-with-immutable-configmap-as-volume.yaml
    ```

3.  **Check Pods:**

    - Verifies the Pods are running.

    ```shell
    kubectl get pods --selector=app.kubernetes.io/name=immutable-configmap-volume
    ```

4.  **View Logs:**

    - Displays the Pod's output, showing the immutable ConfigMap data.

    ```shell
    kubectl logs deployments/immutable-configmap-volume
    ```

5.  **Create New Immutable ConfigMap:**

    - Creates a new immutable ConfigMap with different data.

    ```shell
    apiVersion: v1
    data:
      company_name: "Fiktivesunternehmen GmbH" # new fictional company name
    kind: ConfigMap
    immutable: true
    metadata:
      name: company-name-20240312
    ```

    ```shell
    kubectl apply -f https://k8s.io/examples/configmap/new-immutable-configmap.yaml
    ```

6.  **Check ConfigMaps:**

    - Lists all ConfigMaps, including the new one.

    ```shell
    kubectl get configmap
    ```

7.  **Edit Deployment:**

    - Modifies the Deployment to use the new ConfigMap.

    ```shell
    kubectl edit deployment immutable-configmap-volume
    ```

    - Update volume to use the new ConfigMap.

    ```shell
    volumes:
    - configMap:
        defaultMode: 420
        name: company-name-20240312 # Update this field
      name: config-volume
    ```

8.  **Monitor Pods:**

    - Monitors the Pods during the rollout.

    ```shell
    kubectl get pods --selector=app.kubernetes.io/name=immutable-configmap-volume
    ```

9.  **View Logs (New Pods):**

    - Displays the Pod's output with the updated data.

    ```shell
    kubectl logs deployment/immutable-configmap-volume
    ```

10. **Delete Old ConfigMap:**
    - Removes the old ConfigMap.
    ```shell
    kubectl delete configmap company-name-20150801
    ```

## Cleanup

```shell
kubectl delete deployment configmap-volume configmap-env-var configmap-two-containers configmap-sidecar-container immutable-configmap-volume
kubectl delete service configmap-service configmap-sidecar-service
kubectl delete configmap sport fruits color company-name-20240312
kubectl delete configmap company-name-20150801 # In case it was not handled during the task execution
```

## Ref

https://kubernetes.io/docs/tutorials/configuration/

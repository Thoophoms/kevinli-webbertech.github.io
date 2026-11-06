# Lab 3 Yaml file + Load Balancer

Goal: **Load balancer with yaml configuration file**


## Part I

To access a LoadBalancer deployment, use the “minikube tunnel” command. Here is an example deployment:

```
kubectl create deployment balanced --image=kicbase/echo-server:1.0
kubectl expose deployment balanced --type=LoadBalancer --port=8080
```

In another window, start the tunnel to create a routable IP for the ‘balanced’ deployment:

`minikube tunnel`

To find the routable IP, run this command and examine the EXTERNAL-IP column:

`kubectl get services balanced`

Your deployment is now available at `<EXTERNAL-IP>:8080`

## Part II Create load balancer with yaml 

* Create a load-balancer-example.yaml

service/load-balancer-example.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app.kubernetes.io/name: load-balancer-example
  name: hello-world
spec:
  replicas: 5
  selector:
    matchLabels:
      app.kubernetes.io/name: load-balancer-example
  template:
    metadata:
      labels:
        app.kubernetes.io/name: load-balancer-example
    spec:
      containers:
      - image: gcr.io/google-samples/hello-app:2.0
        name: hello-world
        ports:
        - containerPort: 8080
```

The ReplicaSet has five Pods each of which runs the Hello World application.

**Run minikube server**

![minikube_start](../../../../../images/dev_ops/k8s/minikube_start.png)

**Run the following to create deployment**

`kubectl apply -f https://k8s.io/examples/service/load-balancer-example.yaml`

or,

`kubectl apply -f load-balancer-example.yaml`

![create_deployment](../../../../../images/dev_ops/k8s/create_deployment.png)

**Display information about the Deployment**

`kubectl get deployments hello-world`

`kubectl describe deployments hello-world`

Output,

![deployments](../../../../../images/dev_ops/k8s/deployments.png)

A more detailed description of the `describe` sub command.

![deployment_description](../../../../../images/dev_ops/k8s/deployment_description.png)

**Display information about your ReplicaSet objects**

`kubectl get replicasets`

`kubectl describe replicasets`

Output of the above commands,

![ReplicaSet](../../../../../images/dev_ops/k8s/ReplicaSet.png)

**Create a Service object that exposes the deployment**

`kubectl expose deployment hello-world --type=LoadBalancer --name=my-service`

**Display information about the Service**

`kubectl get services my-service`

![k8s_service](../../../../../images/dev_ops/k8s/k8s_service.png)

**Display pods information**

`kubectl get pods --output=wide`

![k8s_pod](../../../../../images/dev_ops/k8s/k8s_pods.png)

**Test Web Application**

`curl http://<external-ip>:<port>`

where <external-ip> is the external IP address (LoadBalancer Ingress) of your Service, and <port> is the value of Port in your Service description. If you are using minikube, typing minikube service my-service will automatically open the Hello World application in a browser.

The response to a successful request is a hello message:

```shell
Hello, world!
Version: 2.0.0
Hostname: 0bd46b45f32f
```

![launch_app](../../../../../images/dev_ops/k8s/launch_app.png)

```shell
xiaofengli@xiaofenglx:~/code/k8s$ curl http://192.168.49.2:32365/
Hello, world!
Version: 2.0.0
Hostname: hello-world-6db66cfc65-gn9dd
```

To understand the IP better, let us take a look at these,

```shell
xiaofengli@xiaofenglx:~/code/k8s$ kubectl get pods --output=wide
NAME                           READY   STATUS    RESTARTS   AGE   IP           NODE       NOMINATED NODE   READINESS GATES
hello-world-6db66cfc65-2j4h6   1/1     Running   0          20m   10.244.0.4   minikube   <none>           <none>
hello-world-6db66cfc65-8nghl   1/1     Running   0          20m   10.244.0.7   minikube   <none>           <none>
hello-world-6db66cfc65-gn9dd   1/1     Running   0          20m   10.244.0.5   minikube   <none>           <none>
hello-world-6db66cfc65-n7m8v   1/1     Running   0          20m   10.244.0.6   minikube   <none>           <none>
hello-world-6db66cfc65-w8p5j   1/1     Running   0          20m   10.244.0.3   minikube   <none>           <none>
xiaofengli@xiaofenglx:~/code/k8s$ kubectl get services my-service
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
my-service   LoadBalancer   10.101.101.44   <pending>     8080:32365/TCP   7m55s
xiaofengli@xiaofenglx:~/code/k8s$  minikube service my-service
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | my-service |        8080 | http://192.168.49.2:32365 |
```

***Explanation***

* The `10.101.101.44` is the load balancer ip inside the pod.
* The `10.244.0.*` is the 5 instances|replicas ip inside of the pod.
* The internal port of the load balancer is 8080.
* The external port of the load balancer is 32365.
* The external IP of the loadbalancer is pending and undermined, and it was assigned to 192.168.49.2.
* So the mapping is 192.168.49.2:32365 maps to internal loadbalancer's 10.101.101.44:8080.

**Dashboard**

Launch from cmd,

![launch_dashboard](../../../../../images/dev_ops/k8s/dashboard_1.png)

On the left side panel, those show 'N', meaning they are not available to view,

![web_dashboard](../../../../../images/dev_ops/k8s/dashboard_2.png)

**Clean up**

`kubectl delete services my-service`

`kubectl delete deployment hello-world`

## Ref

- https://kubernetes.io/docs/tutorials/stateless-application/expose-external-ip-address/
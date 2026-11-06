# Lab 1 Deploy An App with Portforwarding

Goal: **Portforwarding**

## Create a sample deployment and expose it on port 8080:

```
kubectl create deployment hello-minikube --image=kicbase/echo-server:1.0
kubectl expose deployment hello-minikube --type=NodePort --port=8080
```

It may take a moment, but your deployment will soon show up when you run:

`kubectl get services hello-minikube`

The easiest way to access this service is to let minikube launch a web browser for you:

`minikube service hello-minikube`

>Note: At this point you would see a random port in the outside exposure.

## Use kubectl to forward the port

We forward to a fixed port so that we could control the port in the firewall and we could use this service with a predictable port.

`kubectl port-forward service/hello-minikube 7080:8080`

>Note: Your application is now available at http://localhost:7080/.
> Now the port is a fixed port since this ia service so we need a fixed port that we could open it in the firewall.

You should be able to see the request metadata in the application output. Try changing the path of the request and observe the changes. Similarly, you can do a POST request and observe the body show up in the output.
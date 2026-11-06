# Create a reusable Minikube profile (dev)

This lets you start/stop a consistent config anytime.

## Create + start profile
   
```commandline
minikube start -p dev \
  --cpus=4 \
  --memory=8192 \
  --disk-size=40g \
  --driver=docker \
  --container-runtime=containerd
```

## Use the profile

minikube profile dev

Stop + delete (if needed)

`minikube stop -p dev`

`minikube delete -p dev`

## 2. Sample App Deployment (Nginx demo)

In the following example, we use a yaml config file to describe a deployment, and on the other hand,
we also use the profile to specify the minikube profile config.

Drop this into a file like `nginx-demo.yaml`:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-demo
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx-demo
  template:
    metadata:
      labels:
        app: nginx-demo
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-demo
spec:
  type: NodePort
  selector:
    app: nginx-demo
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080
```


* Deploy it:

`kubectl apply -f nginx-demo.yaml`

* Check pods:

`kubectl get pods`

* Get service URL:

`minikube service nginx-demo --url -p dev`

### 3. Mini kubectl Cheat Sheet (Minikube-friendly)

* Pods / Deployments

`kubectl get pods`

`kubectl get deploy`

`kubectl describe pod <podname>`

* Logs

`kubectl logs <podname>`

`kubectl logs -f <podname>`

* Port-forward

`kubectl port-forward deployment/nginx-demo 8080:80`

* Apply / Delete

`kubectl apply -f file.yaml`

`kubectl delete -f file.yaml`

* Quick shell into a pod

`kubectl exec -it <podname> -- bash`

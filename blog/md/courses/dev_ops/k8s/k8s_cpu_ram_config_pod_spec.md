# CPU + Memory settings directly into the pod spec

Kubernetes does this with resources.requests and resources.limits.

Here’s the same Nginx YAML but with CPU/memory added:

```commandline
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
        resources:
          requests:
            cpu: "250m"      # the pod *asks* for 0.25 CPU
            memory: "256Mi" # and 256 MB RAM guaranteed
          limits:
            cpu: "500m"      # the pod can burst up to 0.5 CPU
            memory: "512Mi" # but max 512 MB RAM
```


Let us save the above file to `nginx-demo.yaml`. To run this file, let us type,

`kubectl -f nginx-demo.yaml`

Next, let us check with the following commands,

```buildoutcfg
kubectl get deployment

kubectl describe deployment nginx-demo

kubectl get pods
```

### Quick breakdown (human-friendly version):

* requests = “I need at least this much to run.”
Kubernetes uses this for scheduling.

* limits = “I’m not allowed to use more than this.”
CPU throttles; memory OOM-kills if exceeded.

### Common values developers use:

* Light web app:

requests: cpu 100m–300m, memory 128–256Mi
  
limits: cpu 300m–1, memory 256–512Mi

* Medium service:

requests: cpu 250m–500m, memory 256–512Mi

limits: cpu 1–2, memory 512Mi–1Gi

* Bigger workloads:

requests: cpu 1–2, memory 1–2Gi

limits: cpu 2–4, memory 2–4Gi
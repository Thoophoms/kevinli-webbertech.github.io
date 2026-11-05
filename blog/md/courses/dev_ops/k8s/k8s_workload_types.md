# K8s Workload Types: Stateless, Stateful, and ReplicaSets

Kubernetes offers several controllers for running Pods. They all keep a set of Pods running, but differ in identity, storage, and ordering guarantees. This page explains the common ones and shows complete, runnable examples using small "dummy" images (`nginx`, `busybox`) so you can try each pattern on Minikube.

## Overview

| Workload | Identity per Pod | Storage | Typical use |
| --- | --- | --- | --- |
| ReplicaSet | None (interchangeable) | Ephemeral | Low-level mechanism behind Deployments; rarely created directly |
| Deployment | None (interchangeable) | Ephemeral | Stateless apps: web servers, APIs, workers |
| StatefulSet | Stable, ordered (`web-0`, `web-1`, ...) | Stable, per-Pod (via `volumeClaimTemplates`) | Stateful apps: databases, queues, anything needing stable network identity or storage |
| DaemonSet | None, one per node | Ephemeral or host-mounted | Node-level agents: log shippers, monitoring, CNI/CSI plugins |
| Job / CronJob | None | Ephemeral | Run-to-completion or scheduled batch tasks |

## Stateless vs. stateful, in practice

- **Stateless** means any replica can handle any request and can be destroyed/recreated at any time without special handling. There is no need for a stable name, a stable IP, or a specific disk. A `Deployment` is the right tool: Pods are fungible and are managed through `ReplicaSet`s that Kubernetes creates and updates for you.
- **Stateful** means each replica has an identity that matters: it needs the same name, the same persistent volume, and sometimes the same startup order every time it restarts (for example, a database node rejoining a cluster). A `StatefulSet` is the right tool: each Pod gets a stable name (`<name>-0`, `<name>-1`, ...), a stable DNS entry, and its own `PersistentVolumeClaim` created from a template.

## ReplicaSet

A ReplicaSet's job is to keep a specified number of Pod replicas running at all times, using a label selector to know which Pods belong to it. In normal use you do not create ReplicaSets directly — a Deployment creates and manages one for you so that it can also handle rolling updates and rollbacks. The direct example below is for learning purposes only.

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-rs
  labels:
    app: nginx-rs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx-rs
  template:
    metadata:
      labels:
        app: nginx-rs
    spec:
      containers:
      - name: nginx
        image: nginx:stable
        ports:
        - containerPort: 80
```

```shell
kubectl apply -f nginx-replicaset.yaml
kubectl get rs
kubectl get pods -l app=nginx-rs
kubectl delete -f nginx-replicaset.yaml
```

If you delete one of the Pods, the ReplicaSet controller creates a replacement immediately to satisfy `replicas: 3` — try it with `kubectl delete pod <one-of-the-pod-names>` and then `kubectl get pods -l app=nginx-rs` again.

## Deployment (stateless workloads)

A Deployment wraps a ReplicaSet and adds rolling updates, rollbacks, and revision history. This is the default choice for stateless workloads.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx-deploy
  template:
    metadata:
      labels:
        app: nginx-deploy
    spec:
      containers:
      - name: nginx
        image: nginx:stable
        ports:
        - containerPort: 80
```

```shell
kubectl apply -f nginx-deployment.yaml
kubectl get deployments
kubectl get rs
kubectl get pods -l app=nginx-deploy
```

Notice `kubectl get rs` shows a ReplicaSet named something like `nginx-deploy-7d8f9c6d9b` — this is the ReplicaSet the Deployment created and now manages for you. A rolling update (for example, changing `image: nginx:stable` to `image: nginx:1.27`) creates a new ReplicaSet and scales it up while scaling the old one down:

```shell
kubectl set image deployment/nginx-deploy nginx=nginx:1.27
kubectl rollout status deployment/nginx-deploy
kubectl rollout undo deployment/nginx-deploy
```

## StatefulSet (stateful workloads)

A StatefulSet requires a headless Service (`clusterIP: None`) to provide the network identity for each Pod, and a `volumeClaimTemplates` entry to give each Pod its own `PersistentVolumeClaim`. On Minikube, the default `standard` StorageClass satisfies these claims automatically.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-headless
  labels:
    app: web
spec:
  clusterIP: None
  selector:
    app: web
  ports:
  - port: 80
    name: http
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: "web-headless"
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx:stable
        ports:
        - containerPort: 80
          name: http
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "standard"
      resources:
        requests:
          storage: 1Gi
```

```shell
kubectl apply -f web-statefulset.yaml
kubectl get statefulsets
kubectl get pods -l app=web -o wide
kubectl get pvc
```

Observe two things a Deployment does not give you:

- **Stable names**: Pods are created in order as `web-0`, `web-1`, `web-2`, and are deleted in reverse order when you scale down.
- **Stable storage**: each Pod keeps the same `PersistentVolumeClaim` (`www-web-0`, `www-web-1`, `www-web-2`) across restarts; deleting a Pod does not delete its volume.

```shell
kubectl delete pod web-0
kubectl get pods -l app=web -w
```

The replacement Pod comes back as `web-0` again, reattached to the same `www-web-0` claim.

## DaemonSet (one Pod per node)

A DaemonSet ensures that every (or a selected subset of) node runs a copy of a Pod — typical for log collectors, metrics agents, or networking plugins. Minikube usually has a single node, so this is mainly useful to understand the pattern.

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-agent
spec:
  selector:
    matchLabels:
      app: node-agent
  template:
    metadata:
      labels:
        app: node-agent
    spec:
      containers:
      - name: busybox
        image: busybox:stable
        command: ["sh", "-c", "while true; do echo alive; sleep 3600; done"]
```

```shell
kubectl apply -f node-agent-daemonset.yaml
kubectl get daemonsets
kubectl get pods -l app=node-agent -o wide
```

## Job and CronJob (run-to-completion)

A `Job` runs a Pod to completion instead of keeping it running forever; a `CronJob` runs a `Job` on a schedule. Neither is "stateless" or "stateful" in the same sense as the workloads above — they are for one-off or scheduled work.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: hello-job
spec:
  template:
    spec:
      containers:
      - name: hello
        image: busybox:stable
        command: ["sh", "-c", "echo hello from a one-shot job"]
      restartPolicy: Never
  backoffLimit: 2
```

```shell
kubectl apply -f hello-job.yaml
kubectl get jobs
kubectl logs job/hello-job
```

## Choosing the right workload

- Does losing a Pod and getting a fresh, differently-named replacement cause problems? If no, use a **Deployment**. If yes (because something depends on a stable name, address, or disk), use a **StatefulSet**.
- Do you need exactly one copy of a Pod on every node? Use a **DaemonSet**.
- Do you need to run something once, or on a schedule, and then stop? Use a **Job** or **CronJob**.
- Do you need the raw replica-count mechanism without rolling updates? Use a **ReplicaSet** directly — but in practice let a Deployment manage it for you.

## Clean up

```shell
kubectl delete -f nginx-replicaset.yaml --ignore-not-found
kubectl delete -f nginx-deployment.yaml --ignore-not-found
kubectl delete -f web-statefulset.yaml --ignore-not-found
kubectl delete -f node-agent-daemonset.yaml --ignore-not-found
kubectl delete -f hello-job.yaml --ignore-not-found
kubectl delete pvc -l app=web
```

Deleting a StatefulSet does **not** delete its `PersistentVolumeClaim`s by default, which is why they are removed with an explicit `kubectl delete pvc` above.

## Ref

- https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
- https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
- https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
- https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
- https://kubernetes.io/docs/concepts/workloads/controllers/job/
- https://kubernetes.io/docs/concepts/workloads/cron-jobs/

# K8s Manifest Types: A Summary of Resource Kinds

Every Kubernetes object is described by a YAML (or JSON) manifest that is sent to the API server. This page summarizes the most common manifest types (the `kind` field), what each one is for, and a minimal example of each. For generating and applying manifests, see [K8s YAML Manifests](k8s_yaml_manifests.md). For the workload controllers in more depth, see [K8s Workload Types](k8s_workload_types.md).

## Anatomy of a manifest

Almost every manifest has the same four top-level fields:

```yaml
apiVersion: apps/v1        # API group and version of the resource
kind: Deployment           # The type of object to create
metadata:                  # Identity: name, namespace, labels, annotations
  name: web
  namespace: dev
  labels:
    app: web
spec:                      # The desired state; the shape depends on the kind
  replicas: 2
  # ...
```

| Field | Purpose |
| --- | --- |
| `apiVersion` | API group/version that serves the kind, for example `v1`, `apps/v1`, `batch/v1`, `networking.k8s.io/v1`. |
| `kind` | The resource type. |
| `metadata` | `name` (required), `namespace`, `labels`, `annotations`. |
| `spec` | The desired state. Kubernetes controllers work to make the real state match it. |
| `status` | The observed state. Written by Kubernetes; never set it in your manifests. |

Some kinds do not follow the `spec` pattern. `ConfigMap` and `Secret` use `data`, and `Role`/`RoleBinding` use `rules`/`subjects`.

Find the right `apiVersion` and all fields for a kind in your cluster:

```shell
kubectl api-resources
kubectl explain deployment.spec
kubectl explain deployment.spec.template.spec.containers --recursive
```

## Summary table

| Kind | `apiVersion` | Namespaced | Purpose |
| --- | --- | --- | --- |
| Namespace | `v1` | No | Logical partition of a cluster |
| Pod | `v1` | Yes | Smallest deployable unit: one or more containers |
| ReplicaSet | `apps/v1` | Yes | Keeps N identical Pods running |
| Deployment | `apps/v1` | Yes | Stateless apps with rolling updates and rollbacks |
| StatefulSet | `apps/v1` | Yes | Stateful apps with stable identity and storage |
| DaemonSet | `apps/v1` | Yes | One Pod per node |
| Job | `batch/v1` | Yes | Run-to-completion task |
| CronJob | `batch/v1` | Yes | Scheduled Jobs |
| Service | `v1` | Yes | Stable virtual IP and DNS name in front of Pods |
| Ingress | `networking.k8s.io/v1` | Yes | HTTP/HTTPS routing into the cluster |
| ConfigMap | `v1` | Yes | Non-confidential configuration |
| Secret | `v1` | Yes | Sensitive configuration |
| PersistentVolume | `v1` | No | A piece of cluster storage |
| PersistentVolumeClaim | `v1` | Yes | A request for storage by a Pod |
| StorageClass | `storage.k8s.io/v1` | No | How storage is dynamically provisioned |
| ServiceAccount | `v1` | Yes | Identity for processes running in Pods |
| Role / RoleBinding | `rbac.authorization.k8s.io/v1` | Yes | Namespace-scoped permissions and who has them |
| ClusterRole / ClusterRoleBinding | `rbac.authorization.k8s.io/v1` | No | Cluster-wide permissions and who has them |
| NetworkPolicy | `networking.k8s.io/v1` | Yes | Allowed Pod-to-Pod and Pod-to-external traffic |
| HorizontalPodAutoscaler | `autoscaling/v2` | Yes | Scales replicas based on metrics |
| ResourceQuota | `v1` | Yes | Caps total resource use in a namespace |
| LimitRange | `v1` | Yes | Default and maximum resources per Pod/container |

## Namespace

A Namespace divides a cluster into virtual clusters. Names of namespaced resources only need to be unique inside their namespace, and quotas and RBAC can be applied per namespace. Namespaces are cluster-scoped and have no `spec` to set in the common case.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: dev
  labels:
    env: dev
```

Namespaced manifests either set `metadata.namespace: dev` or are applied with `kubectl apply -n dev -f file.yaml`. The namespace must exist first.

## Pod

A Pod runs one or more containers that share network and storage. You rarely create bare Pods in production because nothing restarts them if their node fails; use a Deployment or another controller instead. Bare Pods are useful for learning and debugging.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:stable
    ports:
    - containerPort: 80
    resources:
      requests:
        cpu: 100m
        memory: 64Mi
      limits:
        memory: 128Mi
```

## Deployment

A Deployment manages stateless Pods through ReplicaSets that it creates for you. It provides scaling, rolling updates, and rollbacks. `spec.selector` must match the labels in `spec.template.metadata.labels`.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  namespace: dev
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
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
```

## ReplicaSet

A ReplicaSet keeps a specified number of identical Pods running. It has the same `selector` and `template` fields as a Deployment, but no rollout logic. Normally a Deployment owns it, so you do not write ReplicaSets yourself.

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-rs
spec:
  replicas: 2
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
```

## StatefulSet

A StatefulSet gives each Pod a stable name (`db-0`, `db-1`, ...), ordered start and stop, and its own PersistentVolumeClaim from `volumeClaimTemplates`. `serviceName` refers to a headless Service (`clusterIP: None`) that provides the Pods' DNS names.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: db
spec:
  serviceName: db
  replicas: 2
  selector:
    matchLabels:
      app: db
  template:
    metadata:
      labels:
        app: db
    spec:
      containers:
      - name: db
        image: busybox:1.36
        command: ["sh", "-c", "sleep 3600"]
        volumeMounts:
        - name: data
          mountPath: /data
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 1Gi
```

## DaemonSet

A DaemonSet runs one Pod on every node (or on the nodes matching a selector), which suits log collectors, monitoring agents, and network plugins.

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
      - name: agent
        image: busybox:1.36
        command: ["sh", "-c", "while true; do date; sleep 60; done"]
```

## Job and CronJob

A Job runs Pods until a set number of them complete successfully. A CronJob creates Jobs on a cron schedule. Job Pods must use `restartPolicy: Never` or `OnFailure`.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: hello-job
spec:
  backoffLimit: 3
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: hello
        image: busybox:1.36
        command: ["sh", "-c", "echo hello from a job"]
---
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello-cron
spec:
  schedule: "*/5 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
          - name: hello
            image: busybox:1.36
            command: ["sh", "-c", "date; echo hello from cron"]
```

## Service

A Service gives a set of Pods a stable virtual IP and DNS name and load-balances across them. Pods are selected by label, so `spec.selector` must match the Pod labels.

| `spec.type` | Behavior |
| --- | --- |
| `ClusterIP` (default) | Reachable only inside the cluster |
| `NodePort` | Also exposed on a port (30000-32767 by default) on every node |
| `LoadBalancer` | Also provisions an external load balancer (on Minikube, use `minikube tunnel`) |
| `ExternalName` | DNS CNAME alias to an external name; no proxying |

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web
  namespace: dev
spec:
  type: ClusterIP
  selector:
    app: web
  ports:
  - name: http
    port: 80          # Port the Service listens on
    targetPort: 80    # Port on the Pod
```

## Ingress

An Ingress defines HTTP/HTTPS routing rules from outside the cluster to Services. It only takes effect when an ingress controller is running (on Minikube: `minikube addons enable ingress`).

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web
  namespace: dev
spec:
  ingressClassName: nginx
  rules:
  - host: web.example.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web
            port:
              number: 80
```

## ConfigMap

A ConfigMap stores non-confidential configuration as key/value pairs. Pods consume it as environment variables, command-line arguments, or files in a mounted volume. Do not store passwords or tokens in it.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  LOG_LEVEL: info
  app.properties: |
    mode=dev
    feature.x=true
```

Consuming it in a Pod spec:

```yaml
    env:
    - name: LOG_LEVEL
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: LOG_LEVEL
```

See [K8s ConfigMap](k8s_configmap.md) for complete examples.

## Secret

A Secret holds sensitive data such as passwords, tokens, and keys. Values under `data` are base64-encoded, which is encoding and not encryption. Use `stringData` to write plain text and let Kubernetes encode it. Restrict access with RBAC and consider enabling encryption at rest. Do not commit real secrets to Git.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-credentials
type: Opaque
stringData:
  username: appuser
  password: change-me
```

## PersistentVolume, PersistentVolumeClaim, and StorageClass

- A **PersistentVolume (PV)** is a piece of storage in the cluster. It is cluster-scoped.
- A **PersistentVolumeClaim (PVC)** is a namespaced request for storage. Kubernetes binds it to a matching PV, or dynamically provisions one through a StorageClass.
- A **StorageClass** describes a kind of storage and the provisioner that creates it. Minikube ships a default one named `standard`.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  # storageClassName: standard   # omit to use the cluster default
```

Using the claim in a Pod spec:

```yaml
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: data-pvc
  containers:
  - name: app
    image: busybox:1.36
    volumeMounts:
    - name: data
      mountPath: /data
```

Inspect storage with the commands in [K8s Storage Inspection](k8s_storage.md).

## ServiceAccount and RBAC

A ServiceAccount is the identity Pods use when calling the API server. Role-based access control (RBAC) then grants it permissions:

- `Role` and `RoleBinding` are namespaced.
- `ClusterRole` and `ClusterRoleBinding` apply cluster-wide.
- A binding connects a role to one or more subjects (users, groups, or ServiceAccounts).

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: pod-reader
  namespace: dev
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: dev
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-reader
  namespace: dev
subjects:
- kind: ServiceAccount
  name: pod-reader
  namespace: dev
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

Verify the permissions:

```shell
kubectl auth can-i list pods -n dev --as=system:serviceaccount:dev:pod-reader
```

## NetworkPolicy

A NetworkPolicy restricts which Pods can talk to which. It is only enforced if the network plugin supports it; the default Minikube setup may not enforce it unless you start it with a CNI such as Calico (`--cni=calico`).

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-web-from-frontend
  namespace: dev
spec:
  podSelector:
    matchLabels:
      app: web
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
    ports:
    - protocol: TCP
      port: 80
```

## HorizontalPodAutoscaler

An HPA changes a workload's replica count based on observed metrics. CPU-based scaling needs the metrics-server add-on (`minikube addons enable metrics-server`) and CPU `requests` set on the target's containers.

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web
  namespace: dev
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web
  minReplicas: 2
  maxReplicas: 6
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

## ResourceQuota and LimitRange

Both are applied per namespace to control resource use.

- `ResourceQuota` caps the total resources and object counts in the namespace.
- `LimitRange` sets default and maximum requests and limits for individual containers.

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: dev-quota
  namespace: dev
spec:
  hard:
    pods: "20"
    requests.cpu: "4"
    requests.memory: 4Gi
---
apiVersion: v1
kind: LimitRange
metadata:
  name: dev-limits
  namespace: dev
spec:
  limits:
  - type: Container
    default:
      cpu: 500m
      memory: 256Mi
    defaultRequest:
      cpu: 100m
      memory: 64Mi
```

## Putting several kinds in one file

Separate multiple manifests in one file with `---`. A common layout is a Namespace, then a Deployment and the Service that exposes it:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: demo
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello
  namespace: demo
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hello
  template:
    metadata:
      labels:
        app: hello
    spec:
      containers:
      - name: nginx
        image: nginx:stable
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: hello
  namespace: demo
spec:
  selector:
    app: hello
  ports:
  - port: 80
    targetPort: 80
```

Apply, inspect, and remove it:

```shell
kubectl apply -f hello.yaml
kubectl get all -n demo
kubectl delete -f hello.yaml
```

Deleting a Namespace deletes everything inside it, so `kubectl delete -f hello.yaml` removes the Deployment and Service as well.

## Tips

- Prefer `kubectl apply -f` (declarative) over `kubectl create` so that the file stays the source of truth.
- Validate before applying with `kubectl apply --dry-run=server -f file.yaml`, and preview changes with `kubectl diff -f file.yaml`.
- Use labels consistently. Selectors in Services, Deployments, and NetworkPolicies all depend on them.
- Pin image tags or digests rather than using `latest`.
- Set resource `requests` and `limits` so scheduling and autoscaling behave predictably.
- Apply resources in dependency order, or put them in one file in that order: Namespace, then ConfigMap/Secret/PVC/ServiceAccount, then workloads, then Services/Ingress.

## Ref

- https://kubernetes.io/docs/concepts/overview/working-with-objects/
- https://kubernetes.io/docs/reference/kubernetes-api/
- https://kubernetes.io/docs/concepts/workloads/
- https://kubernetes.io/docs/concepts/services-networking/
- https://kubernetes.io/docs/concepts/configuration/
- https://kubernetes.io/docs/concepts/storage/
- https://kubernetes.io/docs/reference/access-authn-authz/rbac/

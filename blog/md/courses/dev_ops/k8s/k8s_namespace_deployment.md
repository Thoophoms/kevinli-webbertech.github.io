# K8s Namespace & Deployment

This page collects the basic `kubectl` commands for creating a namespace, configuring your current context to use it, and creating a Deployment scoped to that namespace. It is a focused companion to [K8s Basic](k8s_basic.md).

## Why namespaces

A namespace is a way to divide a single cluster into multiple virtual clusters. It lets you isolate labs, teams, or environments (`dev`, `staging`, `k8s-lab`, etc.) so that resource names do not collide and so that commands like `kubectl get pods` only show what you expect.

```shell
kubectl get namespaces
```

Kubernetes ships with a few namespaces already: `default`, `kube-system`, `kube-public`, and `kube-node-lease`.

## Create a namespace

```shell
kubectl create namespace k8s-lab
```

Verify it was created:

```shell
kubectl get namespaces
kubectl get ns k8s-lab -o yaml
```

A namespace can also be created from a manifest, which is handy when you want it tracked alongside other YAML files:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: k8s-lab
```

```shell
kubectl apply -f namespace.yaml
```

## Configuring and setting the namespace

There are two ways to target a namespace:

1. **Per-command**, using `-n`/`--namespace`. This only affects the single command:

   ```shell
   kubectl get pods -n k8s-lab
   ```

2. **Persistently for the current context**, so you do not need `-n` on every command:

   ```shell
   kubectl config set-context --current --namespace=k8s-lab
   ```

   Confirm the change:

   ```shell
   kubectl config view --minify | grep namespace:
   ```

   Switch back to `default` when you are done with the lab:

   ```shell
   kubectl config set-context --current --namespace=default
   ```

`kubectl config current-context` and `kubectl config get-contexts` show which cluster/user/namespace combination is active. Always check the current context before creating or deleting resources, especially if you work with more than one cluster.

## Create a Deployment under a specified namespace

Once a namespace exists, a Deployment can be created inside it either with an explicit flag or inside a manifest.

**Option 1: `-n` on `kubectl create`**

```shell
kubectl create deployment hello-node -n k8s-lab \
  --image=registry.k8s.io/e2e-test-images/agnhost:2.39 \
  -- /agnhost netexec --http-port=8080
```

**Option 2: Namespace set via manifest**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-node
  namespace: k8s-lab
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hello-node
  template:
    metadata:
      labels:
        app: hello-node
    spec:
      containers:
      - name: hello-node
        image: registry.k8s.io/e2e-test-images/agnhost:2.39
        args: ["netexec", "--http-port=8080"]
        ports:
        - containerPort: 8080
```

```shell
kubectl apply -f hello-node-deployment.yaml
```

**Option 3: Current context already set to the namespace**

If you already ran `kubectl config set-context --current --namespace=k8s-lab`, you can omit `-n` entirely:

```shell
kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39
```

## Verify resources in the namespace

```shell
kubectl get deployments -n k8s-lab
kubectl get pods -n k8s-lab
kubectl get all -n k8s-lab
```

Listing without `-n` only shows the `default` namespace (or whichever namespace is set on the current context), and `-A`/`--all-namespaces` shows every namespace at once:

```shell
kubectl get pods -A
```

## Clean up

Deleting a namespace deletes every resource inside it, so double-check the current context first.

```shell
kubectl delete namespace k8s-lab
```

## Ref

- https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
- https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
- https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-context/

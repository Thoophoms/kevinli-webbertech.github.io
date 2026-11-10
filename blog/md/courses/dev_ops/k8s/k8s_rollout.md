# K8s Update and Roll Back Your App

This page covers rolling updates, rollout history, and rollbacks for a Deployment. It assumes a running Minikube cluster as set up in [K8s Basic](k8s_basic.md), including the `hello-node` Deployment from that page and the optional `web` Deployment from [K8s YAML Manifests](k8s_yaml_manifests.md).

## Update and roll back your app

For the optional `web` Deployment created in [K8s YAML Manifests](k8s_yaml_manifests.md):

```shell
kubectl set image deployment/web nginx=nginx:alpine
kubectl rollout status deployment/web --timeout=120s
kubectl rollout history deployment/web
kubectl rollout undo deployment/web
kubectl rollout status deployment/web --timeout=120s
```

In `nginx=nginx:alpine`, the left side is the container name, not the Deployment name. This switches image variants for demonstration, not necessarily to a newer version. A rollback restores the previous Pod template and requires a retained earlier revision; it does not restore databases or external configuration. Use `--to-revision=<revision>` with `rollout undo` to select a revision shown by `rollout history`.

Other useful rollout commands:

```shell
kubectl rollout restart deployment/hello-node
kubectl rollout status deployment/hello-node --timeout=120s
kubectl rollout pause deployment/web
kubectl rollout resume deployment/web
```

`restart` replaces Pods through a rolling update; it does not restart the cluster. `pause` suspends rollout of Pod-template changes, not application traffic; resume before expecting updates or rollback. Keep your YAML in sync with any desired imperative changes.

## Ref

- https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/
- https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/

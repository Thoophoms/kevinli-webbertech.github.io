# K8s YAML Manifests

This page covers generating, reviewing, and applying Kubernetes resources from YAML manifests instead of purely imperative `kubectl create`/`kubectl expose` commands. It assumes a running Minikube cluster as set up in [K8s Basic](k8s_basic.md).

## Work with YAML manifests

This optional example creates a separate `web` Deployment. Generating YAML makes it easier to review and reuse configuration:

```shell
kubectl create deployment web --image=nginx:stable --replicas=2 --dry-run=client -o yaml > web-deployment.yaml
kubectl apply --dry-run=server -f web-deployment.yaml
kubectl diff -f web-deployment.yaml
kubectl apply -f web-deployment.yaml
kubectl rollout status deployment/web --timeout=120s
```

- `--dry-run=client` generates the manifest without creating a resource.
- `--dry-run=server` asks the API server to validate the request without persisting it; it requires cluster access and permissions.
- `diff` previews changes. Exit code 1 means differences were found, not that validation failed; codes greater than 1 indicate errors.
- `apply` creates or updates resources declaratively. You can also use `kubectl apply -f ./manifests/` for a directory of manifests.
- Shell redirection with `>` overwrites an existing local file. Review generated manifests before applying them.

`nginx:stable` is convenient for a lab but is a moving tag. Pin a tested version or image digest for reproducible deployments.

The `web` Deployment created here is reused by the scaling and rollout examples in [K8s Basic](k8s_basic.md).

## Ref

- https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/
- https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/
- https://kubernetes.io/docs/reference/kubectl/generated/kubectl_diff/

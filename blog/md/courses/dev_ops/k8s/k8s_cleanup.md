# K8s Clean Up

This page collects the teardown commands for the [K8s Basic](k8s_basic.md) tutorial and its optional examples.

## Clean up

Check `kubectl config current-context` and the namespace before deleting resources. The following commands remove the tutorial application:

- `kubectl delete service hello-node`

- `kubectl delete deployment hello-node`

If you ran the optional examples, remove their resources as well:

```shell
kubectl delete -f web-deployment.yaml
kubectl delete configmap app-config
kubectl delete namespace k8s-lab
```

- `web-deployment.yaml` is the manifest from [K8s YAML Manifests](k8s_yaml_manifests.md).
- `app-config` is the ConfigMap from [K8s ConfigMap](k8s_configmap.md).
- `k8s-lab` is the namespace from [K8s Namespace & Deployment](k8s_namespace_deployment.md).

Deleting a namespace deletes all namespaced resources inside it, not just this tutorial's examples. Only delete the lab namespace if it is disposable.

Stop the local cluster while preserving it for later:

```shell
minikube stop
```

Optionally, delete the default Minikube cluster and its local cluster data:

- `minikube delete`

If you created the separate named profile, use `minikube stop -p k8s-lab` or `minikube delete -p k8s-lab` instead. A Minikube profile and a Kubernetes namespace are different things.

## Troubleshooting and deep cleaning

Start with non-destructive diagnostics:

```shell
minikube status
minikube logs --problems
kubectl get pods -A
kubectl get events -A --sort-by=.metadata.creationTimestamp
kubectl auth can-i create deployments -n default
```

| Symptom | First checks |
| --- | --- |
| Cannot connect to the API server | Check Minikube status, current context, and kubeconfig. |
| Pod remains `Pending` | Use `describe pod` to check scheduling events, resource availability, and volume claims. |
| `ImagePullBackOff` | Check the image name/tag, registry credentials, and network access. |
| `CrashLoopBackOff` | Read current and `--previous` container logs; inspect command arguments and probes. |
| Service has no ready endpoints | Check selectors, Pod readiness, and EndpointSlices. |
| `Forbidden` | Use `kubectl auth can-i` to check permissions for the action and namespace. |

**Destructive last resort:** the following are independent cleanup options, not routine troubleshooting steps.

- `minikube delete --all --purge`

  Deletes all Minikube profiles and removes the local `.minikube` directory. This can destroy local cluster data for unrelated labs.

- `docker system prune`

  Removes unused Docker data, including stopped containers, unused networks, dangling images, and build cache. It affects Docker resources outside Minikube too; volumes are not removed by default. Review Docker's confirmation prompt and avoid adding `--volumes` unless you intend to delete unused volumes.

## Ref

- https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
- https://minikube.sigs.k8s.io/docs/commands/delete/

# K8s Storage Inspection

Quick commands for inspecting the storage resources backing a cluster: PersistentVolumeClaims, PersistentVolumes, and StorageClasses. For application configuration data, see [K8s ConfigMap](k8s_configmap.md) instead.

## Inspect storage resources

```shell
kubectl get pvc
kubectl get pv
kubectl get storageclass
```

PersistentVolumeClaims are namespaced; PersistentVolumes and StorageClasses are cluster-scoped. Deleting a claim can delete its backing storage depending on the reclaim policy.

## Ref

- https://kubernetes.io/docs/concepts/storage/persistent-volumes/
- https://kubernetes.io/docs/concepts/storage/storage-classes/

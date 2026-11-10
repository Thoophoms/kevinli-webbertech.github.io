# K8s Manage Add-ons

Minikube ships with optional add-ons you can enable and disable per cluster. This page assumes a running Minikube cluster as set up in [K8s Basic](k8s_basic.md).

## Manage Add-ons

- show addons

`minikube addons list`

Available add-ons and their default status vary by Minikube version and driver. Use the actual command output rather than assuming an add-on is installed.

- Enable an addon, for example, metrics-server:

  - `minikube addons enable metrics-server`

- View the Pod and Service you created by installing that addon:

  - `kubectl get pod,svc -n kube-system`

- Check the output from metrics-server:

  - `kubectl top pods`

  - `kubectl top pods --containers`

  - `kubectl top pods --sort-by=memory`

  - `kubectl top nodes`

Metrics may take a short time to appear after enabling the add-on. `top` requires a working Metrics Server and shows current usage, not historical monitoring.

- Disable metrics-server:

  - `minikube addons disable metrics-server`

## Ref

- https://minikube.sigs.k8s.io/docs/handbook/addons/
- https://minikube.sigs.k8s.io/docs/commands/addons/

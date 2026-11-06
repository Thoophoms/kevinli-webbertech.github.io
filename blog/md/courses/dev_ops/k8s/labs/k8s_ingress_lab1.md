
# K8s Ingress Lab1 Setup

## Install Prerequisites

Ensure you have kubectl, a Kubernetes cluster (Minikube for local testing, and curl for testing).

**Install kubectl (if not installed)**

![system update](/blog/images/dev_ops/k8s_ingress/System_Update.PNG)

![GPG Key](/blog/images/dev_ops/k8s_ingress/K8s_GPGKey.PNG)

![K8s APT Repository](/blog/images/dev_ops/k8s_ingress/K8s_APT_Repository.PNG)

![Kubectl install](/blog/images/dev_ops/k8s_ingress/kubectl_install.PNG)

**Install Minikube (for local testing)**

![Minikube install](/blog/images/dev_ops/k8s_ingress/minikube_install.PNG)

![Minikube install 2](/blog/images/dev_ops/k8s_ingress/minikube_install2.PNG)

## Part 1: Enable Ingress Controller

**For minikube (simplest option)**

* Let us run the cluster first

`minikube start --driver=docker`

![Starting Minikube](/blog/images/dev_ops/k8s_ingress/minikube_start.PNG)

**Why?**

- Real clusters (EKS,GKE) cost money. Minikube emulates a cluster on your laptop.
- --driver=docker uses Docker containers as "virtual nodes" (lightweight)

Type the following and run,

`minikube addons enable ingress`

![Enabling the Ingress Controller](/blog/images/dev_ops/k8s_ingress/enable_ingress_controller.PNG)

**Why?**

- Ingress isn't enabled by default (like how AWS/GKE require you to install Nginx).
- This deploys an **Nginx Ingress Controller** Pod in your cluster, which acts as the "traffic cop" for routing.

**Verify**

Type the following and run,

`kubectl get pods -n ingress-nginx`

![Verifying the process of enabling the ingress controller](/blog/images/dev_ops/k8s_ingress/verify_controller.PNG)

You should see ingress-nginx-controller-xxxx running.

# K8s Container Runtime

`containerd` is basically the engine under the hood that actually runs containers.

Think of it like this:

`Docker = a full kitchen (chef, menu, ordering system)`

`containerd = just the stove + oven doing the actual cooking`

Kubernetes doesn’t need the whole kitchen — it just needs something to start/stop containers. containerd is that “something.”

What containerd actually is a lightweight container runtime that handles:

* pulling images
* unpacking them
* creating containers
* starting/stopping containers
* managing container storage
* Designed to be simple, fast, and reliable
* Created by Docker but extracted as a standalone component

## Why Kubernetes likes containerd

K8s used to use Docker, but Docker had extra “stuff” Kubernetes didn’t need.

Now, containerd is the preferred runtime because it’s:

* Faster
* Less overhead
* More stable for clusters
* CRI-compliant (Container Runtime Interface)
* Lower memory usage
* Built-in to most K8s distros (EKS, GKE, AKS)

## How to use it In Minikube

When you do:

`minikube start --container-runtime=containerd`

You’re saying:

“Hey Minikube, use containerd as the backend for running containers instead of Docker.”
Under the hood, your Pods will be created by containerd instead of Docker.

## Quick recap (human version)

* containerd = minimal, efficient container runtime

* Docker = containerd + extra developer tooling

Kubernetes now defaults to containerd because it’s leaner and purpose-built.
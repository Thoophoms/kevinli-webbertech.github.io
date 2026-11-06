# Kubernetes Networking Tutorial

## Goal

This tutorial explains how networking works in Kubernetes from the moment a Pod starts to the point where traffic enters the cluster from outside.

By the end, you should understand:

- how Pods communicate with each other
- how Services provide stable access to changing Pods
- how DNS works inside the cluster
- when to use ClusterIP, NodePort, LoadBalancer, and Ingress
- how NetworkPolicy limits traffic between workloads
- how to troubleshoot common Kubernetes networking issues

## The Big Picture

Kubernetes networking is built around a simple model:

1. Every Pod gets its own IP address.
2. Pods can communicate with other Pods without NAT in a healthy cluster.
3. Services give clients a stable virtual IP and DNS name.
4. Ingress provides HTTP and HTTPS routing into the cluster.
5. NetworkPolicy controls which traffic is allowed.

Think of it like this:

- Pod IP = an apartment number that may change
- Service = the apartment building front desk with a stable contact point
- DNS = the address book
- Ingress = the main entrance and traffic director
- NetworkPolicy = the security guard

## Core Networking Objects

### Pod

A Pod is the smallest deployable unit in Kubernetes. Each Pod gets its own IP address. Containers inside the same Pod share the same network namespace, which means:

- they share the same IP address
- they can reach each other through `localhost`
- they can expose multiple ports on the same Pod IP

Example: if a Pod contains an app container and a sidecar container, both containers use the same Pod IP.

### Service

A Service gives a stable endpoint to a set of Pods selected by labels. Pods are replaced often, but the Service stays stable.

Services solve the problem of changing Pod IPs.

### Ingress

Ingress is used for HTTP and HTTPS routing from outside the cluster. It routes traffic based on host or path rules.

### NetworkPolicy

NetworkPolicy allows you to define which Pods can talk to other Pods or external systems. Without it, many clusters allow broad east-west traffic by default.

## Kubernetes Networking Rules

For Kubernetes networking to work correctly, the cluster should satisfy these rules:

- each Pod has a unique IP
- Pods on the same node can communicate
- Pods on different nodes can communicate
- containers inside a Pod can communicate through `localhost`
- Services can forward traffic to healthy backend Pods

This is usually implemented by a CNI plugin.

## What Is CNI?

CNI stands for Container Network Interface. It is the networking layer that makes Pod networking possible.

Common CNI implementations include:

- Calico
- Cilium
- Flannel
- Weave Net

The CNI plugin is responsible for things like:

- assigning Pod IP addresses
- wiring routes between nodes
- enforcing network policies in many environments
- connecting Pods to the cluster network

If Pod-to-Pod communication is broken, the CNI layer is one of the first things to check.

## Pod-to-Pod Communication

Pods can communicate directly by IP, but that is usually not the preferred long-term design because Pod IPs are ephemeral.

Example:

```bash
kubectl get pods -o wide
```

Sample output:

```text
NAME                         READY   STATUS    IP            NODE
web-7f7b8c9d9f-4r8v6        1/1     Running   10.244.1.10   worker-1
api-6fd8c67c4f-zzr8h        1/1     Running   10.244.2.15   worker-2
```

If the `web` Pod talks directly to `10.244.2.15`, that works only as long as the `api` Pod keeps that IP. If the Pod is rescheduled, the IP changes.

That is why applications normally talk to a Service instead of directly to Pod IPs.

## Service Discovery with DNS

Kubernetes includes an internal DNS service, usually CoreDNS.

When you create a Service, Kubernetes also creates a DNS name for it.

For a Service named `api` in the `default` namespace, these names are commonly usable:

- `api`
- `api.default`
- `api.default.svc`
- `api.default.svc.cluster.local`

Inside the cluster, a Pod can call:

```bash
curl http://api:8080
```

instead of hardcoding a Pod IP.

## ClusterIP Service

`ClusterIP` is the default Service type. It exposes the application only inside the cluster.

Use it when:

- one microservice talks to another microservice
- a frontend talks to an internal API
- a worker talks to a database proxy inside the cluster

Example:

```yaml
apiVersion: v1
kind: Service
metadata:
	name: api-service
spec:
	selector:
		app: api
	ports:
		- port: 80
			targetPort: 8080
	type: ClusterIP
```

Explanation:

- `port` is the port exposed by the Service
- `targetPort` is the port the container listens on
- `selector` matches Pods with label `app: api`

Traffic flow:

`client Pod -> Service ClusterIP -> backend Pod targetPort`

## NodePort Service

`NodePort` exposes a Service on a port on every node.

Use it when:

- you need simple external access
- you are testing in Minikube or a lab environment
- you do not have a cloud load balancer

Example:

```yaml
apiVersion: v1
kind: Service
metadata:
	name: api-nodeport
spec:
	type: NodePort
	selector:
		app: api
	ports:
		- port: 80
			targetPort: 8080
			nodePort: 30080
```

Traffic flow:

`client -> nodeIP:30080 -> Service -> Pod:8080`

Notes:

- the default NodePort range is usually `30000-32767`
- every node listens on that NodePort
- this is functional, but not usually the best production entry pattern for web apps

## LoadBalancer Service

`LoadBalancer` creates an external load balancer in supported cloud environments.

Use it when:

- you want public access to a Service
- your cloud provider supports external load balancers
- you want a stable external IP or hostname

Example:

```yaml
apiVersion: v1
kind: Service
metadata:
	name: api-loadbalancer
spec:
	type: LoadBalancer
	selector:
		app: api
	ports:
		- port: 80
			targetPort: 8080
```

Traffic flow:

`client -> cloud load balancer -> node -> Service -> Pod`

## ExternalName Service

`ExternalName` maps a Service to an external DNS name.

Example:

```yaml
apiVersion: v1
kind: Service
metadata:
	name: external-db
spec:
	type: ExternalName
	externalName: mydb.example.com
```

This does not proxy traffic. It creates a DNS alias.

## Ingress

Ingress is normally used for HTTP and HTTPS traffic when you want one entry point for multiple services.

Common use cases:

- `example.com` goes to the frontend service
- `example.com/api` goes to the backend API
- `admin.example.com` goes to the admin service

Example:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
	name: app-ingress
spec:
	ingressClassName: nginx
	rules:
		- host: example.local
			http:
				paths:
					- path: /
						pathType: Prefix
						backend:
							service:
								name: web-service
								port:
									number: 80
					- path: /api
						pathType: Prefix
						backend:
							service:
								name: api-service
								port:
									number: 80
```

Ingress does not work by itself. You need an Ingress Controller such as:

- NGINX Ingress Controller
- Traefik
- HAProxy Ingress

## kube-proxy and Service Routing

When a Pod sends traffic to a Service IP, Kubernetes needs to translate that virtual Service endpoint to one of the real backend Pods.

That job is commonly handled by `kube-proxy`.

Depending on cluster configuration, `kube-proxy` may use:

- `iptables`
- `ipvs`
- eBPF-based alternatives in some environments

The result is that a request to the Service IP is forwarded to one of the matching Pods.

## Endpoints and EndpointSlices

When a Service selects Pods, Kubernetes tracks the actual backend addresses.

You can inspect them with:

```bash
kubectl get endpoints
kubectl get endpointslices.discovery.k8s.io
```

If a Service exists but has no endpoints, the selector may not match any Pods, or the Pods may not be ready.

## Example: Deployment plus Service

Here is a basic example of an app Deployment and an internal ClusterIP Service.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
	name: demo-api
spec:
	replicas: 2
	selector:
		matchLabels:
			app: demo-api
	template:
		metadata:
			labels:
				app: demo-api
		spec:
			containers:
				- name: api
					image: nginx:stable
					ports:
						- containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
	name: demo-api-service
spec:
	selector:
		app: demo-api
	ports:
		- port: 80
			targetPort: 80
	type: ClusterIP
```

Apply it:

```bash
kubectl apply -f demo-api.yaml
```

Verify it:

```bash
kubectl get pods -o wide
kubectl get svc
kubectl get endpoints demo-api-service
```

## Testing Connectivity from Inside the Cluster

One of the easiest ways to troubleshoot networking is to launch a temporary Pod and test DNS and HTTP from inside the cluster.

Example:

```bash
kubectl run netshoot --rm -it \
	--image=nicolaka/netshoot \
	--restart=Never -- bash
```

Inside that Pod, test:

```bash
nslookup demo-api-service
curl http://demo-api-service
ping demo-api-service
```

`ping` may be blocked in some environments, so `curl`, `wget`, `dig`, and `nslookup` are often more useful.

## Namespace and DNS Behavior

DNS resolution depends on namespace.

If your client Pod is in the same namespace as the Service, using just the short Service name is usually enough:

```bash
curl http://demo-api-service
```

If the Service is in another namespace, use the namespace-qualified name:

```bash
curl http://demo-api-service.backend
```

Or the full name:

```bash
curl http://demo-api-service.backend.svc.cluster.local
```

## NetworkPolicy Basics

By default, traffic inside a cluster is often open unless NetworkPolicy is enabled and enforced by the CNI plugin.

NetworkPolicy lets you define:

- which Pods can receive traffic
- which Pods can send traffic
- which ports and protocols are allowed

Example: only allow Pods with label `app: web` to call Pods with label `app: api` on TCP port 8080.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
	name: allow-web-to-api
spec:
	podSelector:
		matchLabels:
			app: api
	policyTypes:
		- Ingress
	ingress:
		- from:
				- podSelector:
						matchLabels:
							app: web
			ports:
				- protocol: TCP
					port: 8080
```

Important:

- NetworkPolicy only works if your CNI plugin supports it
- once policies are applied, unexpected traffic blocks are common if rules are incomplete

## Egress Traffic

Ingress traffic means traffic entering a Pod.
Egress traffic means traffic leaving a Pod.

Many real systems need to control egress to:

- databases
- external APIs
- package repositories
- internal services in other namespaces

Example egress policy patterns include:

- allow DNS to CoreDNS
- allow HTTPS to a known external API
- block all other outbound traffic

## Common Traffic Paths

### 1. Pod to Pod

`frontend Pod -> backend Pod IP`

Possible, but not ideal for application design.

### 2. Pod to Service

`frontend Pod -> backend Service DNS -> backend Pod`

This is the normal pattern.

### 3. External Client to NodePort

`browser -> nodeIP:nodePort -> Service -> Pod`

### 4. External Client to LoadBalancer

`browser -> external load balancer -> Service -> Pod`

### 5. External Client to Ingress

`browser -> Ingress Controller -> Service -> Pod`

## Port Terms You Must Not Confuse

These are commonly mixed up:

- `containerPort`: port exposed by the container definition
- `targetPort`: port the Service forwards traffic to on the Pod
- `port`: port exposed by the Service
- `nodePort`: external port opened on each node for a NodePort Service

Example:

```yaml
ports:
	- port: 80
		targetPort: 8080
		nodePort: 30080
```

This means:

- clients call the Service on port `80`
- the Service forwards to Pod port `8080`
- if type is `NodePort`, nodes also listen on `30080`

## DNS Troubleshooting

If a Service name does not resolve:

1. check that the Service exists
2. check the namespace
3. check CoreDNS Pods
4. test from inside another Pod

Useful commands:

```bash
kubectl get svc
kubectl get pods -n kube-system
kubectl get configmap coredns -n kube-system -o yaml
kubectl exec -it <pod-name> -- nslookup kubernetes.default
```

## Service Troubleshooting

If traffic reaches the Service but the app still fails, check these items:

### Selector mismatch

The Service selector must match Pod labels.

```bash
kubectl get svc demo-api-service -o yaml
kubectl get pods --show-labels
```

### No endpoints

```bash
kubectl get endpoints demo-api-service
```

If no endpoints appear, the Service has no healthy backend Pods.

### Wrong targetPort

If the container listens on `8080` but the Service forwards to `80`, traffic fails.

### Readiness probe failures

Pods may be running but excluded from Service endpoints if readiness probes are failing.

```bash
kubectl describe pod <pod-name>
```

### NetworkPolicy block

Traffic may be denied by policy even when DNS and Service configuration look correct.

```bash
kubectl get networkpolicy
kubectl describe networkpolicy <policy-name>
```

## Ingress Troubleshooting

If Ingress does not work:

1. verify the Ingress Controller is installed
2. confirm the Ingress resource is using the correct `ingressClassName`
3. confirm DNS points to the controller or load balancer
4. check backend Service and endpoints
5. inspect controller logs

Useful commands:

```bash
kubectl get ingress
kubectl describe ingress app-ingress
kubectl get pods -A | grep -i ingress
kubectl logs -n ingress-nginx deploy/ingress-nginx-controller
```

## Quick Lab on Minikube

If you are learning locally with Minikube, this is a simple workflow:

1. start Minikube
2. deploy a sample app
3. create a ClusterIP Service
4. test from another Pod
5. expose with NodePort or Ingress

Example:

```bash
minikube start
kubectl create deployment hello-minikube --image=kicbase/echo-server:1.0
kubectl expose deployment hello-minikube --port=8080 --target-port=8080
kubectl get svc hello-minikube
```

To test from inside the cluster:

```bash
kubectl run curlpod --image=curlimages/curl:8.7.1 --rm -it --restart=Never -- \
	curl http://hello-minikube:8080
```

To expose it externally with NodePort:

```bash
kubectl expose deployment hello-minikube --type=NodePort --name=hello-nodeport --port=8080
minikube service hello-nodeport
```

To enable Ingress on Minikube:

```bash
minikube addons enable ingress
kubectl get pods -n ingress-nginx
```

## Best Practices

- use Services instead of Pod IPs
- use labels consistently so selectors stay predictable
- keep internal traffic on ClusterIP when external exposure is not needed
- use Ingress for HTTP and HTTPS routing instead of many separate LoadBalancers
- add NetworkPolicy for least-privilege communication
- test from inside the cluster before assuming the issue is external
- verify readiness probes because they directly affect Service endpoints

## Common Interview-Level Questions

### Why not call Pods directly by IP?

Because Pod IPs change when Pods are recreated or rescheduled.

### What is the difference between Service and Ingress?

A Service exposes an application inside the cluster or at layer 4, while Ingress handles layer 7 HTTP and HTTPS routing into the cluster.

### Does Ingress replace Service?

No. Ingress usually routes to Services, and Services route to Pods.

### Why does a Service exist but not forward traffic?

Common reasons are selector mismatch, no ready Pods, wrong targetPort, or blocked traffic by NetworkPolicy.

## Summary

Kubernetes networking becomes much easier once you keep the layers clear:

- Pods get IPs
- Services give stable access to Pods
- DNS makes Services discoverable
- Ingress manages web traffic into the cluster
- NetworkPolicy restricts who can talk to whom
- CNI makes the whole data path possible

If you can trace traffic using this path,

`client -> Ingress or Service -> endpoints -> Pod`,

you can usually find the networking problem quickly.

## Ref

- https://kubernetes.io/docs/concepts/cluster-administration/networking/
- https://kubernetes.io/docs/concepts/services-networking/service/
- https://kubernetes.io/docs/concepts/services-networking/ingress/
- https://kubernetes.io/docs/concepts/services-networking/network-policies/
- https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/

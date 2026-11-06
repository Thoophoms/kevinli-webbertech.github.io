# Introduction to Kubernetes Ingress

## What is Ingress?

In Kubernetes, **Ingress** is an API object that manages external HTTP/S access to cluster services, providing routing rules, 
SSL termination, and load balancing. It acts as a reverse proxy, reducing the need for multiple load balancers. Key components include the Ingress resource (rules) and 
an Ingress Controller (e.g., NGINX, Traefik) that implements them.

## Why Use Ingress? (Real-World Analogy)

Think of Ingress like a **restaurant host**:

- **Without Ingress**: You have to know exactly which table (Pod) to go to --this is like using
NodePort or LoadBalancer services directly.
- **With Ingress**: The host (Ingress) takes your request ("I want the Web App Menu") and directs
you to the right table (Service) based on predefined rules.

## Common Use Cases

1. **Host-Based Routing**: Serve multiple websites (e.g., blog.example.com, shop.example.com) 
from the same cluster.
2. **Path-Based Routing**: Different paths (/api, /app) route to different backend services.
3. **TLS/SSL Termination**: Handle HTTPS encryption at the Ingress level instead of inside Pods.
4. **Load Balancing**: Distribute traffic across multiple backend services.


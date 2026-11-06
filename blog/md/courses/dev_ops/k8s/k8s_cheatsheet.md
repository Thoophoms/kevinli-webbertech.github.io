#### This cheatsheet provides a quick reference to the most commonly used kubectl commands for developers and operators. Whether you're just getting started or need a refresher, this guide covers day-to-day tasks like deploying apps, inspecting cluster state, debugging pods, and managing resources.


# Setup & Configuration

```
kubectl version                                 # Show kubectl & cluster version
kubectl config view                             # View kubeconfig details
kubectl config use-context <context>            # Switch context
kubectl config current-context                  # Show current context
alias k=kubectl                                 # Create alias
source <(kubectl completion bash|zsh)           # Enable shell autocompletion
```

# Creating & applying Resources

```
kubectl apply -f <file.yaml>                                                                    # Apply config from file
kubectl create -f <file.yaml>                                                                   # Create resource from YAML
kubectl delete -f <file.yaml>                                                                   # Delete resource via YAML
kubectl create deplyoment <name> --image=nginx                                                  # Creates a deployment named name running the latest nginx container
kubectl expose deployment <name> --port=80 --target-port=80 --type=NodePort                     # Creates a Service named name (same as deployment) and makes the NGINX server accessible via nay node's IP at a high-numbered port
```

# Working with Resources

```
kubectl get pods                            # List all pods
kubectl get svc                             # List services
kubectl get deployments                     # List deployments
kubectl get all                             # List all resources in namespace
kubectl describe pod <pod-name>             # Show pod details
kubectl delete pod <pod-name>               # Delete pod
```

# Namespaces

```
kubectl get namespaces                                              # List all namespaces in the cluster
kubectl create namespace <name>                                     # Create a new namespace named <name>
kubectl delete namespace <name>                                     # Delete the namespace <name> and all its resources
kubectl config set-context --current --namespace=<name>             # Set <name> as the default namespace for the current context
```

# Logs, Exec & Debugging

```
kubectl logs <pod>                          # View logs
kubectl logs <pod> -c <container>           # Logs from specific container
kubectl exec -it <pod> `` /bin/sh           # Shell into container
kubectl get events                          # View recent cluster events
kubectl explain pod                         # Display API schema
```

# Deployment & Rollouts

```
kubectl rollout status deployment/<name>                                # Check rollout progress
kubectl rollout undo deployment/<name>                                  # Rollback to previous version
kubectl scale deployment <name> --replicas=3                            # Scale the deployment <name> to 3 replicas (pods)
kubectl set image deployment/<name> <container>=<new-image>             # Update the container image in the deployment <name> to <new-image>
```

# Monitoring

```
kubectl top nodes               # CPU & Memory for nodes
kubectl top pods                # CPU & Memory for pods
```

# Networking & Port Forwarding

```
kubectl port-forward svc/<svc-name> 8080:80             # Forward local port 8080 to port 80 of the service <svc-name>
kubectl port-forward pod/<pod-name> 8080:80             # Forward local port 8080 to port 80 of the pod <pod_name>
kubectl proxy                                           # Run local proxy to API server
```

# Labels & Selectors

```
kubectl label pod <pod> env=prod                                    # Add a label "env=prod" to the pod <pod>
kubectl get pods -l env=prod                                        # List pods with the label "env=prod"
kubectl annotate pod <pod> description='My test pod'                # Add an annotation with a description to the pod <pod>
```

# RBAC & Access Control

```
kubectl auth can-i get pods                                     # Check if the current user can perform 'get' on pods
kubectl auth can-i delete svc --as=user@example.com             # Check if user@example.com can perform 'delete' on services
```

# Miscellaneous

```
kubectl get nodes                                       # List cluster nodes
kubectl cordon <node>                                   # Mark node unschedulable
kubectl drain <node> --ignore-daemonsets                # Evict pods from node
kubectl uncordon <node>                                 # Make node schedulable
```
# Introduction to Kubernetes (K8s)

### **What is Kubernetes?**  
**Kubernetes (K8s)** is an open-source **container orchestration platform** designed to automate the deployment, scaling, and management of containerized applications. It was originally developed by **Google** and is now maintained by the **Cloud Native Computing Foundation (CNCF)**.  

### **Key Features of Kubernetes**  
1. **Container Orchestration**  
   - Manages Docker (or other container runtime) workloads across clusters of machines.  
   - Handles scheduling, scaling, and failover automatically.  

2. **Self-Healing & High Availability**  
   - Automatically restarts failed containers.  
   - Replaces unresponsive nodes and ensures desired state.  

3. **Load Balancing & Scaling**  
   - Distributes traffic across containers for optimal performance.  
   - Supports **horizontal scaling** (adding more containers) and **vertical scaling** (increasing container resources).  

4. **Declarative Configuration**  
   - Uses **YAML/JSON** files to define the desired state (e.g., *"Run 5 copies of this app"*).  

5. **Multi-Cloud & Hybrid Support**  
   - Runs on **AWS, Azure, GCP, on-premises**, and even **Raspberry Pi clusters**.  

6. **Extensible Ecosystem**  
   - Supports **plugins, operators, and custom resources** (CRDs) for advanced use cases.  

---

### **Core Kubernetes Components**  
| **Component**       | **Function** |
|---------------------|-------------|
| **Cluster** | A set of worker machines (nodes) running containerized apps. |
| **Node** | A physical/virtual machine running containers (via **kubelet**). |
| **Pod** | Smallest deployable unit (1+ containers sharing storage/network). |
| **Deployment** | Manages replica sets of pods (for scaling/updates). |
| **Service** | Exposes pods as network services (e.g., load-balanced IP). |
| **Ingress** | Manages external HTTP(S) access to services. |
| **ConfigMap & Secret** | Stores configuration data and sensitive info (e.g., passwords). |
| **Volume** | Persistent storage for pods. |
| **kubectl** | CLI tool to interact with Kubernetes. |

---

### **Why Use Kubernetes?**  
✅ **Scalability**: Easily scale apps up/down based on demand.  
✅ **Fault Tolerance**: Automatically recovers from failures.  
✅ **Portability**: Runs anywhere (cloud, on-prem, edge).  
✅ **DevOps & CI/CD Friendly**: Integrates with tools like **Helm, ArgoCD, Jenkins**.  

### **Example Use Cases**  
- Microservices architectures  
- Machine learning workflows  
- Web apps with variable traffic  
- Batch processing jobs  

---

### **Kubernetes vs. Docker**  
- **Docker** is for **creating and running containers** on a single host.  
- **Kubernetes** is for **orchestrating containers across multiple hosts** (clusters).  


## K8s Architecture

### **1. Kubernetes Architecture (Master & Worker Nodes)**  
- **Control Plane (Master):**  
  - **kube-apiserver** → Entry point for all commands.  
  - **etcd** → Key-value store for cluster state.  
  - **kube-scheduler** → Assigns pods to nodes.  
  - **kube-controller-manager** → Handles node/pod replication.  
- **Worker Nodes:**  
  - **kubelet** → Ensures containers run in pods.  
  - **kube-proxy** → Manages network rules.  
  - **Container Runtime** (e.g., Docker, containerd).  

---

### **2. Networking in Kubernetes**  
- **Pods** get unique IPs (but ephemeral).  
- **Services** provide stable IPs/DNS names:  
  - **ClusterIP** (internal), **NodePort** (external access), **LoadBalancer** (cloud-provided LB).  
- **Ingress** → Routes HTTP traffic (e.g., Nginx, Traefik).  
- **CNI Plugins** (Calico, Flannel) handle pod-to-pod communication.  

---

### **3. Storage & Volumes**  
- **Ephemeral Storage** (dies with pod).  
- **PersistentVolumes (PV)** → Long-term storage (e.g., AWS EBS, NFS).  
- **PersistentVolumeClaims (PVC)** → Pods "claim" PVs.  
- **StatefulSets** → For stateful apps (e.g., databases).  

---

### **4. Security (RBAC, Pod Policies, Secrets)**  
- **RBAC** → Role-based access control (e.g., `kubectl create role`).  
- **Network Policies** → Restrict pod communication (e.g., `deny-all` by default).  
- **Secrets** → Store sensitive data (base64-encoded).  
- **Pod Security Contexts** → Run as non-root, read-only filesystems.  

---

### **5. Scaling & Autoscaling**  
- **Horizontal Pod Autoscaler (HPA)** → Scales pods based on CPU/memory.  
- **Vertical Pod Autoscaler (VPA)** → Adjusts CPU/memory limits.  
- **Cluster Autoscaler** → Adds/removes nodes (cloud-only).  

---

### **6. Kubernetes Operators & Custom Resources (CRDs)**  
- **Operators** → Automate app management (e.g., databases, Prometheus).  
- **Custom Resource Definitions (CRDs)** → Extend Kubernetes API.  

---

### **7. Monitoring & Logging**  
- **Metrics Server** → Basic CPU/memory metrics.  
- **Prometheus + Grafana** → Advanced monitoring.  
- **EFK Stack** (Elasticsearch, Fluentd, Kibana) → Logging.  

---

### **8. Kubernetes Tools & Ecosystem**  
- **Helm** → Package manager for K8s (charts).  
- **k9s** → Terminal UI for Kubernetes.  
- **ArgoCD** → GitOps-based deployment tool.  
- **Istio** → Service mesh (mTLS, traffic control).  

---

### **9. Kubernetes on Different Platforms**  
- **Minikube** → Local single-node cluster.  
- **k3s** → Lightweight K8s for edge/IoT.  
- **EKS (AWS), GKE (Google), AKS (Azure)** → Managed K8s services.  

---

### **10. Common Challenges & Best Practices**  
- **Anti-Patterns:**  
  - Running single-replica stateful apps.  
  - Using `latest` tags for images.  
- **Best Practices:**  
  - Use namespaces for isolation.  
  - Set resource limits (`requests`/`limits`).  
  - Immutable containers (no SSH inside pods).  

---
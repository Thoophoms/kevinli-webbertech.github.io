# Amazon EKS (Elastic Kubernetes Service) 

Amazon EKS (Elastic Kubernetes Service) cheat sheet to assist you in managing your Kubernetes clusters on AWS.

Got it 👍 — Amazon **EKS** (Elastic Kubernetes Service) is AWS’s managed Kubernetes offering. Here’s a structured overview for you:

---

## 🚀 Amazon EKS (Elastic Kubernetes Service)

### 🔹 What it is

* A **fully managed Kubernetes control plane** hosted on AWS.
* Lets you run Kubernetes without needing to manage your own master/control plane nodes.
* Works seamlessly with other AWS services (VPC, IAM, CloudWatch, ALB, etc.).

---

### 🔹 Key Features

* **Managed Control Plane**: AWS runs and scales the Kubernetes control plane across multiple Availability Zones.
* **Integration with AWS Services**: Deep integration with IAM (for RBAC), ELB/ALB (for ingress), CloudWatch (for logging/monitoring), and EBS/EFS (for persistent storage).
* **Fargate Support**: Run Kubernetes pods on AWS Fargate without managing EC2 worker nodes.
* **Multi-region Availability**: High availability via cross-AZ replication.
* **Security**: IAM roles for service accounts, private endpoints, encryption, security groups.

---

### 🔹 Components

1. **EKS Cluster**

   * Control plane managed by AWS.
   * Worker nodes (EC2 or Fargate) inside your VPC.
2. **Node Groups**

   * Managed node groups (AWS provisions EC2s).
   * Self-managed node groups (you manage lifecycle).
3. **Networking**

   * Uses Amazon VPC CNI plugin for pod networking.
4. **Add-ons**

   * CoreDNS, kube-proxy, VPC CNI managed as EKS add-ons.
   * Can install Helm charts for monitoring/logging/CI-CD.

---

### 🔹 Typical Workflow

1. **Create an EKS Cluster** (via console, CLI, or Terraform/CloudFormation).
2. **Configure kubectl** using `aws eks update-kubeconfig`.
3. **Add worker nodes** (EC2 managed node group or Fargate profiles).
4. **Deploy workloads** using Kubernetes manifests/Helm.
5. **Integrate with AWS services** for ingress, storage, monitoring, secrets.

---

### 🔹 Common Use Cases

* Running **microservices** in production.
* **Hybrid workloads** with on-prem + cloud.
* **Machine learning & data pipelines** (integrates with SageMaker, EMR).
* **Multi-tenant SaaS platforms**.

---

### 🔹 CLI Quick Commands

```bash
# Update kubeconfig for EKS cluster
aws eks update-kubeconfig --region us-east-1 --name my-cluster

# List clusters
aws eks list-clusters

# List nodes once connected
kubectl get nodes

# Deploy an app
kubectl apply -f deployment.yaml
```

---


## 🛠️ AWS EKS Cheat Sheet

### **Cluster Management**

* **Create a Cluster**:

  ```bash
  aws eks create-cluster --name my-cluster --role-arn arn:aws:iam::account-id:role/role-name --resources-vpc-config subnetIds=subnet-xxxxxx,securityGroupIds=sg-xxxxxx
  ```

* **Delete a Cluster**:

  ```bash
  aws eks delete-cluster --name my-cluster
  ```

* **Describe a Cluster**:

  ```bash
  aws eks describe-cluster --name my-cluster
  ```

### **Node Group Management**

* **Create Node Group**:

  ```bash
  aws eks create-nodegroup --cluster-name my-cluster --nodegroup-name my-nodegroup --subnets subnet-xxxxxx --instance-types t3.medium --ami-type AL2_x86_64
  ```

* **Delete Node Group**:

  ```bash
  aws eks delete-nodegroup --cluster-name my-cluster --nodegroup-name my-nodegroup
  ```

### **IAM & Authentication**

* **Update kubeconfig**:

  ```bash
  aws eks update-kubeconfig --name my-cluster
  ```

* **Get Cluster Endpoint**:

  ```bash
  aws eks describe-cluster --name my-cluster --query "cluster.endpoint"
  ```

### **kubectl Commands**

* **Get Nodes**:

  ```bash
  kubectl get nodes
  ```

* **Get Pods**:

  ```bash
  kubectl get pods
  ```

* **Apply Configuration**:

  ```bash
  kubectl apply -f deployment.yaml
  ```

* **Delete Resource**:

  ```bash
  kubectl delete -f deployment.yaml
  ```

### **Security Best Practices**

* **Use IAM Roles for Service Accounts (IRSA)**:

  * Create an OIDC identity provider for your EKS cluster.
  * Associate IAM roles with Kubernetes service accounts.

* **Enable Control Plane Logging**:

  ```bash
  aws eks update-cluster-config --name my-cluster --logging '{"clusterLogging":[{"types":["api","audit","authenticator","controllerManager","scheduler"],"enabled":true}]}'
  ```

* **Use AWS Secrets Manager**:

  * Store sensitive data and reference it in your Kubernetes manifests.

---

For a more comprehensive guide, you can refer to the following resources:

* [Tutorials Dojo EKS Cheat Sheet](https://tutorialsdojo.com/amazon-elastic-kubernetes-service-eks/)
* [AWS CLI EKS Examples](https://docs.aws.amazon.com/cli/v1/userguide/cli_eks_code_examples.html)
* [Kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
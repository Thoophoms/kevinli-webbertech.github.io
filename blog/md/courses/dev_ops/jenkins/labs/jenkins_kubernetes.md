# Jenkins Meets Kubernetes: A Step-by-Step Guide to Integration Using Minikube

## Overview
This guide walks through the process of integrating Jenkins with Kubernetes using Minikube on a Windows machine. It covers setup, deployment, troubleshooting, and lessons learned along the way. This tutorial is especially useful for beginners working in constrained environments (e.g., university-issued machines) or using Docker as a Minikube driver.

**Environment Setup:**

* Windows 11 PC (with PowerShell & admin access)

* Docker Desktop

* Minikube

* Jenkins (via Docker)

* kubectl CLI

**Primary Commands:**
```
minikube start
kubectl cluster-info
minikube service jenkins --url
minikube ip 
```
Run these from an elevated PowerShell terminal. If using a restricted user account, ensure admin credentials are applied.


## Minikube Setup with Hyper-V
First, enable virtualization in BIOS and install Hyper-V on Windows. Attempts to launch Minikube with Hyper-V may fail due to memory limits (e.g., insufficient memory to allocate 2200MB or even 1800MB). If that happens:

1. Try lowering memory allocation via:
```
minikube start --driver=hyperv --memory=1800
```
2. If issues persist, delete the existing cluster:
```
minikube delete --all --purge
```
3. Alternatively, switch to Docker:
```
minikube start --driver=docker --memory=1800
```
Tip: Docker driver is more reliable in low-memory environments or where Hyper-V switching is problematic.

## Virtual Switch Setup (For Hyper-V Users)
If Hyper-V is used:

* Open Hyper-V Manager as admin.

* Go to Virtual Switch Manager.

* Create a New External Network Switch.

* Name it **MinikubeSwitch**.

* Bind it to the correct internet-enabled network adapter.

This step ensures that Minikube can communicate externally.

## Jenkins Deployment
Create a Kubernetes deployment YAML (jenkins-deployment.yaml) with a Jenkins Deployment and Service. Apply it using:

```
kubectl apply -f jenkins-deployment.yaml
```
Verify deployment:
```
kubectl get svc
kubectl get pods
```
If attempting to start Jenkins via Docker after this, expect failure — Jenkins is now running inside Kubernetes.

**Common mistake: Docker Jenkins vs K8s Jenkins:**

If running:
```
docker start jenkins
```
and seeing container-not-found errors, it’s likely Jenkins is only deployed in Kubernetes.

To access Jenkins locally (if needed), use:
```
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```
Then access Jenkins via: **http://localhost:8080**

Retrieve admin password:

```
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

## Connecting Jenkins to Minikube
To connect Jenkins to the Kubernetes cluster:

1. Display kubeconfig:

```
type $env:USERPROFILE\.kube\config
```
2. Save the file to an accessible location (e.g., Downloads) as kubeconfig.txt

3. In Jenkins:

* Go to Manage Jenkins > Credentials

* Add a Secret file

* Upload kubeconfig.txt

4. If the correct credential type isn't visible:

* Install Kubernetes Credentials Provider Plugin.

* Restart Jenkins:
```
docker restart jenkins
```

**Jenkins Kubernetes Cloud Configuration:**
1. Install Kubernetes Plugin from Jenkins Plugin Manager

2. Navigate to:

* Manage Jenkins > Configure System

* Scroll to the Cloud section

* Click Add New Cloud > Kubernetes

3. Configure:

* Kubernetes URL: Use output from minikube ip, typically https://192.168.49.2:8443

* Credentials: Select the kubeconfig.txt secret

* Optionally disable WebSockets and direct connection

If connection test fails with kubernetes.default.svc error, it’s likely Jenkins is running outside the cluster.

## Deploying Jenkins in Minikube and Using Minikube Docker Daemon

To avoid networking issues:

1. Point terminal to Minikube Docker daemon:
```
& minikube -p minikube docker-env | Invoke-Expression
```
2. Pull Jenkins Docker image inside Minikube:
```
docker pull jenkins/jenkins:lts
```
3. Create a new jenkins.yaml file for Kubernetes deployment. Save it as type “All Files”.

Example: 
```
apiVersion: v1
kind: Service
metadata:
  name: jenkins
spec:
  type: NodePort
  ports:
    - port: 8080
      targetPort: 8080
      nodePort: 30000
  selector:
    app: jenkins
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jenkins
spec:
  replicas: 1
  selector:
    matchLabels:
      app: jenkins
  template:
    metadata:
      labels:
        app: jenkins
    spec:
      containers:
        - name: jenkins
          image: jenkins/jenkins:lts
          ports:
            - containerPort: 8080
```

4. Apply the deployment:
```
kubectl apply -f jenkins.yaml
```
5. Access Jenkins:
```
minikube service jenkins --url
```

Log in using the password from:
```
kubectl exec --namespace default -it $(kubectl get pods --namespace default -l app=jenkins -o jsonpath="{.items[0].metadata.name}") -- cat /var/jenkins_home/secrets/initialAdminPassword
```

## Lessons Learned
* Jenkins running outside Kubernetes requires explicit credentials and external IP usage.

* Docker is the more beginner-friendly driver for Minikube on Windows.

* Networking configuration is often the source of Kubernetes integration issues.

* Admin rights and file permissions are critical on university-imaged machines.

* Always read error outputs; they guide the next fix.

## Resources
* **Oluchi Njoku's Article** - Jenkins Meets Kubernetes: My First Integration Experience as a DevOps Intern: https://medium.com/@njokuol/jenkins-meets-kubernetes-my-first-integration-experience-as-a-devops-intern-b5263119d11a

* Minikube Documentation: https://minikube.sigs.k8s.io/docs/

* Jenkins Kubernetes Plugin Guide: https://plugins.jenkins.io/kubernetes/

* Jenkins on Kubernetes via Minikube (Official Tutorial): https://www.jenkins.io/doc/book/installing/kubernetes/

* Docker Desktop Configuration: https://docs.docker.com/desktop/settings/mac/#resources (also applicable for Windows)

* Common Jenkins-K8s Troubleshooting Guide: https://github.com/jenkinsci/kubernetes-plugin#troubleshooting

* Accessing Jenkins via Minikube Tunnel: https://minikube.sigs.k8s.io/docs/handbook/accessing/

This tutorial was prepared as part of a DevOps internship learning journey and may be helpful for other students or engineers setting up local Jenkins–Kubernetes integrations for the first time.

---


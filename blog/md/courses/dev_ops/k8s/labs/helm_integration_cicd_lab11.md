# Helm Chart

Let’s take this a step further and package your application using **Helm** for a more structured and reusable deployment approach. Here’s a step-by-step guide to integrating Helm charts into your **Kubernetes + Nexus + GitHub Actions** pipeline.

## Helm Chart Usage and a better integration

### **1. Create a Basic Helm Chart**

First, you need to create a Helm chart for your application. Run:

```bash
helm create my-app
```

This creates a basic Helm chart structure:

```
my-app/
├── charts/
├── templates/
│   ├── deployment.yaml
│   ├── _helpers.tpl
│   ├── hpa.yaml
│   ├── ingress.yaml
│   ├── service.yaml
│   └── serviceaccount.yaml
├── Chart.yaml
├── values.yaml
└── README.md
```

---

### **2. Customize the Helm Chart**

Update the `values.yaml` file to reflect your Nexus registry settings:

**`my-app/values.yaml`**

```yaml
image:
  repository: nexus.example.com:8081/my-docker-repo/my-app
  tag: latest
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

replicaCount: 2

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 250m
    memory: 256Mi

ingress:
  enabled: true
  className: ""
  annotations: {}
  hosts:
    - host: my-app.example.com
      paths:
        - path: /
          pathType: Prefix
  tls: []

imagePullSecrets:
  - name: nexus-docker-secret
```

---

### **3. Update the Deployment Template**

Update the deployment template to use the values from `values.yaml`:

**`my-app/templates/deployment.yaml`**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-app.fullname" . }}
  labels:
    app: {{ include "my-app.name" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ include "my-app.name" . }}
  template:
    metadata:
      labels:
        app: {{ include "my-app.name" . }}
    spec:
      imagePullSecrets:
      {{- toYaml .Values.imagePullSecrets | nindent 8 }}
      containers:
        - name: {{ include "my-app.name" . }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: {{ .Values.service.port }}
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
```

---

### **4. Push the Helm Chart to Nexus**

Make sure your Nexus instance has a **Helm (Hosted)** repository. Then, package and push the chart:

```bash
helm lint my-app/
helm package my-app/
helm push my-app-0.1.0.tgz oci://nexus.example.com:8081/repository/helm-hosted
```

---

### **5. Update GitHub Actions Workflow**

Update the GitHub Actions workflow to include Helm packaging and pushing:

**`.github/workflows/ci-cd-pipeline.yml`**

```yaml
name: CI/CD Pipeline with Helm

on:
  push:
    branches:
      - main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Log in to nexus Docker Registry
      env:
        DOCKER_SERVER: ${{ secrets.DOCKER_SERVER }}
        DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
        DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
      run: |
        echo "${DOCKER_PASSWORD}" | docker login ${DOCKER_SERVER} -u ${DOCKER_USERNAME} --password-stdin

    - name: Build and Push Docker Image
      env:
        DOCKER_SERVER: ${{ secrets.DOCKER_SERVER }}
        DOCKER_REPO: ${{ secrets.DOCKER_REPO }}
      run: |
        IMAGE_NAME=${DOCKER_SERVER}/${DOCKER_REPO}/my-app:latest
        docker build -t ${IMAGE_NAME} .
        docker push ${IMAGE_NAME}

  helm-deploy:
    runs-on: ubuntu-latest
    needs: build-and-push
    steps:
    - name: Setup kubectl
      uses: azure/setup-kubectl@v3

    - name: Configure kubectl
      env:
        KUBE_CONFIG: ${{ secrets.KUBE_CONFIG }}
      run: |
        echo "${KUBE_CONFIG}" | base64 -d > ~/.kube/config

    - name: Package and Push Helm Chart
      env:
        DOCKER_SERVER: ${{ secrets.DOCKER_SERVER }}
        DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
        DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
      run: |
        helm lint my-app/
        helm package my-app/
        helm push my-app-0.1.0.tgz oci://${DOCKER_SERVER}/repository/helm-hosted

    - name: Deploy via Helm
      env:
        DOCKER_SERVER: ${{ secrets.DOCKER_SERVER }}
      run: |
        helm repo add my-repo oci://${DOCKER_SERVER}/repository/helm-hosted
        helm repo update
        helm upgrade --install my-app my-repo/my-app --namespace default
```

---

### **6. Test the Pipeline**

1. Commit and push your Helm chart and updated workflow file.
2. Make sure your Helm repository in Nexus is accessible.
3. Verify the deployment in your Kubernetes cluster:

```bash
helm ls
kubectl get pods
```

## **1. Helm Chart Versioning and App Version Management**

#### **a. Automate Version Bumping**

We can automate Helm chart versioning using the `git describe` command, which uses git tags for versioning. Add a small script in your GitHub Actions workflow:

**Add a `VERSION` file** (optional but recommended for clarity):

```plaintext
0.1.0
```

#### **b. Update the GitHub Workflow**

Update the workflow to automatically bump the Helm chart version on each push:

```yaml
name: CI/CD Pipeline with Helm Versioning

on:
  push:
    branches:
      - main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Log in to nexus Docker Registry
      env:
        DOCKER_SERVER: ${{ secrets.DOCKER_SERVER }}
        DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
        DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
      run: |
        echo "${DOCKER_PASSWORD}" | docker login ${DOCKER_SERVER} -u ${DOCKER_USERNAME} --password-stdin

    - name: Build and Push Docker Image
      env:
        DOCKER_SERVER: ${{ secrets.DOCKER_SERVER }}
        DOCKER_REPO: ${{ secrets.DOCKER_REPO }}
      run: |
        VERSION=$(cat VERSION)
        IMAGE_NAME=${DOCKER_SERVER}/${DOCKER_REPO}/my-app:${VERSION}
        docker build -t ${IMAGE_NAME} .
        docker push ${IMAGE_NAME}

    - name: Package and Push Helm Chart
      env:
        DOCKER_SERVER: ${{ secrets.DOCKER_SERVER }}
        DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
        DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
      run: |
        VERSION=$(cat VERSION)
        sed -i "s/^version:.*/version: ${VERSION}/" my-app/Chart.yaml
        sed -i "s/^appVersion:.*/appVersion: ${VERSION}/" my-app/Chart.yaml
        helm lint my-app/
        helm package my-app/
        helm push my-app-${VERSION}.tgz oci://${DOCKER_SERVER}/repository/helm-hosted

    - name: Bump Version
      run: |
        VERSION=$(cat VERSION)
        IFS='.' read -r MAJOR MINOR PATCH <<< "$VERSION"
        NEW_VERSION="${MAJOR}.${MINOR}.$((PATCH + 1))"
        echo $NEW_VERSION > VERSION
        git config user.name "github-actions"
        git config user.email "actions@github.com"
        git add VERSION my-app/Chart.yaml
        git commit -m "Bump version to ${NEW_VERSION}"
        git push
```

---

### **2. GitOps Style Deployment with Helm**

To make this more GitOps-friendly, you can:

#### **a. Use a Dedicated GitOps Repository**

Create a separate repository for your Kubernetes manifests or Helm releases. This repo can serve as the **"single source of truth"** for your cluster state.

#### **b. Add Helmfile or ArgoCD (Optional)**

If you want a more comprehensive GitOps approach, consider using **ArgoCD** or **Flux** to automatically sync your cluster with the Helm chart updates.

---

### **3. Update the Helm Chart for Versioning**

Update your Helm chart to reflect the new versioning approach:

**`my-app/values.yaml`**

```yaml
image:
  repository: nexus.example.com:8081/my-docker-repo/my-app
  tag: {{ .Chart.AppVersion }}
  pullPolicy: IfNotPresent
```

**`my-app/Chart.yaml`**

```yaml
apiVersion: v2
name: my-app
description: A Helm chart for my app
version: 0.1.0
appVersion: 0.1.0
```

---

### **4. Testing the Full Pipeline**

1. **Push** your updated Helm chart and workflow file.
2. **Tag** your main branch with an initial version if you haven't already:

```bash
git tag -a v0.1.0 -m "Initial version"
git push origin v0.1.0
```

3. Monitor your GitHub Actions to ensure the version is bumped correctly on each push.

---

### **5. (Optional) Automate Helm Chart Cleanup**

You might want to periodically clean up old Helm chart versions from Nexus to avoid clutter.


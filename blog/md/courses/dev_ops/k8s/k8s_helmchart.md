# Kubernetes Helm Chart Tutorial

## Goal

This tutorial explains what Helm is, why Helm charts are useful in Kubernetes, and how to create, install, upgrade, and debug a basic chart.

By the end, you should understand:

- what Helm does in a Kubernetes workflow
- the structure of a Helm chart
- how `values.yaml` drives configuration
- how templates turn values into Kubernetes manifests
- how to install, upgrade, rollback, and uninstall a release
- how to debug common Helm chart issues

## What Is Helm?

Helm is the package manager for Kubernetes.

If `kubectl` is the tool you use to apply raw YAML, Helm is the tool you use to package, parameterize, and manage that YAML as a reusable application.

Think of Helm like this:

- Kubernetes YAML = source files for infrastructure
- Helm chart = reusable application package
- Helm release = one installed instance of that package in a cluster

## Why Use Helm?

Without Helm, you often end up with many YAML files that are difficult to reuse across environments.

Helm helps when you need:

- a reusable deployment package
- different settings for dev, test, and prod
- versioned releases
- simpler upgrades and rollbacks
- a standard structure for Kubernetes applications

Common examples:

- deploy the same app to dev and prod with different replica counts
- change image tags without editing many YAML files
- install open-source tools like Prometheus, Grafana, or NGINX Ingress quickly

## Core Helm Concepts

### Chart

A chart is a collection of files that describe a Kubernetes application.

### Release

A release is a deployed instance of a chart.

The same chart can be installed multiple times with different release names.

Example:

- chart name: `webapp`
- release names: `webapp-dev`, `webapp-prod`

### Repository

A Helm repository is a place where versioned charts are stored.

Examples:

- Bitnami Helm repository
- internal company chart repository

### Values

Values are the configuration inputs passed into a chart.

They usually live in:

- `values.yaml`
- environment-specific override files
- command-line `--set` or `-f` options

### Templates

Templates are Kubernetes manifest files with placeholders and logic.

Helm renders those templates into plain YAML before sending them to Kubernetes.

## Install Helm

Check whether Helm is already installed:

```bash
helm version
```

If you need installation instructions, use the official docs:

- https://helm.sh/docs/intro/install/

## Create a New Chart

The fastest way to start is:

```bash
helm create webapp
```

That command generates a starter chart directory.

Typical structure:

```text
webapp/
  Chart.yaml
  values.yaml
  charts/
  templates/
    deployment.yaml
    service.yaml
    ingress.yaml
    serviceaccount.yaml
    hpa.yaml
    _helpers.tpl
    tests/
```

## Important Files in a Helm Chart

### Chart.yaml

This file stores chart metadata.

Example:

```yaml
apiVersion: v2
name: webapp
description: A Helm chart for Kubernetes
type: application
version: 0.1.0
appVersion: "1.0.0"
```

Important fields:

- `name`: chart name
- `version`: chart version
- `appVersion`: application version
- `type`: usually `application` or `library`

### values.yaml

This file provides default configuration values.

Example:

```yaml
replicaCount: 2

image:
  repository: nginx
  pullPolicy: IfNotPresent
  tag: "1.27"

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: false
```

This is where you adjust chart behavior without rewriting templates.

### templates/

This directory contains templated Kubernetes resources.

Examples:

- Deployment
- Service
- Ingress
- ConfigMap
- Secret
- ServiceAccount

## How Templating Works

Helm uses Go templating syntax.

Example from a Deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "webapp.fullname" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app.kubernetes.io/name: {{ include "webapp.name" . }}
  template:
    metadata:
      labels:
        app.kubernetes.io/name: {{ include "webapp.name" . }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: 80
```

Common template references:

- `.Values` accesses values from `values.yaml`
- `.Chart` accesses metadata from `Chart.yaml`
- `.Release` accesses release metadata
- `include` reuses helper templates

## Useful Built-In Objects

Helm charts commonly use these objects:

- `.Values`
- `.Release.Name`
- `.Release.Namespace`
- `.Chart.Name`
- `.Chart.Version`

Examples:

```yaml
metadata:
  name: {{ .Release.Name }}-service
```

```yaml
labels:
  chart: {{ .Chart.Name }}-{{ .Chart.Version }}
```

## Example: Minimal Helm Chart Flow

Create a chart:

```bash
helm create demo-app
cd demo-app
```

Render templates locally without installing:

```bash
helm template demo-app .
```

Lint the chart:

```bash
helm lint .
```

Install the chart into Kubernetes:

```bash
helm install demo-app .
```

Check releases:

```bash
helm list
```

Check deployed resources:

```bash
kubectl get all
```

## Install a Chart with Custom Values

You can override values in several ways.

### Option 1: Override with `--set`

```bash
helm install demo-app . \
  --set replicaCount=3 \
  --set image.tag=1.27
```

### Option 2: Override with another values file

Create `values-dev.yaml`:

```yaml
replicaCount: 1
service:
  type: NodePort
image:
  tag: "1.27"
```

Install with it:

```bash
helm install demo-app . -f values-dev.yaml
```

Using files is usually cleaner than very long `--set` commands.

## Upgrade a Release

When the chart or values change, upgrade the release:

```bash
helm upgrade demo-app .
```

Upgrade with a values file:

```bash
helm upgrade demo-app . -f values-prod.yaml
```

Upgrade and install if missing:

```bash
helm upgrade --install demo-app . -f values-prod.yaml
```

That pattern is common in CI and CD pipelines.

## Roll Back a Release

Helm tracks revision history for releases.

View history:

```bash
helm history demo-app
```

Roll back to a previous revision:

```bash
helm rollback demo-app 1
```

This is one of Helm's biggest operational advantages.

## Uninstall a Release

Remove the deployed release:

```bash
helm uninstall demo-app
```

This removes the Kubernetes resources managed by that release unless special retention behavior is configured.

## Preview Changes Before Applying

Before upgrading, render templates locally:

```bash
helm template demo-app . -f values-prod.yaml
```

You can also simulate an install:

```bash
helm install demo-app . --dry-run --debug
```

This is useful for catching template errors before touching the cluster.

## Helm Linting

Run:

```bash
helm lint .
```

This checks for common chart issues such as:

- invalid chart structure
- broken templates
- metadata issues

Linting should be part of your normal workflow.

## Helper Templates

Helm starter charts include `_helpers.tpl`.

This file usually contains reusable snippets for names and labels.

Example:

```gotemplate
{{- define "webapp.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}
```

Why use helpers:

- reduce repeated template logic
- keep naming consistent
- centralize label generation

## Chart Dependencies

Charts can depend on other charts.

Example in `Chart.yaml`:

```yaml
dependencies:
  - name: redis
    version: 19.6.0
    repository: https://charts.bitnami.com/bitnami
```

Update dependencies:

```bash
helm dependency update
```

This pulls dependent charts into the `charts/` directory.

## Namespaces with Helm

Install into a namespace:

```bash
helm install demo-app . --namespace demo --create-namespace
```

List releases across all namespaces:

```bash
helm list -A
```

Many teams keep applications separated by namespace and environment.

## Best Practice: Separate Values by Environment

A common pattern is:

```text
values.yaml
values-dev.yaml
values-test.yaml
values-prod.yaml
```

Example:

- `values.yaml` contains safe defaults
- `values-dev.yaml` enables lightweight settings
- `values-prod.yaml` uses stronger resource limits, autoscaling, and ingress

## Example Production-Oriented Values

```yaml
replicaCount: 3

image:
  repository: myorg/webapp
  tag: "2.1.0"

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: app.example.com
      paths:
        - path: /
          pathType: Prefix

resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 512Mi
```

## Helm Template Debugging

Common commands:

```bash
helm template demo-app .
helm install demo-app . --dry-run --debug
helm get values demo-app
helm get manifest demo-app
helm status demo-app
```

What they help with:

- rendered manifest review
- release configuration inspection
- operational state checks

## Common Helm Problems

### 1. YAML formatting errors

Templates may render invalid YAML because of indentation mistakes.

Typical fix:

- use `nindent` carefully
- render locally with `helm template`

### 2. Wrong values path

If you reference `.Values.imageTag` but the actual file uses `.Values.image.tag`, rendering fails or produces the wrong output.

### 3. Release name conflicts

If a release with the same name already exists in the namespace, `helm install` fails.

Check:

```bash
helm list -A
```

### 4. Resource already exists

A chart may try to create an object that already exists and is not owned by the release.

This is common when mixing raw `kubectl apply` with Helm-managed resources.

### 5. Ingress or Service values do not match cluster reality

Your chart may install successfully, but the application still fails because:

- service ports are wrong
- ingress class is wrong
- selectors do not match Pod labels
- readiness probes keep Pods out of Service endpoints

## Helm vs kubectl

Use `kubectl` when:

- you are learning Kubernetes basics
- you want to inspect raw manifests directly
- you are making a one-off change

Use Helm when:

- you want reusable deployments
- you need environment-based configuration
- you need release history and rollback
- you want a cleaner packaging model for apps

They are not competitors. Helm usually produces manifests, and Kubernetes still applies and runs those resources.

## Helm in CI and CD

A common deployment flow looks like this:

1. application image is built
2. image tag is updated in Helm values
3. chart is linted
4. chart is rendered for validation
5. `helm upgrade --install` deploys the release

This makes Helm a common fit for GitHub Actions, Jenkins, GitLab CI, and Argo-based workflows.

## Basic Lab

Here is a simple learning lab using Minikube.

### Start the cluster

```bash
minikube start
kubectl get nodes
```

### Create the chart

```bash
helm create hello-helm
cd hello-helm
```

### Render the chart

```bash
helm template hello-helm .
```

### Install it

```bash
helm install hello-helm .
```

### Verify resources

```bash
helm list
kubectl get deploy,svc,pods
```

### Upgrade replica count

```bash
helm upgrade hello-helm . --set replicaCount=3
kubectl get deploy
```

### Roll back if needed

```bash
helm history hello-helm
helm rollback hello-helm 1
```

### Remove it

```bash
helm uninstall hello-helm
```

## Best Practices

- keep charts small and readable
- prefer values files over long command-line overrides
- lint charts before installing or upgrading
- render templates locally before production deployment
- keep naming and labels consistent through helper templates
- separate environment configuration into dedicated values files
- avoid mixing manual `kubectl apply` with Helm ownership for the same resources
- version your charts clearly

## Summary

Helm gives Kubernetes a packaging and release workflow.

The most important ideas are:

- chart = package
- values = configuration
- templates = generated manifests
- release = installed instance

If you remember this flow,

`chart + values -> rendered YAML -> release in Kubernetes`,

you can reason through most Helm behavior quickly.

## Ref

- https://helm.sh/docs/
- https://helm.sh/docs/topics/charts/
- https://helm.sh/docs/chart_template_guide/
- https://helm.sh/docs/helm/helm_install/
- https://helm.sh/docs/helm/helm_upgrade/
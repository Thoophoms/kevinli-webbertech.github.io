# Introduction to MLOps

## What is MLOps?

**MLOps** (Machine Learning Operations) is a set of practices that combines Machine Learning, DevOps, and Data Engineering to deploy and maintain ML models in production reliably and efficiently.

MLOps bridges the gap between model development (experimentation) and model deployment (production), applying software engineering best practices to the full ML lifecycle.

---

## Why MLOps?

Without MLOps, ML projects commonly face:

- **Model drift**: Production data changes over time, degrading model accuracy.
- **Reproducibility issues**: Different environments produce different results.
- **Manual deployment**: Slow, error-prone model releases.
- **No monitoring**: Silent failures go undetected.
- **Collaboration friction**: Data scientists and engineers work in silos.

MLOps solves these problems by automating and standardizing the end-to-end ML workflow.

---

## The ML Lifecycle

```
Data Collection → Data Preprocessing → Feature Engineering
       ↓
Model Training → Model Evaluation → Model Validation
       ↓
Model Packaging → Model Deployment → Model Monitoring
       ↓
          Feedback Loop (retrain as needed)
```

### Phases Explained

| Phase | Description |
|---|---|
| **Data Collection** | Gather raw data from databases, APIs, data lakes |
| **Data Preprocessing** | Clean, transform, and validate data quality |
| **Feature Engineering** | Create meaningful input features for models |
| **Model Training** | Train ML algorithms on prepared datasets |
| **Model Evaluation** | Measure accuracy, precision, recall, F1, AUC-ROC |
| **Model Validation** | Confirm the model meets business requirements |
| **Model Packaging** | Containerize model with dependencies (Docker, conda) |
| **Model Deployment** | Serve model via REST API, batch, or streaming |
| **Model Monitoring** | Track data drift, performance degradation, and errors |

---

## Core MLOps Principles

### 1. Versioning
Track versions of data, code, and models together so any experiment is fully reproducible.

- **Code versioning**: Git / GitHub
- **Data versioning**: DVC (Data Version Control)
- **Model versioning**: MLflow, Weights & Biases

### 2. Automation (CI/CD/CT)
Automate training, testing, and deployment pipelines.

- **CI (Continuous Integration)**: Automatically test code and data changes
- **CD (Continuous Delivery)**: Automatically package and stage the model
- **CT (Continuous Training)**: Automatically retrain when data or performance drifts

### 3. Reproducibility
Given the same inputs (data + code + config), always produce the same outputs.

Tools: Docker, conda environments, DVC, MLflow

### 4. Monitoring & Observability
Track model behavior in production:
- **Data drift**: Input distribution has shifted
- **Concept drift**: The relationship between inputs and outputs has changed
- **Performance metrics**: Latency, throughput, error rates

Tools: Evidently AI, Prometheus, Grafana, WhyLogs

### 5. Collaboration
Enable data scientists, ML engineers, and DevOps teams to work together using shared tools and standards.

---

## MLOps Maturity Levels

| Level | Description |
|---|---|
| **Level 0** | Manual process — scripts run locally, models deployed by hand |
| **Level 1** | ML pipeline automation — training pipelines automated, CT enabled |
| **Level 2** | CI/CD pipeline automation — full automation from code commit to production deployment |

Most organizations start at Level 0 and gradually mature toward Level 2.

---

## Key Tools & Technologies

### Experiment Tracking
- **MLflow** — Open-source experiment tracking, model registry
- **Weights & Biases (W&B)** — Visualization and experiment management
- **Neptune.ai** — Metadata store for ML experiments

### Pipeline Orchestration
- **Apache Airflow** — General-purpose workflow scheduler
- **Kubeflow Pipelines** — Kubernetes-native ML pipelines
- **Prefect** — Modern dataflow orchestration
- **ZenML** — MLOps framework designed for portability

### Model Serving
- **FastAPI** — Lightweight REST API for model inference
- **TorchServe** — PyTorch model server
- **TensorFlow Serving** — TensorFlow model server
- **BentoML** — Unified model packaging and serving
- **Seldon Core** — Kubernetes-based model deployment

### Feature Stores
- **Feast** — Open-source feature store
- **Tecton** — Enterprise feature platform
- **Hopsworks** — End-to-end feature store

### Monitoring
- **Evidently AI** — Data and model drift detection
- **WhyLogs** — Data logging and profiling
- **Prometheus + Grafana** — Infrastructure and service monitoring

### Containerization & Infrastructure
- **Docker** — Package model + dependencies
- **Kubernetes** — Orchestrate containerized model services
- **Helm** — Kubernetes package manager for ML deployments

---

## A Simple MLOps Example with MLflow

### Step 1: Install MLflow
```bash
pip install mlflow scikit-learn
```

### Step 2: Train and Track with MLflow
```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Start MLflow run
with mlflow.start_run():
    # Train model
    clf = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)
    clf.fit(X_train, y_train)
    
    # Evaluate
    accuracy = accuracy_score(y_test, clf.predict(X_test))
    
    # Log parameters and metrics
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 3)
    mlflow.log_metric("accuracy", accuracy)
    
    # Log model
    mlflow.sklearn.log_model(clf, "random_forest_model")
    
    print(f"Accuracy: {accuracy:.4f}")
```

### Step 3: View the MLflow UI
```bash
mlflow ui
# Open http://localhost:5000 in your browser
```

### Step 4: Serve the Model
```bash
# Get the run ID from the MLflow UI
mlflow models serve -m "runs:/<RUN_ID>/random_forest_model" -p 1234
```

### Step 5: Make a Prediction
```bash
curl -X POST http://localhost:1234/invocations \
  -H "Content-Type: application/json" \
  -d '{"inputs": [[5.1, 3.5, 1.4, 0.2]]}'
```

---

## CI/CD for ML: A GitHub Actions Example

```yaml
# .github/workflows/ml_pipeline.yml
name: ML Pipeline

on:
  push:
    paths:
      - 'src/**'
      - 'data/**'

jobs:
  train-and-evaluate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run data validation
        run: python src/validate_data.py
      
      - name: Train model
        run: python src/train.py
      
      - name: Evaluate model
        run: python src/evaluate.py
      
      - name: Build Docker image
        run: docker build -t my-model:${{ github.sha }} .
      
      - name: Push to registry
        run: docker push my-registry/my-model:${{ github.sha }}
```

---

## Model Monitoring with Evidently AI

```python
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, ClassificationPreset

# Reference data (training distribution)
reference_data = pd.read_csv("reference_data.csv")

# Current production data
current_data = pd.read_csv("current_data.csv")

# Create drift report
report = Report(metrics=[
    DataDriftPreset(),
    ClassificationPreset(),
])

report.run(reference_data=reference_data, current_data=current_data)
report.save_html("drift_report.html")
print("Report saved to drift_report.html")
```

---

## MLOps vs DevOps

| Aspect | DevOps | MLOps |
|---|---|---|
| Artifact | Application code | Model + code + data |
| Testing | Unit/integration tests | Data validation + model evaluation |
| Deployment trigger | Code commit | Code commit OR data drift OR performance drop |
| Monitoring | Uptime, latency, errors | Data drift, model accuracy, feature statistics |
| Reproducibility | Code + config | Code + config + data + hyperparameters |

---

## Cloud MLOps Platforms

| Platform | Provider |
|---|---|
| **Amazon SageMaker** | AWS |
| **Azure Machine Learning** | Microsoft Azure |
| **Vertex AI** | Google Cloud |
| **Databricks MLflow** | Databricks |

These platforms provide managed infrastructure for the entire ML lifecycle — from data prep through deployment and monitoring.

---

## Summary

MLOps is essential for taking ML models from prototypes to reliable production systems. The key pillars are:

1. **Version everything** — data, code, and models
2. **Automate pipelines** — CI/CD/CT
3. **Monitor continuously** — drift and performance
4. **Containerize for portability** — Docker + Kubernetes
5. **Collaborate through shared platforms** — MLflow, W&B, feature stores

As ML systems grow in complexity, MLOps practices ensure they remain maintainable, reproducible, and trustworthy.

# ML Scan Tools and ML Security Perspective

## Overview
Machine learning systems expand the security scope beyond application code. In MLOps, risk can enter through data, model artifacts, dependencies, containers, CI/CD, and inference endpoints.

A practical approach is to scan early and continuously, then enforce release gates for high-risk findings.

## Threat Surfaces Table

| Threat Surface | Typical Risk | What to Scan |
|---|---|---|
| Training data | Poisoning, hidden triggers, PII leakage | Data quality, drift/outliers, PII patterns, schema anomalies |
| Model artifacts | Backdoored weights, unsafe serialization | Model files, pickle usage, signatures/checksums |
| Feature pipelines | Data exfiltration, logic abuse | ETL code, dependency CVEs, access controls |
| Notebooks | Secret leakage, arbitrary execution | Hardcoded secrets, unsafe shell calls, outputs |
| Dependencies and images | Known CVEs, malicious packages | SBOM, SCA, container/image vulnerabilities |
| Serving endpoints | Prompt injection, model abuse, DoS | API auth, rate limits, input filtering, abuse detection |
| CI/CD and supply chain | Tampered builds, unsigned artifacts | Pipeline configs, provenance, signing/attestation |

## Scan Tool Categories

1. SAST for application and pipeline code.
2. Secrets scanning for keys, tokens, and credentials.
3. SCA/SBOM scanning for vulnerable dependencies.
4. Container/image scanning for OS and package CVEs.
5. IaC scanning for cloud/Kubernetes misconfigurations.
6. Model artifact scanning for unsafe formats and tampering.
7. Data security scanning for PII/policy violations and poisoning indicators.
8. Runtime monitoring for abuse signals and anomalous requests.

## Practical Tools Table

| Category | Common Tools | Practical Use in ML |
|---|---|---|
| SAST | Semgrep, CodeQL, Bandit | Scan training/serving code and CI scripts on PRs |
| Secrets | Gitleaks, TruffleHog | Block credential leaks in notebooks and repos |
| SCA/SBOM | Trivy, Snyk, Syft/Grype | Generate SBOM and fail builds on critical CVEs |
| Container | Trivy, Clair | Scan model-serving images before deploy |
| IaC | Checkov, tfsec, kube-score | Validate Terraform/K8s security posture |
| Model scan | modelscan, custom hash/signature checks | Detect risky serialization and artifact tampering |
| Data scan | Great Expectations, validators + PII detectors | Enforce schema and privacy constraints in training data |
| Runtime | Falco, API gateway/WAF + observability stack | Alert on suspicious model/API behavior post-release |

## CI Gate YAML Example

```yaml
name: ml-security-gate

on:
  pull_request:
  push:
    branches: [main]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Secrets scan
        run: gitleaks detect --source . --exit-code 1

      - name: SAST scan
        run: semgrep --config auto --error

      - name: Dependency and image scan
        run: |
          trivy fs --severity HIGH,CRITICAL --exit-code 1 .
          trivy image --severity CRITICAL --exit-code 1 ml-serving:latest

      - name: Policy gate
        run: echo "Fail if any CRITICAL finding exists"
```

## Checklist

- Define risk thresholds for PR, merge, and release.
- Run scans at pre-commit, PR, merge, and release stages.
- Require signed model artifacts and verify checksums in CI.
- Scan notebooks and data pipelines, not only backend code.
- Generate and store SBOMs for every release.
- Track exceptions with owner and expiration date.
- Add runtime alerts for abuse, drift, and anomalous traffic.

## Summary
ML security is strongest as layered scanning plus enforced gates. Start with secrets, SAST, SCA, and container scanning in CI, then add model/data checks and runtime monitoring across the full lifecycle.

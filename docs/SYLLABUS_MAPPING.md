# Syllabus Mapping (CO1 – CO4)

This table demonstrates how the GradeMind project fulfills the course outcomes (COs) for the syllabus.

| CO  | Syllabus Topic | GradeMind Implementation |
| :--- | :--- | :--- |
| CO1 | SDLC | Project lifecycle documented in `CO1_AGILE.md` |
| CO1 | Agile | Scrum framework, Backlog, and User Stories implemented in `BACKLOG.md` |
| CO1 | Jira/Trello | Project management and Agile tools explained in `CO1_AGILE.md` |
| CO2 | DevOps | CI/CD pipeline implemented via GitHub Actions (`.github/workflows/ci.yml`) |
| CO2 | Git | Git workflow, branching, and commit strategies documented in `CO2_DEVOPS.md` |
| CO2 | Docker | Application containerization implemented via `Dockerfile` and `.dockerignore` |
| CO2 | Kubernetes | Deployment managed via `k8s/deployment.yaml` and `k8s/service.yaml` |
| CO2 | YAML | Configuration used for K8s deployments and GitHub Actions |
| CO2 | Minikube | Local Kubernetes cluster deployment instructions in `MINIKUBE.md` |
| CO2 | Prometheus | Application monitoring implemented via `monitoring/prometheus.yml` |
| CO2 | Grafana | Visualization concepts explained in `CO2_DEVOPS.md` |
| CO2 | AWS/GCP | Cloud deployment strategies outlined in `AWS_SAGEMAKER.md` |
| CO3 | DevSecOps | Integrated security tools in the CI/CD pipeline |
| CO3 | SonarQube | Static code analysis readiness documented in `CO3_SECURITY.md` |
| CO3 | OWASP ZAP | Dynamic Application Security Testing documented in `CO3_SECURITY.md` |
| CO3 | Trivy | Container vulnerability scanning documented in `CO3_SECURITY.md` |
| CO3 | Secure Coding | Input validation in `src/predict.py`, environment variables for secrets |
| CO3 | OWASP Top 10 | Security risks and mitigations documented in `OWASP_TOP10.md` |
| CO3 | GDPR | Data privacy and protection documented in `GDPR.md` |
| CO3 | DVC | Dataset versioning configured via `dvc.yaml` |
| CO3 | MLflow | Experiment tracking integrated into `src/train.py` |
| CO3 | MLOps | End-to-end ML lifecycle documented in `MLOPS.md` |
| CO3 | AI Ethics | Bias, fairness, and responsible AI documented in `AI_ETHICS.md` |
| CO4 | SageMaker | Cloud ML deployment architecture outlined in `AWS_SAGEMAKER.md` |
| CO4 | Cloud CI/CD | ML pipeline cloud integration documented in `AWS_SAGEMAKER.md` |
| CO4 | Cloud Storage | S3 integration for models and data explained in `AWS_SAGEMAKER.md` |
| CO4 | APIs | Flask prediction endpoint acts as a REST API for the ML model |

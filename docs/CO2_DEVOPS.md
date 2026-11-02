# CO2 – DevOps Fundamentals

This document outlines the DevOps practices and tools used in the GradeMind project.

## DevOps Culture
DevOps is a set of practices that combines software development (Dev) and IT operations (Ops). It aims to shorten the systems development life cycle and provide continuous delivery with high software quality. Key aspects include collaboration, automation, continuous integration, continuous delivery, and continuous monitoring.

## Continuous Integration and Continuous Deployment (CI/CD)
CI/CD is a method to frequently deliver apps to customers by introducing automation into the stages of app development.
In GradeMind, we use **GitHub Actions** for our CI/CD pipeline (configured in `.github/workflows/ci.yml`).

### GradeMind CI/CD Pipeline
1. **Git Push**: Code is pushed to the repository.
2. **GitHub Actions**: The automated pipeline triggers.
3. **Install Dependencies**: Python environment is set up and dependencies are installed.
4. **Run Tests**: `pytest` runs unit tests to ensure code correctness.
5. **Run Security Scans**:
   - `Bandit` checks Python code for security issues.
   - `pip-audit` checks dependencies for known vulnerabilities.
6. **Build Docker Image**: The application is packaged into a Docker container for consistent deployment.

## Git Workflow
We follow a structured Git branching strategy:
- `main`: Production-ready code.
- `develop`: Integration branch for new features.
- `feature/*`: Branches for developing specific features (e.g., `feature/prediction-ui`).

### Basic Git Commands
- `git clone <url>`: Download a repository.
- `git checkout -b <branch>`: Create and switch to a new branch.
- `git add <file>`: Stage changes for commit.
- `git commit -m "message"`: Save staged changes with a descriptive message.
- `git push origin <branch>`: Upload local commits to the remote repository.
- `git pull`: Fetch and merge changes from the remote repository.
- `git merge <branch>`: Combine changes from one branch into another.

## Docker
Docker is a platform for developing, shipping, and running applications in containers. Containers package the application code and all its dependencies, ensuring it runs consistently across any environment.
- The `Dockerfile` specifies how to build the GradeMind image (Python 3.11, installing requirements, running Flask).
- `.dockerignore` prevents unnecessary files from being included in the image.

## Kubernetes and Minikube
Kubernetes is a container orchestration system for automating software deployment, scaling, and management. Minikube is a tool that lets you run Kubernetes locally.
See `MINIKUBE.md` for specific instructions on deploying GradeMind locally.
We use YAML configuration files (`k8s/deployment.yaml`, `k8s/service.yaml`) to define the desired state of our application in Kubernetes.

## Monitoring
Monitoring is crucial for understanding the health and performance of the application.
- **Prometheus**: An open-source systems monitoring and alerting toolkit. We configured it (`monitoring/prometheus.yml`) to scrape metrics from our Flask application (using `prometheus-flask-instrumentator`). We track metrics like request count, prediction count, and prediction latency.
- **Grafana**: Can be used alongside Prometheus to visualize these metrics in dashboards.

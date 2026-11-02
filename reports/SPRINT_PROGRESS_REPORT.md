# GradeMind - Agile Sprint Progress Report

## Agile Framework: Scrum
- **Project**: GradeMind (Team 5)
- **Sprint Cadence**: 2-Week Sprints
- **Total Sprints**: 3 Sprints

---

## Sprint 1: Project Foundation & Dataset Formulation
- **Dates**: Weeks 1 - 2
- **Sprint Goal**: Define requirements, design architecture, generate synthetic student dataset, and establish Git repository structure.
- **Key Deliverables**:
  - `docs/CO1_AGILE.md` and `docs/BACKLOG.md` formulated.
  - Synthetic data generation algorithm implemented (`data/students.csv`).
  - Capstone Project Abstract submitted and approved (`docs/TEAM-5_ABSTRACT.pdf`).
- **Velocity**: 24 Story Points (100% completed).

---

## Sprint 2: ML Pipeline & Model Training
- **Dates**: Weeks 3 - 4
- **Sprint Goal**: Develop data validation, train classification models, tune hyperparameters, and evaluate performance.
- **Key Deliverables**:
  - Random Forest Classifier trained with 89.5% accuracy.
  - Serialization pipeline to `results/model.joblib`.
  - Feature importance and evaluation visualizations generated.
  - MLOps experiment tracking configured with MLflow and DVC.
- **Velocity**: 32 Story Points (100% completed).

---

## Sprint 3: Full-Stack Web App, DevSecOps & Containerization
- **Dates**: Weeks 5 - 6
- **Sprint Goal**: Build Flask dashboard, integrate SQLite database, run security scans, and containerize the application.
- **Key Deliverables**:
  - Flask web application with real-time prediction and student analytics dashboard.
  - Security scanning integrated (Bandit & pip-audit).
  - Docker containerization and Kubernetes manifests configured.
  - Prometheus metrics instrumentation (`/metrics`).
- **Velocity**: 38 Story Points (100% completed).

---

## Retrospective & Team Contribution Summary

| Member | Primary Focus |
| :--- | :--- |
| **T. Devi Prasad** | ML algorithm evaluation, Random Forest optimization, classification metrics |
| **B. Sidharth Reddy** | Flask application routing, SQLite database schema and queries |
| **R. Harshit** | UI dashboard design, charts, Jinja2 template styling |
| **D. Vinay Varma** | Docker containerization, Kubernetes configurations, DevSecOps security audits |

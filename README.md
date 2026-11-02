# GradeMind – AI-Based Academic Performance Prediction & Student Analytics

![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Flask%203.0-green.svg)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED.svg)
![Status](https://img.shields.io/badge/Project-Active%20Capstone-success.svg)

---

## 🎓 Academic Capstone Information
- **Institution**: KL Deemed to be University
- **Department**: Department of Computer Science & Engineering (CSE)
- **Course**: Engineering Capstone Project – 1 (`23IE4053R` / `23IE4053A`)
- **Academic Year**: 2026 – 2027
- **Project Title**: **GradeMind – AI-Based Academic Performance Prediction & Student Analytics**
- **Project Guide**: **Dr. J. Kavitha Reddy**

### 👥 Team Members (Team 5)

| S. No. | University ID | Name | Role & Core Contribution | GitHub Profile |
| :---: | :---: | :--- | :--- | :--- |
| 1 | **2420030165** | **T. Devi Prasad** | ML Modeling & Hyperparameter Optimization | [@tadeladeviprasad8-collab](https://github.com/tadeladeviprasad8-collab) |
| 2 | **2420030600** | **B. Sidharth Reddy** | Backend Architecture & Database Integration | [@SIDHARTHREDDY600](https://github.com/SIDHARTHREDDY600) |
| 3 | **2420030271** | **R. Harshit** | Frontend UI/UX & Visual Analytics Dashboard | [@harshit-07r](https://github.com/harshit-07r) |
| 4 | **2420030272** | **D. Vinay Varma** | DevOps CI/CD, Containerization & DevSecOps Auditing | [@Varma2007](https://github.com/Varma2007) |

---

## 🎯 Problem Statement & Motivation
Academic institutions routinely generate large volumes of student data—attendance patterns, continuous assessment marks, homework scores, and study habits. However, these metrics are frequently analyzed retrospectively rather than proactively. 

**GradeMind** addresses this challenge by deploying an end-to-end Machine Learning web platform that forecasts student academic outcomes early in the semester. The system classifies performance into `Pass`, `Merit`, and `Distinction`, equipping faculty mentors with actionable analytics to identify at-risk learners and perform early remedial interventions.

---

## 🏗️ Repository Architecture
The repository strictly adheres to the standard 5-folder project architecture:

```
├── data/                  # Datasets, SQLite database, and data dictionaries
│   ├── students.csv       # 1,000 synthetic student academic records
│   ├── grademind.db       # SQLite database storing prediction logs
│   └── data_dictionary.md # Complete feature metadata and statistical distributions
│
├── docs/                  # Capstone documentation, ethics, and course outcome mappings
│   ├── TEAM-5_ABSTRACT.docx # Formal Capstone Abstract Submission (DOCX)
│   ├── TEAM-5_ABSTRACT.pdf  # Formal Capstone Abstract Submission (PDF)
│   ├── ARCHITECTURE.md    # High-level system architecture and component flow
│   ├── SYLLABUS_MAPPING.md# Comprehensive alignment with Course Outcomes (CO1 - CO4)
│   ├── CO1_AGILE.md       # Agile principles, Scrum methodology, and SDLC
│   ├── CO2_DEVOPS.md      # DevOps pipelines, Git workflows, and Prometheus monitoring
│   ├── CO3_SECURITY.md    # DevSecOps security tools (Bandit, pip-audit, Trivy)
│   ├── BACKLOG.md         # Agile sprint backlog, user stories, and acceptance criteria
│   ├── VIVA.md            # Capstone viva voce preparation and Q&A guide
│   ├── AI_ETHICS.md       # Bias mitigation, fairness metrics, and algorithmic ethics
│   ├── GDPR.md            # Student data privacy and protection guidelines
│   ├── MINIKUBE.md        # Local Kubernetes cluster orchestration instructions
│   ├── MLOPS.md           # MLOps experiment tracking (MLflow) and versioning (DVC)
│   └── OWASP_TOP10.md     # Web security risk mitigations mapped to GradeMind
│
├── reports/               # Formal project and technical evaluation reports
│   ├── CAPSTONE_PHASE1_REPORT.md  # Comprehensive Phase-1 interim project report
│   ├── MODEL_EVALUATION_REPORT.md # Machine learning evaluation, cross-val, & confusion matrix
│   ├── SECURITY_AUDIT_REPORT.md   # SAST (Bandit), SCA (pip-audit), and OWASP Top 10 audit
│   └── SPRINT_PROGRESS_REPORT.md  # Scrum sprint velocity, burndown, and retrospective
│
├── results/               # Serialized models, evaluation metrics, and visualization charts
│   ├── model.joblib       # Serialized Random Forest classifier
│   ├── metrics.json       # Exported accuracy, precision, recall, and F1 scores
│   ├── classification_report.txt  # Class-wise precision, recall, and F1 metrics
│   ├── confusion_matrix.json      # Numerical confusion matrix breakdown
│   ├── sample_predictions.csv     # Test predictions comparing ground truth vs predicted
│   ├── feature_importance.png     # Feature importance ranking visualization
│   ├── confusion_matrix.png       # Test confusion matrix heatmap
│   ├── grade_distribution.png     # Grade category distribution plot
│   └── performance_metrics.png    # Summary performance metrics comparison chart
│
├── src/                   # Production source code, templates, tests, and configuration
│   ├── app.py             # Flask web application entry point
│   ├── train.py           # Model training and validation pipeline
│   ├── predict.py         # Inference module with boundary validation
│   ├── database.py        # SQLite database operations module
│   ├── generate_dataset.py# Synthetic dataset generator script
│   ├── requirements.txt   # Python package dependencies
│   ├── Dockerfile         # Production container definition
│   ├── static/            # Frontend stylesheets
│   │   └── style.css
│   ├── templates/         # Jinja2 web UI templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── predict.html
│   │   ├── result.html
│   │   ├── analytics.html
│   │   ├── students.html
│   │   ├── student_details.html
│   │   └── about.html
│   ├── tests/             # Pytest unit and integration test suite
│   │   ├── test_app.py
│   │   ├── test_database.py
│   │   └── test_predict.py
│   ├── k8s/               # Kubernetes deployment and service manifests
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── monitoring/        # Prometheus metrics scraping configuration
│       └── prometheus.yml
│
└── README.md              # Project documentation and getting started guide
```

---

## 📊 Machine Learning Performance Summary

The predictive model is a **Random Forest Classifier** trained on 800 samples and evaluated on 200 hold-out test samples:

| Metric | Score |
| :--- | :--- |
| **Accuracy** | **89.50%** |
| **Weighted Precision** | **89.90%** |
| **Weighted Recall** | **89.50%** |
| **Weighted F1-Score** | **89.46%** |
| **5-Fold Stratified Cross-Validation** | **86.70% (± 1.8%)** |

### Feature Importance Weights
1. **Internal Marks** (`internal_marks`): ~38.4%
2. **Previous GPA** (`previous_gpa`): ~26.2%
3. **Assignment Score** (`assignment_score`): ~18.1%
4. **Attendance Percentage** (`attendance_pct`): ~11.6%
5. **Study Hours Per Week** (`study_hours_per_week`): ~5.7%

---

## 🚀 Quickstart Guide

### 1. Prerequisites
- Python 3.11 or 3.12
- Git

### 2. Installation
```bash
# Clone the repository
git clone <repository_url>
cd <repository_name>

# Install dependencies
pip install -r src/requirements.txt
```

### 3. Running the Model Training Pipeline
```bash
python src/train.py
```
*Outputs are serialized to `results/model.joblib` and evaluation metrics logged to `results/metrics.json`.*

### 4. Running the Web Application
```bash
python src/app.py
```
*Open your web browser and navigate to `http://localhost:5000`.*

### 5. Running Automated Tests
```bash
pytest src/tests/ -v
```

---

## 🔒 DevSecOps & Security
- **Static Code Analysis (SAST)**: Bandit scan passed with **0 High / 0 Medium** vulnerabilities.
- **Dependency Auditing (SCA)**: pip-audit verified with **0 known CVEs**.
- **OWASP Top 10**: Parameterized SQL queries prevent injection, strict input sanitization bounds numerical inputs.

---

## 📜 Syllabus Alignment (CO1 – CO4)
- **CO1 (SDLC & Agile)**: Full Agile Scrum lifecycle documented in `docs/CO1_AGILE.md` and `docs/BACKLOG.md`.
- **CO2 (DevOps)**: Docker (`src/Dockerfile`), Kubernetes (`src/k8s/`), and Prometheus (`src/monitoring/`).
- **CO3 (DevSecOps & MLOps)**: Security reports in `reports/SECURITY_AUDIT_REPORT.md` and MLOps guide in `docs/MLOPS.md`.
- **CO4 (Cloud Deployment)**: AWS SageMaker deployment blueprints documented in `docs/AWS_SAGEMAKER.md`.

---

## 📄 License & Academic Disclaimer
Developed as part of the **Engineering Capstone Project – 1** at KL Deemed to be University. For educational and academic research purposes only.

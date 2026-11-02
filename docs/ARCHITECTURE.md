# GradeMind System Architecture

## 1. High-Level Architecture Overview
GradeMind is architected as an end-to-end AI-driven academic performance prediction and student analytics platform.

```
+-----------------------------------------------------------------------------------+
|                                 CLIENT LAYER                                      |
|  - Modern Responsive Web UI (HTML5, CSS3, Jinja2 Templates)                       |
|  - Real-Time Grade Prediction Form & Instant Actionable Feedback                  |
|  - Cohort Analytics Dashboard & Student Performance Visualizations                |
+------------------------------------------+----------------------------------------+
                                           | HTTP Requests / JSON APIs
                                           v
+-----------------------------------------------------------------------------------+
|                             APPLICATION LAYER (Flask)                             |
|  - Web Application Server (src/app.py)                                            |
|  - Request Validation & Preprocessing Pipeline (src/predict.py)                   |
|  - Prometheus Observability Metrics Endpoint (/metrics)                          |
+-------------------+---------------------------------------+-----------------------+
                    |                                       |
                    v                                       v
+---------------------------------------+   +---------------------------------------+
|            ML ENGINE LAYER            |   |           DATA STORAGE LAYER          |
|  - Scikit-Learn Random Forest Model   |   |  - Student Dataset (data/students.csv)|
|  - Model Serialization (joblib)       |   |  - SQLite Database (data/grademind.db)|
|  - Offline Training (src/train.py)    |   |  - Experiment Tracking (MLflow)       |
|  - Multi-class: Pass, Merit, Distinct |   |  - Data Version Control (DVC)         |
+---------------------------------------+   +---------------------------------------+
```

## 2. Component Breakdown

### A. Web Application (`src/app.py`)
- Provides clean REST endpoints and server-rendered templates for students and faculty.
- Features: Single prediction, historical student log, cohort analytics, and Prometheus metrics.

### B. Machine Learning Engine (`src/train.py`, `src/predict.py`)
- **Model**: Random Forest Classifier (100 estimators, max depth 10, min samples split 5).
- **Features**: Attendance percentage, Internal marks, Assignment scores, Weekly study hours, Previous GPA.
- **Output**: Multi-class classification into `Pass`, `Merit`, or `Distinction` with class probability confidence scores.

### C. DevOps & Infrastructure (`src/Dockerfile`, `src/k8s/`, `src/monitoring/`)
- Containerized using Docker for multi-platform repeatability.
- Kubernetes deployment and service configurations for container orchestration.
- Prometheus scraping endpoint for real-time latency and prediction monitoring.

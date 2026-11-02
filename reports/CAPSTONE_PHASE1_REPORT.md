# Capstone Project Phase-1 Interim Report

## KL Deemed to be University
### Department of Computer Science & Engineering
**Course**: Engineering Capstone Project – 1 (23IE4053R / 23IE4053A)  
**Academic Year**: 2026 - 2027  
**Project Title**: GradeMind – AI-Based Academic Performance Prediction & Student Analytics  
**Guide**: Dr. J. Kavitha Reddy  

---

### Team Members

| S. No. | University ID | Name | Role & Core Contribution |
| :--- | :--- | :--- | :--- |
| 1 | **2420030165** | T. Devi Prasad | ML Model Engineering & Hyperparameter Optimization |
| 2 | **2420030600** | B. Sidharth Reddy | Backend Web Architecture & Database Integration |
| 3 | **2420030271** | R. Harshit | Frontend UI/UX & Analytics Visualizations |
| 4 | **2420030272** | D. Vinay Varma | DevOps, CI/CD Pipeline & DevSecOps Security Auditing |

---

## 1. Executive Summary & Abstract
Academic institutions routinely gather substantial volumes of academic indicators—including attendance rates, continuous assessment marks, homework scores, and study habits. However, these metrics are frequently examined retrospectively rather than proactively. 

**GradeMind** bridges this gap by deploying an intelligent Machine Learning system that predicts semester outcomes at an early stage. The system categorizes performance into `Pass`, `Merit`, and `Distinction`, while providing educators and academic mentors with an interactive visual dashboard to identify at-risk students and initiate timely pedagogical interventions.

---

## 2. Problem Statement & Motivation
In large higher-education cohorts, faculty mentors lack scalable mechanisms to track student risk profiles in real time. Traditional semester-end evaluations identify learning deficiencies when remedial intervention is no longer feasible. 

GradeMind addresses this by:
1. Synthesizing early-semester performance indicators into actionable risk metrics.
2. Delivering high-precision predictive classification (89.5% test accuracy).
3. Embedding DevSecOps and MLOps best practices directly into the application lifecycle.

---

## 3. Project Objectives
- **Prediction Engine**: Train and serialize an ensemble Random Forest model capable of multi-class academic outcome prediction.
- **Educator Dashboard**: Construct an intuitive web dashboard for viewing student records, distribution analytics, and prediction confidence.
- **DevOps/DevSecOps Pipeline**: Containerize the solution with Docker, configure Kubernetes orchestration, and automate static security audits (Bandit, pip-audit).
- **MLOps Integration**: Version control data through DVC and log experiment iterations via MLflow.

---

## 4. System Implementation & Results
The machine learning pipeline was trained on 1,000 synthetic academic records. Evaluation highlights:
- **Test Accuracy**: 89.5%
- **Weighted Precision**: 89.9%
- **Weighted Recall**: 89.5%
- **Weighted F1-Score**: 89.5%
- **5-Fold Stratified Cross-Validation**: 86.7% (± 1.8%)

### Feature Importance Hierarchy
1. Continuous Internal Assessment Marks (~38.4%)
2. Cumulative Previous GPA (~26.2%)
3. Assignment Completion Score (~18.1%)
4. Lecture Attendance Percentage (~11.6%)
5. Weekly Independent Study Hours (~5.7%)

---

## 5. Course Outcomes (CO) Alignment
- **CO1 (SDLC & Agile)**: User stories, Scrum sprints, backlog grooming documented in `docs/CO1_AGILE.md` and `docs/BACKLOG.md`.
- **CO2 (DevOps)**: Docker containerization, Kubernetes manifests, Prometheus monitoring in `src/`.
- **CO3 (DevSecOps & MLOps)**: Bandit security scans, OWASP Top 10 mitigations, MLflow experiment tracking.
- **CO4 (Cloud Deployment)**: AWS SageMaker deployment blueprints and cloud architecture documented in `docs/AWS_SAGEMAKER.md`.

---

## 6. Conclusion & Next Steps
Phase 1 successfully establishes a functioning end-to-end predictive prototype with verified security compliance and container readiness. Phase 2 will focus on multi-cohort longitudinal tracking, automated SMS/email risk alerts to mentors, and production deployment on cloud infrastructure.

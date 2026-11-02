# MLOps (Machine Learning Operations)

This document outlines the MLOps lifecycle implemented in GradeMind.

## The MLOps Lifecycle
MLOps aims to reliably and efficiently deploy and maintain machine learning models in production.

1. **Data Ingestion & Validation**: Collecting and verifying the quality of the student dataset.
2. **Data Versioning (DVC)**: Tracking changes to the dataset over time, similar to how Git tracks code.
3. **Model Training**: Using Scikit-Learn to train the Random Forest model.
4. **Experiment Tracking (MLflow)**: Logging parameters, metrics (accuracy, F1), and model artifacts to compare different training runs.
5. **Model Versioning**: Saving specific iterations of the trained model (e.g., as `.joblib` files).
6. **Deployment**: Serving the model via a Flask web application inside a Docker container.
7. **Monitoring**: Tracking the application and model performance in production (using Prometheus).
8. **Retraining**: Updating the model when new data becomes available or performance degrades.

## Tools Used

### DVC (Data Version Control)
Git is great for code, but terrible for large datasets or binary model files. We use DVC to version the `data/students.csv` file.
- **Why**: Ensures reproducibility. If a model starts performing poorly, we can use DVC to revert to the exact dataset that trained a previous, successful model.
- **Usage**: `dvc init`, `dvc add data/students.csv`.

### MLflow
MLflow is used for local experiment tracking.
- **Why**: When tuning the Random Forest (e.g., changing `max_depth` or `n_estimators`), MLflow automatically logs the parameters and the resulting accuracy.
- **Usage**: The `src/train.py` script includes MLflow tracking code. Results can be viewed in the local `mlruns/` directory or via the MLflow UI (`mlflow ui`).

## Architecture: Training vs. Prediction History
It is important to distinguish between the **training dataset** and the **application prediction history**:

```text
Training Dataset (data/students.csv)
       ↓
DVC (Versioning)
       ↓
ML Training (src/train.py)
       ↓
MLflow (Tracking)
       ↓
model.joblib (Trained Artifact)
       ↓
Flask Application (app.py)
       ↓
Student Prediction
       ↓
SQLite Prediction History (database/grademind.db)
       ↓
Analytics Dashboard
```
- **CSV Dataset**: Used strictly for training the Random Forest model offline.
- **SQLite Database**: Used at runtime by the web application to store real-time user predictions and calculate dashboard analytics. Mixing these unnecessarily can cause data leaks or performance issues.

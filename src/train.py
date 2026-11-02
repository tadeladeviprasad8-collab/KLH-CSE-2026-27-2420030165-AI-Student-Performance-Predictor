"""
src/train.py - Train the GradeMind ML model
"""

import os
import sys
import json
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix
)

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SRC_DIR, ".."))

DATASET_PATH = os.path.join(BASE_DIR, "data", "students.csv")
MODEL_PATH = os.path.join(BASE_DIR, "results", "model.joblib")

FEATURE_COLUMNS = [
    "attendance_pct",
    "internal_marks",
    "assignment_score",
    "study_hours_per_week",
    "previous_gpa"
]
TARGET_COLUMN = "final_grade_category"
TEST_SIZE = 0.2
RANDOM_STATE = 42


def load_dataset(path=DATASET_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found at: {path}")
    df = pd.read_csv(path)
    print(f"Dataset loaded: {len(df)} records from {path}")
    return df


def validate_dataset(df):
    required_cols = FEATURE_COLUMNS + [TARGET_COLUMN]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")
    
    valid_targets = {"Pass", "Merit", "Distinction"}
    actual_targets = set(df[TARGET_COLUMN].unique())
    if not actual_targets.issubset(valid_targets):
        raise ValueError(f"Unexpected target values: {actual_targets - valid_targets}")
    
    return df


def train_model(df):
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=RANDOM_STATE
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average="weighted")
    rec = recall_score(y_test, y_pred, average="weighted")
    f1 = f1_score(y_test, y_pred, average="weighted")

    print(f"Accuracy:  {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall:    {rec:.4f}")
    print(f"F1-Score:  {f1:.4f}")

    metrics = {
        "accuracy": round(acc, 4),
        "precision": round(prec, 4),
        "recall": round(rec, 4),
        "f1_score": round(f1, 4)
    }
    return model, metrics


def save_model(model, path=MODEL_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)
    print(f"Model saved to: {path}")


def main():
    print("=" * 50)
    print("GradeMind - Model Training Pipeline")
    print("=" * 50)
    df = load_dataset(DATASET_PATH)
    df = validate_dataset(df)
    model, metrics = train_model(df)
    save_model(model, MODEL_PATH)
    print("Training pipeline complete successfully!")


if __name__ == "__main__":
    main()

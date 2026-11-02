"""
src/predict.py - Prediction module for GradeMind
"""

import os
import sys
import joblib
import numpy as np

# Resolve project paths dynamically
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SRC_DIR, ".."))

MODEL_PATH = os.environ.get("MODEL_PATH", os.path.join(BASE_DIR, "results", "model.joblib"))

FEATURE_NAMES = [
    "attendance_pct",
    "internal_marks",
    "assignment_score",
    "study_hours_per_week",
    "previous_gpa"
]


def load_model(model_path=None):
    """Load the trained model from disk."""
    if model_path is None:
        model_path = MODEL_PATH

    if not os.path.exists(model_path):
        # Fallback check
        alt_path = os.path.join(BASE_DIR, "models", "model.joblib")
        if os.path.exists(alt_path):
            model_path = alt_path
        else:
            raise FileNotFoundError(
                f"Model not found at '{model_path}'. "
                "Please run 'python src/train.py' first to train the model."
            )

    model = joblib.load(model_path)
    return model


def validate_input(attendance_pct, internal_marks, assignment_score,
                   study_hours_per_week, previous_gpa):
    """Validate that all input values are within acceptable ranges."""
    errors = []

    if not (0 <= attendance_pct <= 100):
        errors.append("Attendance must be between 0 and 100")

    if not (0 <= internal_marks <= 100):
        errors.append("Internal marks must be between 0 and 100")

    if not (0 <= assignment_score <= 100):
        errors.append("Assignment score must be between 0 and 100")

    if not (0 <= study_hours_per_week <= 50):
        errors.append("Study hours must be between 0 and 50")

    if not (0 <= previous_gpa <= 10):
        errors.append("Previous GPA must be between 0 and 10")

    if errors:
        raise ValueError("; ".join(errors))

    return {
        "attendance_pct": float(attendance_pct),
        "internal_marks": float(internal_marks),
        "assignment_score": float(assignment_score),
        "study_hours_per_week": float(study_hours_per_week),
        "previous_gpa": float(previous_gpa)
    }


def predict_grade(attendance_pct, internal_marks, assignment_score,
                  study_hours_per_week, previous_gpa, model_path=None):
    """Predict the student's grade category and return confidence scores."""
    validated = validate_input(
        attendance_pct, internal_marks, assignment_score,
        study_hours_per_week, previous_gpa
    )

    model = load_model(model_path)

    features_array = np.array([[
        validated["attendance_pct"],
        validated["internal_marks"],
        validated["assignment_score"],
        validated["study_hours_per_week"],
        validated["previous_gpa"]
    ]])

    predicted_grade = model.predict(features_array)[0]

    probabilities = {}
    confidence = None
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(features_array)[0]
        classes = model.classes_
        for cls, prob in zip(classes, probs):
            probabilities[cls] = round(float(prob) * 100, 1)
        confidence = probabilities[predicted_grade]

    return {
        "predicted_grade": predicted_grade,
        "confidence": confidence,
        "probabilities": probabilities,
        "inputs": validated
    }

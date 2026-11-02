import pytest
import os
import sys

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SRC_DIR, "..", ".."))
if os.path.join(BASE_DIR, "src") not in sys.path:
    sys.path.insert(0, os.path.join(BASE_DIR, "src"))

from predict import predict_grade, validate_input, load_model

def test_model_file_exists():
    path = os.path.join(BASE_DIR, "results", "model.joblib")
    assert os.path.exists(path), "Model file not found in results/"

def test_model_loads():
    path = os.path.join(BASE_DIR, "results", "model.joblib")
    model = load_model(path)
    assert model is not None

def test_prediction_returns_valid_category():
    res = predict_grade(85.0, 80.0, 85.0, 15.0, 8.5)
    assert res["predicted_grade"] in ["Pass", "Merit", "Distinction"]

def test_validation_rejects_out_of_bounds():
    with pytest.raises(ValueError):
        validate_input(150.0, 50.0, 50.0, 10.0, 8.0)

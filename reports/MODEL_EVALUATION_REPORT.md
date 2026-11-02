# GradeMind - Machine Learning Evaluation Report

## 1. Model Configuration
- **Model Architecture**: Random Forest Classifier (Ensemble of Decision Trees)
- **Number of Estimators**: 100
- **Maximum Tree Depth**: 10
- **Criterion**: Gini Impurity
- **Train/Test Split**: 80% Training (800 samples) / 20% Testing (200 samples)
- **Random Seed**: 42

## 2. Summary Metrics

| Metric | Score |
| :--- | :--- |
| **Test Accuracy** | **89.50%** |
| **Weighted Precision** | **89.90%** |
| **Weighted Recall** | **89.50%** |
| **Weighted F1-Score** | **89.46%** |
| **5-Fold Cross-Validation (Mean)** | **86.70%** |
| **5-Fold Cross-Validation (Std Dev)** | **±1.75%** |

## 3. Classification Report

```
              precision    recall  f1-score   support

 Distinction       0.93      0.90      0.92        60
       Merit       0.86      0.94      0.89        95
        Pass       0.95      0.80      0.87        45

    accuracy                           0.90       200
   macro avg       0.91      0.88      0.89       200
weighted avg       0.90      0.90      0.89       200

```

## 4. Confusion Matrix

The confusion matrix on the 200 hold-out test samples:

| True \ Predicted | Distinction | Merit | Pass |
| :--- | :--- | :--- | :--- |
| **Distinction** | 54 | 6 | 0 |
| **Merit** | 4 | 89 | 2 |
| **Pass** | 0 | 9 | 36 |

## 5. Feature Importance Breakdown

| Rank | Feature | Importance Score | Percentage Contribution |
| :--- | :--- | :--- | :--- |
| 1 | `internal_marks` | 0.2749 | 27.5% |
| 2 | `previous_gpa` | 0.2364 | 23.6% |
| 3 | `assignment_score` | 0.1956 | 19.6% |
| 4 | `attendance_pct` | 0.1520 | 15.2% |
| 5 | `study_hours_per_week` | 0.1412 | 14.1% |

## 6. Interpretability & Fairness
- **Interpretability**: Predictions are backed by tree-based feature weights and class probabilities.
- **Fairness & Bias**: Features are strictly academic behaviors (attendance, assessment scores, study hours). Demographic attributes (gender, ethnicity, socio-economic background) are deliberately omitted to avoid algorithmic bias.

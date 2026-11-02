"""
generate_dataset.py - Generates synthetic student data for GradeMind

This script creates ~1000 realistic student records with academic features
and a logically consistent final_grade_category (Pass/Merit/Distinction).

Usage:
    python generate_dataset.py
"""

import pandas as pd
import numpy as np
import os

def generate_dataset(num_students=1000, output_path="data/students.csv"):
    """
    Generate synthetic student academic data.
    
    The data is designed to be logically realistic:
    - Higher attendance, marks, study hours, and GPA → better grades
    - Some randomness is added to simulate real-world variation
    """
    np.random.seed(42)  # For reproducibility
    
    # --- Generate base features ---
    # A "talent" factor that loosely ties all features together
    talent = np.random.normal(0.5, 0.2, num_students).clip(0.1, 0.95)
    
    # Attendance: 40% to 100%
    attendance_pct = (talent * 60 + 40 + np.random.normal(0, 8, num_students)).clip(40, 100).round(1)
    
    # Internal Marks: 20 to 100
    internal_marks = (talent * 80 + 20 + np.random.normal(0, 10, num_students)).clip(20, 100).round(0).astype(int)
    
    # Assignment Score: 20 to 100
    assignment_score = (talent * 75 + 25 + np.random.normal(0, 10, num_students)).clip(20, 100).round(0).astype(int)
    
    # Study Hours Per Week: 2 to 30
    study_hours_per_week = (talent * 25 + 2 + np.random.normal(0, 4, num_students)).clip(2, 30).round(1)
    
    # Previous GPA: 3.0 to 10.0
    previous_gpa = (talent * 7 + 3 + np.random.normal(0, 0.8, num_students)).clip(3.0, 10.0).round(1)
    
    # --- Calculate a composite score to determine grade category ---
    # Weighted composite of all features (normalized to 0-100 scale)
    composite_score = (
        (attendance_pct / 100) * 20 +          # 20% weight
        (internal_marks / 100) * 25 +           # 25% weight
        (assignment_score / 100) * 20 +         # 20% weight
        (study_hours_per_week / 30) * 15 +      # 15% weight
        (previous_gpa / 10) * 20                # 20% weight
    )
    
    # Add a small random factor to avoid perfectly deterministic labels
    composite_score += np.random.normal(0, 3, num_students)
    
    # --- Assign grade categories based on composite score ---
    final_grade_category = []
    for score in composite_score:
        if score >= 70:
            final_grade_category.append("Distinction")
        elif score >= 50:
            final_grade_category.append("Merit")
        else:
            final_grade_category.append("Pass")
    
    # --- Build DataFrame ---
    df = pd.DataFrame({
        "student_id": [f"STU{str(i+1).zfill(4)}" for i in range(num_students)],
        "attendance_pct": attendance_pct,
        "internal_marks": internal_marks,
        "assignment_score": assignment_score,
        "study_hours_per_week": study_hours_per_week,
        "previous_gpa": previous_gpa,
        "final_grade_category": final_grade_category
    })
    
    # --- Save to CSV ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
    # --- Print summary ---
    print(f"Dataset generated: {output_path}")
    print(f"Total students: {len(df)}")
    print(f"\nGrade distribution:")
    print(df["final_grade_category"].value_counts())
    print(f"\nFeature summary:")
    print(df.describe().round(2))
    
    return df


if __name__ == "__main__":
    generate_dataset()

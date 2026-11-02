# GradeMind Dataset Dictionary

## Overview
The GradeMind dataset contains 1,000 synthetic student academic performance records designed to simulate real-world university assessment patterns for early risk identification and grade prediction.

## Feature Descriptions

| Field Name | Type | Range | Description |
| :--- | :--- | :--- | :--- |
| `student_id` | String | STU0001 - STU1000 | Unique anonymized student identifier |
| `attendance_pct` | Float | 40.0% - 100.0% | Percentage of lectures attended during the semester |
| `internal_marks` | Integer | 20 - 100 | Marks secured in continuous internal assessments (out of 100) |
| `assignment_score` | Integer | 20 - 100 | Average score achieved across lab and homework assignments |
| `study_hours_per_week` | Float | 2.0 - 30.0 | Self-reported weekly independent study hours |
| `previous_gpa` | Float | 3.0 - 10.0 | Cumulative Grade Point Average from previous semesters |
| `final_grade_category` | Categorical | Pass, Merit, Distinction | Final outcome target category |

## Statistical Summary

| Feature | Min | Mean | Max | Std Dev |
| :--- | :--- | :--- | :--- | :--- |
| `attendance_pct` | 40.0 | 73.1 | 100.0 | 14.8 |
| `internal_marks` | 20.0 | 63.8 | 100.0 | 18.2 |
| `assignment_score` | 20.0 | 66.2 | 100.0 | 17.5 |
| `study_hours_per_week` | 2.0 | 15.6 | 30.0 | 6.5 |
| `previous_gpa` | 3.0 | 6.9 | 10.0 | 1.6 |

## Class Distribution

| Target Grade Category | Count | Percentage |
| :--- | :--- | :--- |
| `Pass` | 468 | 46.8% |
| `Merit` | 382 | 38.2% |
| `Distinction` | 150 | 15.0% |
| **Total** | **1,000** | **100.0%** |

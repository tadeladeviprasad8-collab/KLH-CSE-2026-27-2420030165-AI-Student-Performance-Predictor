"""
src/app.py - Main Flask application for GradeMind
"""

import os
import sys
from flask import Flask, render_template, request, flash, redirect, url_for, Response
from dotenv import load_dotenv

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SRC_DIR, ".."))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from predict import predict_grade, load_model
from database import init_db, add_student, get_all_students, get_student_by_id, search_students, delete_student

try:
    from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
    PROMETHEUS_AVAILABLE = True
except ImportError:
    PROMETHEUS_AVAILABLE = False

load_dotenv()

template_dir = os.path.join(SRC_DIR, "templates")
static_dir = os.path.join(SRC_DIR, "static")
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key-change-in-production")

if PROMETHEUS_AVAILABLE:
    PREDICTION_COUNTER = Counter("grademind_predictions_total", "Total predictions", ["predicted_grade"])
    PREDICTION_LATENCY = Histogram("grademind_prediction_latency_seconds", "Latency")

    @app.route("/metrics")
    def metrics():
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


def get_analytics():
    students = get_all_students()
    total = len(students)
    if total == 0:
        return None

    pass_count = sum(1 for s in students if s['predicted_grade'] == 'Pass')
    merit_count = sum(1 for s in students if s['predicted_grade'] == 'Merit')
    distinction_count = sum(1 for s in students if s['predicted_grade'] == 'Distinction')

    avg_attendance = sum(s['attendance_pct'] for s in students) / total
    avg_internal_marks = sum(s['internal_marks'] for s in students) / total
    avg_assignment_score = sum(s['assignment_score'] for s in students) / total
    avg_study_hours = sum(s['study_hours_per_week'] for s in students) / total
    avg_gpa = sum(s['previous_gpa'] for s in students) / total

    return {
        "total_students": total,
        "pass_count": pass_count,
        "merit_count": merit_count,
        "distinction_count": distinction_count,
        "avg_attendance": round(avg_attendance, 1),
        "avg_internal_marks": round(avg_internal_marks, 1),
        "avg_assignment_score": round(avg_assignment_score, 1),
        "avg_study_hours": round(avg_study_hours, 1),
        "avg_gpa": round(avg_gpa, 1),
        "pass_pct": round(pass_count / total * 100, 1),
        "merit_pct": round(merit_count / total * 100, 1),
        "distinction_pct": round(distinction_count / total * 100, 1),
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            student_id = request.form.get("student_id", "").strip()
            student_name = request.form.get("student_name", "").strip()

            if not student_id:
                student_id = f"STU{np.random.randint(1000, 9999)}"
            if not student_name:
                student_name = "Anonymous Student"

            attendance_pct = float(request.form["attendance_pct"])
            internal_marks = float(request.form["internal_marks"])
            assignment_score = float(request.form["assignment_score"])
            study_hours = float(request.form["study_hours_per_week"])
            previous_gpa = float(request.form["previous_gpa"])

            result = predict_grade(
                attendance_pct=attendance_pct,
                internal_marks=internal_marks,
                assignment_score=assignment_score,
                study_hours_per_week=study_hours,
                previous_gpa=previous_gpa
            )

            add_student(
                student_id=student_id,
                student_name=student_name,
                attendance_pct=attendance_pct,
                internal_marks=internal_marks,
                assignment_score=assignment_score,
                study_hours_per_week=study_hours,
                previous_gpa=previous_gpa,
                predicted_grade=result["predicted_grade"]
            )

            if PROMETHEUS_AVAILABLE:
                PREDICTION_COUNTER.labels(predicted_grade=result["predicted_grade"]).inc()

            return render_template(
                "result.html",
                result=result,
                student_id=student_id,
                student_name=student_name
            )
        except Exception as e:
            flash(f"Error making prediction: {str(e)}", "danger")
            return redirect(url_for("predict"))

    return render_template("predict.html")


@app.route("/analytics")
def analytics():
    data = get_analytics()
    return render_template("analytics.html", analytics=data)


@app.route("/students")
def students():
    query = request.args.get("search", "").strip()
    if query:
        student_list = search_students(query)
    else:
        student_list = get_all_students()
    return render_template("students.html", students=student_list, search_query=query)


@app.route("/students/<int:student_id>")
def student_detail(student_id):
    student = get_student_by_id(student_id)
    if not student:
        flash("Student record not found", "warning")
        return redirect(url_for("students"))
    return render_template("student_details.html", student=student)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/health")
def health():
    return {"status": "healthy", "service": "GradeMind"}


if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    print(f"Starting GradeMind on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=debug)

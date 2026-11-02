"""
src/database.py - Database operations for GradeMind
"""

import sqlite3
import os
from datetime import datetime

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SRC_DIR, ".."))

DB_DIR = os.environ.get("DB_DIR", os.path.join(BASE_DIR, "data"))
DB_PATH = os.environ.get("DB_PATH", os.path.join(DB_DIR, "grademind.db"))


def get_db_connection():
    """Create and return a database connection."""
    if not os.path.exists(os.path.dirname(DB_PATH)):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize the database and create the students table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            student_name TEXT NOT NULL,
            attendance_pct REAL NOT NULL,
            internal_marks REAL NOT NULL,
            assignment_score REAL NOT NULL,
            study_hours_per_week REAL NOT NULL,
            previous_gpa REAL NOT NULL,
            predicted_grade TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def add_student(student_id, student_name, attendance_pct, internal_marks,
                assignment_score, study_hours_per_week, previous_gpa, predicted_grade):
    """Add a new student prediction record to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
        INSERT INTO students (
            student_id, student_name, attendance_pct, internal_marks,
            assignment_score, study_hours_per_week, previous_gpa,
            predicted_grade, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        student_id, student_name, attendance_pct, internal_marks,
        assignment_score, study_hours_per_week, previous_gpa,
        predicted_grade, created_at
    ))

    conn.commit()
    student_record_id = cursor.lastrowid
    conn.close()
    return student_record_id


def get_all_students():
    """Retrieve all students from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students ORDER BY id DESC')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_student_by_id(db_id):
    """Retrieve a single student record by its database primary key."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE id = ?', (db_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


def search_students(query):
    """Search students by student_id or student_name."""
    conn = get_db_connection()
    cursor = conn.cursor()
    search_term = f"%{query}%"
    cursor.execute('''
        SELECT * FROM students 
        WHERE student_id LIKE ? OR student_name LIKE ?
        ORDER BY id DESC
    ''', (search_term, search_term))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def delete_student(db_id):
    """Delete a student record by ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (db_id,))
    conn.commit()
    conn.close()

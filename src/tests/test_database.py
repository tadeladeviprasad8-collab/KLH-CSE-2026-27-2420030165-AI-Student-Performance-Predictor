import pytest
import os
import sys
import tempfile

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SRC_DIR, "..", ".."))
if os.path.join(BASE_DIR, "src") not in sys.path:
    sys.path.insert(0, os.path.join(BASE_DIR, "src"))

import database as db_module
from database import init_db, add_student, get_all_students, get_student_by_id

fd, TEST_DB_PATH = tempfile.mkstemp(suffix=".db")
os.close(fd)

@pytest.fixture(autouse=True)
def mock_db_path(monkeypatch):
    monkeypatch.setattr(db_module, "DB_PATH", TEST_DB_PATH)
    init_db()
    yield

def test_init_db_creates_table():
    assert os.path.exists(TEST_DB_PATH)

def test_add_and_retrieve_student():
    db_id = add_student("STU999", "Test User", 80.0, 75.0, 80.0, 12.0, 7.8, "Merit")
    student = get_student_by_id(db_id)
    assert student is not None
    assert student["student_id"] == "STU999"

import pytest
import os
import sys
import tempfile

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SRC_DIR, "..", ".."))
if os.path.join(BASE_DIR, "src") not in sys.path:
    sys.path.insert(0, os.path.join(BASE_DIR, "src"))

from app import app
import database as db_module

fd, TEST_DB_PATH = tempfile.mkstemp(suffix=".db")
os.close(fd)

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(db_module, "DB_PATH", TEST_DB_PATH)
    db_module.init_db()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_home_page(client):
    rv = client.get("/")
    assert rv.status_code == 200

def test_about_page(client):
    rv = client.get("/about")
    assert rv.status_code == 200

def test_health_check(client):
    rv = client.get("/health")
    assert rv.status_code == 200
    assert rv.json["status"] == "healthy"

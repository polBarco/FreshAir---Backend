import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.comments_database import Base, get_db
from main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_user_comments.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override get_db to use the testing database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)

def test_create_comment(client):
    response = client.post("/comment", json={"id": 1, "name": "Test User", "content": "Test Content"})
    #assert response.status_code == 200
    assert response.json()["name"] == "Test User"
    assert response.json()["content"] == "Test Content"

def test_get_comment(client):
    response = client.get("/comment/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"
    assert response.json()["content"] == "Test Content"

def test_get_comments(client):
    response = client.get("/comments")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_update_comment(client):
    response = client.put("/update/1", params={"content": "Updated Content"})
    assert response.status_code == 200
    assert response.json()["content"] == "Updated Content"

def test_update_comment_name(client):
    response = client.put("/updatename/1", params={"name": "Updated User"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"

def test_delete_comment(client):
    response = client.delete("/delete/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Updated User"
    assert response.json()["content"] == "Updated Content"

    response = client.get("/comment/1")
    assert response.status_code == 404

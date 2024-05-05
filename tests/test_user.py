import pytest
from fastapi.testclient import TestClient
from main import app  # replace with the path to your FastAPI application

@pytest.fixture
def client():
    return TestClient(app)

def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user(client):
    test_user_data = {"name": "Test User", "email": "test@example.com"}  # replace with your user data structure
    response = client.post("/users/", json=test_user_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"
    assert response.json()["email"] == "test@example.com"

# Add more tests for other user-related endpoints
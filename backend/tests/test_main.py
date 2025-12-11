import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calculate():
  response = client.get("/arithmetic/+", params={'num1': 1, 'num2': 2})
  assert response.status_code == 200
  assert response.json()['result'] == 3

def test_validate_input():
  response = client.post("/input", json={'input': '+ 1 2'})
  assert response.status_code == 200
  assert response.json()['valid'] == True

def test_get_data():
  response = client.get("/arithmetic/+", params={'num1': 1, 'num2': 2})
  response = client.get("/data")
  assert response.status_code == 200
  assert len(response.json()['data']) == 1
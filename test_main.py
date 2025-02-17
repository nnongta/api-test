from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_plus():
    response = client.get("/plus/5/6")
    assert response.status_code == 200
    assert response.json() == {"result": 11}

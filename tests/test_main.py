from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to SafeNest Security API!"}

def test_send_alert():
    payload = {
        "device_id": "cam_entrance_01",
        "location": "Main Gate",
        "event": "glass break",
        "timestamp": "2025-06-08T14:30:00Z"
    }

    response = client.post("/api/v1/alerts/send-alert", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert "threat_level" in json_data
    assert json_data["device_id"] == payload["device_id"]
    assert json_data["status"] == "Alert processed"

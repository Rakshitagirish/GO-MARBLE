from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_reviews():
    response = client.get("/api/reviews?page=https://example.com")
    assert response.status_code == 200
    assert "reviews_count" in response.json()

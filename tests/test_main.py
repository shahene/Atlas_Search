from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_search_endpoint_returns_structured_response():
    response = client.get("/search", params={"query": "payments"})
    assert response.status_code == 200

    payload = response.json()

    assert payload["query"] == "payments"
    assert payload["count"] == len(payload["results"])
    assert payload["count"] > 0
    assert payload["results"][0]["title"] == "Stripe"

def test_search_endpoint_returns_empty_results_for_no_match():
    response = client.get("/search", params={"query": "quantum"})
    assert response.status_code == 200
    assert response.json()["count"] == 0
    assert response.json()["results"] == []


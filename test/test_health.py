def test_health_check_pass(test_client):
    response = test_client.get("/health/")

    assert response.status_code == 200
    assert response.json().get("status") == "healthy"


def test_health_check_redirects(test_client):
    response = test_client.get("/health")

    assert isinstance(response.history, list)
    assert len(response.history) == 1
    assert response.history[0].status_code == 307

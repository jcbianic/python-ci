def test_app_start(test_client):
    response = test_client.get("/ping")
    assert response.status_code == 200
    assert response.data == b"pong"

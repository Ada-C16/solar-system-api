def test_handle_planets_returns_200_and_empty_array(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {}
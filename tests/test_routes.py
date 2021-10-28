def test_get_all_planets_returns_empty_list_when_db_is_empty(client):
    # Act
    response = client.get("/planets")

    # Assert
    assert response.status_code == 200
    assert response.get_json() == []
def test_get_all_planets_returns_empty_list_when_db_is_empty(client):
    # Act
    response = client.get("/planets")

    # Assert
    assert response.status_code == 200
    assert response.get_json() == []


def test_get_one_planet_by_id_returns_correct_planet(client, one_saved_planet):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "name": "earth",
        "description": "blue marble",
        "moons": 1,
        "id": 1
    }


def test_get_one_planet_by_id_with_empty_db_returns_404(client):
    response = client.get("/planets/1")
    assert response.status_code == 404

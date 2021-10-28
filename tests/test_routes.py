from app.models.planet import Planet

def test_get_planets_returns_200_empty_array_when_db_is_empty(client):
    # act
    response = client.get("/planets")

    # assert
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_single_planet_returns_one_saved_planet(client, one_planet):
    # act
    response = client.get("/planets/1")

    # assert
    assert response.status_code == 200
    assert response.get_json() == {
            "id": 1,
            "name": "Jupiter",
            "description": "A planet in the Milky Way",
            "size_rank": 1
        }

def test_get_single_planet_with_empty_db_returns_404(client):
    # act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # assert
    assert response.status_code == 404
    assert response.get_json() == None


def test_get_planets_with_valid_data_returns_correct_array(client, multiple_planets):
    # act
    response = client.get("/planets")

    # assert
    assert response.status_code == 200
    assert response.get_json() == [
        {
            "id": 1,
            "name": "Jupiter",
            "description": "A planet in the Milky Way",
            "size_rank": 1
        },
        {
            "id": 2,
            "name": "Saturn",
            "description": "A planet in the Milky Way",
            "size_rank": 2
        }
    ]

def test_post_planet_with_JSON_request_body_returns_201(client):
    # Act
    response = client.post("/planets", json={
        "name": "Jupiter",
        "description": "A planet in the Milky Way",
        "size_rank": 1
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "planet": {
            "id": 1,
            "name": "Jupiter",
            "description": "A planet in the Milky Way",
            "size_rank": 1
        }
    }
    new_planet = Planet.query.get(1)
    assert new_planet
    assert new_planet.id == 1
    assert new_planet.name == "Jupiter"
    assert new_planet.description == "A planet in the Milky Way"
    assert new_planet.size_rank == 1
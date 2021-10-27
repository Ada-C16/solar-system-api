def test_get_list_of_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_response_body_of_fixture_planet(client, two_saved_planets):
    #Act 
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response_body == {
        "id": 1,
        "name": "Mars", 
        "description": "Red planet"
    }

def test_get_response_body_of_planet_with_no_data(client):
    # Act
    response = client.get("/planets/1")

    # Assert
    assert response.status_code == 404

def test_get_list_of_planets_in_test_db(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
        "id": 1,
        "name": "Mars", 
        "description": "Red planet"
        },
        {
        "id": 2,
        "name": "Saturn", 
        "description": "Lots of rings!"
        }
    ]

def test_post_new_planet_returns_status_code(client):
    # Act
    request = client.post("/planets", json = {"name": "Venus", "description": "Test"})

    # Assert
    assert request.status_code == 201
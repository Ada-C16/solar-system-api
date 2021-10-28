def test_get_planets(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_one_record(client, one_planet):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert len(response_body) == 4
    assert response_body == {
        "name" : "Mercury", 
        "description" : "Closest to the sun, hot.", 
        "has moons" : False,
        "id" : 1
    }

def test_get_all_planets_with_one_record_returns_404(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 404

def test_get_all_planets_returns_array(client, two_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body == [{
        "name" : "Mercury", 
        "description" : "Closest to the sun, hot.", 
        "has moons" : False,
        "id" : 1
    }, {
        "name" : "Venus", 
        "description" : "Spins the opposite direction of other planets.", 
        "has moons" : False,
        "id" : 2
    }]

def test_post_all_planets_returns_201(client):
    # Act
    response = client.post("/planets", json = {"name": "Venus", "description": "Spins the opposite direction of other planets", "has_moons": 0})
    response_body = response.get_json()

    #Assert
    assert response.status_code == 201
from app.models.planet import Planet


def test_get_all_planets_returns_empty_list_when_db_is_empty(client):
    #act
    response = client.get("/planets")

    #assert
    assert response.status_code == 200
    assert response.get_json() == []


def test_get_one_planet_retuns_one_planet(client, one_planet):
    response = client.get("/planets/1")
    response_body = response.get_json()

    #assert

    assert response.status_code == 200
    # assert "planet" in response_body
    assert response_body == {
            "color": "light brown",
            "description": "in betwen Mars and Saturn",
            "distance": "5",
            "id": 1,
            "name": "Jupiter"
        
    }
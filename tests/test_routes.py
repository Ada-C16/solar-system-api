from app.models.planet import Planet
import json

def test_get_all_planets_database_empty(client):
    response = client.get('/planets')
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == ['There are no planets yet! :O', 200]


def test_get_one_planet(client, add_planet):
    response = client.get('/planets/1')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "description": "way out there",
        "name": "pluto",
        "sign": "Scorpio"}

def test_get_one_planet_no_data_no_fixture_returns_404(client):
    response = client.get('/planets/1')
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == "Planet with ID 1 not found."

def test_get_all_planets_returns_200(client, add_three_planets):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body == [
        {
            "name": "pluto",
            "id": 1,
            "description": "way out there",
            "sign": "Scorpio"
        },
        {
            "name": "mercury",
            "id": 2,
            "description": "messenger closest to sign",
            "sign": "Virgo"
        },
        {
            "name": "saturn",
            "id": 3,
            "description": "forever hula hooping",
            "sign": "Capricorn"
        }
    ]

def test_create_planet_return_201(client, add_planet):
    planet_data = {
        "name":"bluto", 
        "description":"who knows",
        "sign":"Taurus"
    }
    response = client.post('/planets', data=json.dumps(planet_data), content_type='application/json')

    assert response.status_code == 201

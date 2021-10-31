def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"id": 1, "name": "Neptune", "description": "no surface"}

def test_get_one_planet_with_empty_db_returns_404(client):
    response = client.get("/planets/1")
    assert response.status_code == 404

def test_get_all_planets_returns_list_of_planets(client, two_saved_planets):
    response = client.get("/planets")
    assert response.status_code == 200
    assert response.get_json() == [ 
        {
        "name": "Neptune",
        "description": "no surface",
        "id": 1
        },
        {
        "name": "Mars",
        "description": "elon",
        "id": 2
        }
    ] 

def test_create_planet_returns_201(client):
    request_body = {
        "name": "Earth",
        "description": "Us"
    }
    response = client.post("/planets", json=request_body)

    assert response.status_code == 201 
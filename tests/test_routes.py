from app.models.planet import Planet

def test_get_all_planets_when_none_exist(client):
    response = client.get("/planets")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_planet_1_when_none_exist(client):
    response = client.get("/planets/1")

    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == "Error: Planet 1 not found"

def test_get_all_planets_when_some_exist(client, two_saved_planets):
    planet1 = dict(id=1, name="Planet 1", description="I'm planet 1", type="gas giant")
    planet2 = dict(id=2, name="Planet 2", description="I'm planet 2", type="gas giant")

    response = client.get("/planets")

    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert planet1 in response_body
    assert planet2 in response_body

def test_create_a_planet_when_none_exist(client):
    response = client.post("/planets", json=({"name":"Planet 1", "description":"I'm planet 1", "type":"gas giant"}))
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet with id:1 successfully created"
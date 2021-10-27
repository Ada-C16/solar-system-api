import json


def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_two_planets_returns_two_planets(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "Earth",
        "description": "Blue green marble",
        "distance": "Right here"
    }


def test_get_planet_returns_expected_planet(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Earth",
        "description": "Blue green marble",
        "distance": "Right here"
    }


def test_returns_new_planet(client, two_saved_planets):
    data = {
        "name": "Earth",
        "description": "Blue green marble",
        "distance": "Right here"
    }
    response = client.post("/planets", data=json.dumps(data),
                           headers={"Content-Type": "application/json"})

    assert response.status_code == 201


def test_get_planet_returns_404(client):
    response = client.get("/planets/1")

    assert response.status_code == 404
from flask import jsonify
from flask.helpers import make_response

def test_get_all_planets_but_records_empty(client):
    response = client.get("/planet")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_one_planet(client, two_planets_populated):
    response = client.get("/planet/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "mercury",
        "description": "Smol orbit"
    }
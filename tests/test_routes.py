# Act Arrage

import json

from flask.globals import request

def test_route_gets_planets_in_database_returns_empty_list(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_route_returns_all_available_planets_returns_all_planets(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id" : 1,
        "name" :"Earth",
        "description" : "blue and green",
        "oxygen_level" : "21%"
    },  {
        "id" : 2,
        "name" : "Saturn",
        "description" : "a ball of gas",
        "oxygen_level" : "little to none"}
        ]

def test_route_gets_planet_by_id_returns_planet_with_matching_id(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "name" :"Earth",
        "description" : "blue and green",
        "oxygen_level" : "21%"
    }

def test_route_returns_404_for_unavailable_planet_id(client, two_saved_planets):
    response = client.get("/planets/3")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == None

def test_route_returns_404_for_no_book_in_dabatase(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == None

def test_route_gets_planet_by_name_returns_planet_with_matching_name(client, two_saved_planets): #figure out testing with search for name
    response = client.get("/planets?name=Earth")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id" : 1,
        "name" :"Earth",
        "description" : "blue and green",
        "oxygen_level" : "21%"
    }]

def test_route_posts_data_to_database(client):
    data = {
        "id" : 1,
        "name" :"Earth",
        "description" : "blue and green",
        "oxygen_level" : "21%"
    }

    response = client.post("/planets", json = data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == None
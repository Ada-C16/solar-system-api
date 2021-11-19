
from flask import json
from flask.globals import request
from flask.wrappers import Response


def test_get_all_planets_with_no_records(client):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response.status_code ==200
    assert response_body == []

def test_get_planet_by_id(client,two_saved_planets):
    response = client.get('/planets/1')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
    "id":1,
    "name": "Jupiter", 
    "diameter":"Diameter: 86,881 miles (139,822 km)", 
    "moons": True, 
    "picture":"https://cdn.mos.cms.futurecdn.net/WyxFYsiUAQAgU4peSSoBNZ-970-80.png"
}

def test_get_by_id_without_data(client):
    response = client.get('/planets/1')
    response_body = response.get_json()

    assert response.status_code == 404

def test_get_all_planets_with_data(client,two_saved_planets):
    response = client.get('/planets')
    response_body = response.get_json()
    saturn =  {
    "id":2,
    "name": "Saturn", 
    "diameter":"Diameter: 74,900 miles (120,500 km)", 
    "moons": True, 
    "picture":"https://cdn.mos.cms.futurecdn.net/bDVqRSjnbY9jMyVPmStUBY-970-80.png"
}
    jupiter = {
    "id":1,
    "name": "Jupiter", 
    "diameter":"Diameter: 86,881 miles (139,822 km)", 
    "moons": True, 
    "picture":"https://cdn.mos.cms.futurecdn.net/WyxFYsiUAQAgU4peSSoBNZ-970-80.png"
}
    assert response.status_code ==200
    assert saturn in response_body
    assert jupiter in response_body

def test_post_one_planet(client):
    response = client.post('/planets',json= {"id":1,
    "name": "Jupiter", 
    "diameter":"Diameter: 86,881 miles (139,822 km)", 
    "moons": True, 
    "picture":"https://cdn.mos.cms.futurecdn.net/WyxFYsiUAQAgU4peSSoBNZ-970-80.png"}
)
    response_body = response.get_json()

    assert response.status_code ==201
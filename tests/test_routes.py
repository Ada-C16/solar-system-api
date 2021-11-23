# Act Arrage

import json

from flask.globals import request

def test_route_gets_planets_in_database_returns_empty_list(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []
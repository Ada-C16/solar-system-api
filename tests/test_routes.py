import pytest

def test_get_all_planets_returns_200(client):
    response = client.get('/planets')
    response_body = response.get_json()
    
    assert response.status_code == 200
    # assert response_body == []
    assert response_body == ['There are no planets yet! :O', 200]
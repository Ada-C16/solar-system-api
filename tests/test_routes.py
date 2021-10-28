def test_get_all_planets_with_no_records(client):
    #Act
    response=client.get("/planets")
    response_body=response.get_json()

    #Assert
    assert response.status_code==200
    assert response_body==[]

def test_get_one_planet_two_planets_db(client, two_planets):
    #Act
    response=client.get("/planets/1")
    response_body=response.get_json()

    #Assert
    assert response.status_code==200
    assert response_body=={"name":"Pluto", "description":"The unlucky one", "biggest_moon":"", "id":1}

def test_get_one_planet_with_no_records(client):
    #Act
    response=client.get("/planets/1")
    response_body=response.get_json()

    #Assert
    assert response.status_code==404
    assert response_body== None

def test_get_all_planets_two_planets_db(client, two_planets):
    #Act
    response=client.get("/planets")
    response_body=response.get_json()

    #Assert
    assert response.status_code==200
    assert len(response_body)==2

def test_post_planet(client):
    #Arrange
    planet={"name":"Pluto", "description":"The unlucky one", "biggest_moon":""}
    #Act
    response=client.post("/planets", json=planet)
    response_body=response.get_json()
    #Assert
    assert response.status_code==201
    #assert response_body=="Pluto succesfully created"



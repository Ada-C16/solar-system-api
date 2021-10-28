# get all books and return no records
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# get one book by id
def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == {
        'id' : 1,
        'name' : 'Arrakis',
        'description' : 'sand',
        'xenomorphs' : False
    }

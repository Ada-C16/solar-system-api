def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client, three_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "name" : "Mars",
        "description" : "Hot and dusty",
        "color" : "red"
    }


def test_get_one_book_but_is_empty_returns_error(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == f"Planet 1 not found"

def test_get_all_planets(client, three_saved_planets):
    planet1 = dict(id=1, name="Mars", description="Hot and dusty", color="red")
    planet2 = dict(id=2, name="Earth", description="Nice", color="blue marble")
    planet3 = dict(id=3, name="Saturn", description="Has some rings", color="yellow-brown")

    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert planet1 in response_body
    assert planet2 in response_body
    assert planet3 in response_body

def test_posts_one_planet_successfully(client):
    post_planet = dict(name="Post", description="Posty", color="Postingggg")

    response = client.post("/planets", json={"name" : "Post", "description" :"Posty", "color" : "Postingggg"})
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {"id" : 1, "name" : "Post", "description" :"Posty", "color" : "Postingggg"}

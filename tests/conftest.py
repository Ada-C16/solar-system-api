import pytest
from app import create_app
from app import db
from app.models.planet import Planet #bc we are making an instance of Book in the 3rd function


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def three_saved_planets(app):
    mars_planet = Planet(name="Mars", description="Hot and dusty", color="red")
    earth_planet = Planet(name="Earth", description="Nice", color="blue marble")
    saturn_planet = Planet(name="Saturn", description="Has some rings", color="yellow-brown")

    db.session.add_all([mars_planet, earth_planet, saturn_planet])
    db.session.commit()
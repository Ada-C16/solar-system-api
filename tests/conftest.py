import pytest
from app import create_app
from app import db
from app.models.planet import Planet


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
def one_planet(app):
    planet1 = Planet(name="Mercury", description="Closest to the sun, hot.", has_moons=0)
    db.session.add(planet1)
    db.session.commit()

@pytest.fixture
def two_planets(app):
    planet1 = Planet(name="Mercury", description="Closest to the sun, hot.", has_moons=0)
    planet2 = Planet(name="Venus", description="Spins the opposite direction of other planets.", has_moons=0)
    db.session.add_all([planet1, planet2])
    db.session.commit()
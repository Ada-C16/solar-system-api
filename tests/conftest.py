import pytest

from app import create_app, db
from app.models.planet import Planet

#app
@pytest.fixture
def app():
    app = create_app({"Testing": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

#client
@pytest.fixture
def client(app):
    return app.test_client()

#data
@pytest.fixture
def one_planet(app):
    new_planet = Planet(
        name="Jupiter", description="A planet in the Milky Way", size_rank=1)
    db.session.add(new_planet)
    db.session.commit()

@pytest.fixture
def multiple_planets(app):
    planet_one = Planet(
        name="Jupiter", description="A planet in the Milky Way", size_rank=1)
    planet_two = Planet(
        name="Saturn", description="A planet in the Milky Way", size_rank=2)
    db.session.add(planet_one)
    db.session.add(planet_two)
    db.session.commit()    

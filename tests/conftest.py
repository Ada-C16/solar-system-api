import pytest
from app import create_app, db
from app.models.Planet import Planet

@pytest.fixture
def app():
    app = create_app(True)
    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_planets(app):
    planet_1=Planet(name="Pluto", description="The unlucky one", biggest_moon="")
    planet_2=Planet(name="Saturn", description="The one with rings", biggest_moon="Titan")
    db.session.add_all([planet_1, planet_2])
    db.session.commit()




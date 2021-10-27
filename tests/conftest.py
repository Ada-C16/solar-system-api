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
def two_saved_planets(app):
    # Arrange
    planet_1 = Planet(name="Planet 1",
                    description="I'm planet 1",
                    type="gas giant")
    planet_2 = Planet(name="Planet 2",
                    description="I'm planet 2",
                    type="gas giant")

    db.session.add(planet_1)
    db.session.add(planet_2)

    db.session.commit()
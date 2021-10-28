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
    planet_1 = Planet(name="Mercury",
                      description="first planet",
                      moons=0)
    planet_2 = Planet(name="Saturn",
                      description="multiengaged planet",
                      moons=82)

    db.session.add_all([planet_1, planet_2])
    db.session.commit()


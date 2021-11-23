import pytest
from app import db
from app import create_app
from app.models.planets import Planet

# Arrange

@pytest.fixture
def app():
    app = create_app({"TESTING":True})

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
    planet1 = Planet(
        name = "Earth",
        description = "blue and green",
        oxygen_level = "21%"
    )
    planet2 = Planet(
        name = "Saturn",
        description = "a ball of gas",
        oxygen_level = "little to none"
    )

    db.session.add_all([planet1, planet2])
    db.session.commit()


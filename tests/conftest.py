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
    planet1 = Planet(
        name="Earth", description="Blue green marble", distance="Right here")
    planet2 = Planet(name="Mars", description="red", distance="next door")
    db.session.add_all([planet1, planet2])
    db.session.commit()

import pytest
from app import create_app
from app import db
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING" : True})

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
    earth = Planet(
        name="Earth",
        description="Its a planet",
        distance_from_sun=92
    )

    mercury = Planet(
        name="Mercury",
        description="Its a planet",
        distance_from_sun=35
    )

    db.session.add_all([earth, mercury])
    db.session.commit()

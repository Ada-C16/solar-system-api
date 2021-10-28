import pytest
from app import db
from app import create_app
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
    mars = Planet(name = "Mars", description="Red planet")
    saturn = Planet(name = "Saturn", description="Lots of rings!")

    db.session.add_all([mars, saturn])
    db.session.commit()
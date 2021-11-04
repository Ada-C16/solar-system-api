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
def two_planets_populated(app):

    mercury = Planet(name = "mercury",
                  description = "Smol orbit")
    venus = Planet(name = "venus",
                  description = "Orange for days")
    
    db.session.add_all([mercury, venus])
    db.session.commit()

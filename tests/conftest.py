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
def add_planet():
    pluto = Planet(name="pluto", description="way out there", sign="Scorpio")
    db.session.add(pluto)
    db.session.commit()

@pytest.fixture
def add_three_planets():
    pluto = Planet(name="pluto", description="way out there", sign="Scorpio")
    mercury = Planet(name="mercury", description="messenger closest to sign", sign="Virgo")
    saturn = Planet(name="saturn", description="forever hula hooping", sign="Capricorn")

    db.session.add_all([pluto, mercury, saturn])
    db.session.commit()
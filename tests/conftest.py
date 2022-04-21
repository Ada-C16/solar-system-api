import pytest
from app import create_app, db
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"Testing": True})

    with app.app_context():
        db.create_all()
        yield app

    
    with app.app_context():
        db.drop_all()



@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_planet(app):
    new_planet = Planet(
        color="light brown", description = "in betwen Mars and Saturn",distance = "5", name= "Jupiter")
    db.session.add(new_planet)
    db.session.commit()
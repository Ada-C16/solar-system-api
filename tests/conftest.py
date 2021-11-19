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
    jupiter_planet = Planet(
    name="Jupiter", 
    diameter="Diameter: 86,881 miles (139,822 km)", 
    moons=True, 
    picture="https://cdn.mos.cms.futurecdn.net/WyxFYsiUAQAgU4peSSoBNZ-970-80.png"
)
    saturn_planet = Planet(name="Saturn", 
    diameter="Diameter: 74,900 miles (120,500 km)", 
    moons=True, 
    picture="https://cdn.mos.cms.futurecdn.net/bDVqRSjnbY9jMyVPmStUBY-970-80.png"
)

    db.session.add_all([jupiter_planet, saturn_planet])
   
    db.session.commit()
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
    arrakis_planet = Planet(
        name="Arrakis",
        description="Got the spice",
        has_moons=True
    )
    pluto_planet = Planet(
        name="Pluto",
        description="sad",
        has_moons=True
    )

    db.session.add_all([arrakis_planet, pluto_planet])
    db.session.commit()
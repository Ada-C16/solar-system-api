from os import name
import pytest
from app import create_app
from app import db
from app.models.solar import Planet

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

# from app.models.solar import Planet

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    saturn_planet = Planet(name="Saturn",description="Icy rings")
    pluto_planet = Planet(name="Pluto",description="reallly small")

    db.session.add_all([saturn_planet, pluto_planet])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()

    
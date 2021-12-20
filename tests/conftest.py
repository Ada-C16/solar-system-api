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
    planet_1 = Planet(name="Sun",
                      description="Fire and warmth 4evr",
                      color="Orange")
    planet_2 = Planet(name="Venus",
                         description="Ruler of Libra and Taurus",
                         color="Purple")

    db.session.add_all([planet_1, planet_2])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()
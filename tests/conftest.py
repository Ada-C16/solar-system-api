import pytest
from app import create_app
from app import db
from apps.model.planet import Planet


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
  nine_planet = Planet(name="Planet Nine",
                    description="mysterious shadow planet",
                    circum= 10000)
  pluto_planet = Planet(name="Pluto",
                        description="not named after a cartoon",
                        circum = 9000)

  db.session.add_all([nine_planet, pluto_planet])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()
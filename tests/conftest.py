# file to store all my fixtures; confiure test: conftest
# from flask import Flask
import pytest
from app import create_app, db
from app.models.planet import Planet

# app
@pytest
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()  # creates empty database
        yield app

    with app.app_context():
        db.drop_all()   # deletes data

# client
@pytest.fixture
def client(app):
    return app.test_client()

# data
@pytest.fixture
def save_two_planets(app):
    # Arrange
    dune_planet = Planet(name="Arrakis",
                        description="sand",
                        xenomorhps=False)

    water_planet = Planet(title="Water",
                        description="waterisLife",
                        xenomorphs=True)

    db.session.add_all([dune_planet, water_planet])
    db.session.commit()

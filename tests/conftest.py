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
    Jupiter = Planet(name="Jupiter",
                      description="whatever")
    Saturn = Planet(name="Saturn",
                         description="another planet")

    db.session.add_all([Jupiter, Saturn])
    db.session.commit()
import pytest
from app import create_app
from app import db
from app.models.planet import Planet #bc we are making an instance of Book in the 3rd function


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
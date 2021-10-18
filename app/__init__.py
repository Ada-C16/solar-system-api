#create app function and registering blueprints
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    from .routes import planets_bp #importing from routes
    app.register_blueprint(planets_bp) #registering the route

    return app

from flask import Flask, jsonify


def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import planet_system_bp
    app.register_blueprint(planet_system_bp)

    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    return app

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    from .routes import bodies_bp
    app.register_blueprint(bodies_bp)

    return app

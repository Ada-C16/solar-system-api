from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    from .routes import planet_list_bp
    app.register_blueprint(planet_list_bp)
    return app

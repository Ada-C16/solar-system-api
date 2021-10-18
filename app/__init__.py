from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    from .routes import solarsystem_bp
    app.register_blueprint(solarsystem_bp)

    return app

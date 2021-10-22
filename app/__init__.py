from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

<<<<<<< HEAD
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.planet import Planet

    from .routes import planets_db
    app.register_blueprint(planets_db)
=======
    from .routes import planets_bp
    app.register_blueprint(planets_bp)
>>>>>>> ea02a294217126cdd6f0e378525bd08e8e88c4ec

    return app

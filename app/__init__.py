from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

import os

load_dotenv()

db = SQLAlchemy()   
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DEV_DB')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_DB')
    

    db.init_app(app)
    migrate.init_app(app, db)


    from .routes import solar_systems_bp
    app.register_blueprint(solar_systems_bp)

    from app.models.planet import Planet

    return app





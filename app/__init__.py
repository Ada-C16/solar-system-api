from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os


db=SQLAlchemy()
migrate=Migrate()
load_dotenv()

# DATABASE_CONNECTION_STRING='postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'
def create_app(test_config=None):
    app=Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")
    # from app.models.planet import Planet

    db.init_app(app)
    migrate.init_app(app,db)

    from app.models.planet import Planet
    
    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    return app





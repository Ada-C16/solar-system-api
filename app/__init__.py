from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

# initialize sqlalchemy
db = SQLAlchemy()
migrate = Migrate()

# set the database connection string
DATABASE_CONNECTION_STRING = 'postgresql+psycopg2://postgres:postgres@localhost:5432/our_universe'


def create_app(test_config=None):
    app = Flask(__name__)

    # configure sql alchemy
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_STRING

    # import models
    from app.models.planet import Planet

    # hook up flask and sql alchemy
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    
    return app
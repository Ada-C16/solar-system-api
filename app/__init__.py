#create app function and registering blueprints
# Step 1: import and initialize 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

DATABASE_CONNECTION_STRING = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'


def create_app(test_config=None):
    app = Flask(__name__)

    # Step 2: Configure SQLAlchemy
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_STRING

    # Step 3: hook up Flask to SQLAlchemy
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import planets_bp #importing from routes
    app.register_blueprint(planets_bp) #registering the route

    return app



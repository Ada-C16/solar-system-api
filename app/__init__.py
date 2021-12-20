from flask import Flask
# Step 1:
# Import and initialize SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Initialize SQLAlchemy
db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    
    # Step 2:
    # Configure SQLAlchemy
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    if not test_config:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_CONNECTION_STRING")
    else:
        app.config["TESTING"]=True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_TEST_CONNECTION_STRING")

    # Import Models here!
    from app.models.planet import Planet

    # Step 3:
    # Hook up Flask & SQLALchemy
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    return app

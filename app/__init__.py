from flask import Flask
# Step 1:
# Import and initialize SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize SQLAlchemy
db = SQLAlchemy()
migrate = Migrate()
DATABASE_CONNECTION_STRING='postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

def create_app(test_config=None):
    app = Flask(__name__)

    # Step 2:
    # Configure SQLAlchemy
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_STRING

    # Import Models here!
    from app.models.planet import Planet

    # Step 3:
    # Hook up Flask & SQLALchemy
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    return app

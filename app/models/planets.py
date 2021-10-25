# attribuites: id, name, description + 1
from app import db

class Planet(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(64))
    num_moons = db.Column(db.Integer)
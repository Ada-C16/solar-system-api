from flask import Blueprint
class Planet:
    def __init__(self, id, name, description, moon):
        self.id = id
        self.name = name
        self.description = description 
        self.moon = moon 

planets = [
    Planet(1, "Saturn", "A gassy, heavy, giant who's sixth from the sun. Most likely compposed of iron, nickel, and rock.", 82),
    Planet(2, "Mercury", "When it retrogrades everything in the world sucks.", 0),
    Planet(3, "Venus", "It is named after the goddess of love and beauty. Second brightest object in the sky.", 0)
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
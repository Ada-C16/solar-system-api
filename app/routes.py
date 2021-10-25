from flask import Blueprint
from flask import Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Planet:
    def __init__(self, id, name, description, moon):
        self.id = id
        self.name = name
        self.description = description 
        self.moon = moon 
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "moon": self.moon
        }

# planets = [
#     Planet(1, "Saturn", "A gassy, heavy, giant who's sixth from the sun. Most likely compposed of iron, nickel, and rock.", 82),
#     Planet(2, "Mercury", "When it retrogrades everything in the world sucks.", 0),
#     Planet(3, "Venus", "It is named after the goddess of love and beauty. Second brightest object in the sky.", 0)
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# @planets_bp.route("", methods=["GET"])

# def read_planets():
#     planet_response = []
#     for planet in planets:
#         planet_response.append(
#         planet.to_json()
#         )
#     return jsonify(planet_response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def read_single_planet(planet_id): 
#     planet_id = int(planet_id)
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet.to_json()
        # consider writing conditional that returns
        # a message if planet id does not exist. 
    
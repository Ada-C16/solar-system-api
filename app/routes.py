from flask import Blueprint, jsonify
from .planet import Planet

planets = [
    Planet(1, "Mercury", "Mercury is the smallest planet in the Solar System and the closest to the Sun", "terrestrial"), 
    Planet(2, "Venus", "Venus is the second planet from the Sun.", "terrestrial")
]

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "type": planet.type,
            }
        )
    return jsonify(planets_response)
    
@planet_bp.route("/<planet_id>", methods=["GET"])
def planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "type": planet.type,
            }
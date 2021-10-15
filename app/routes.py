from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, distance):
        self.id = id
        self.name = name
        self.description = description
        self.distance = distance

planets = [
    Planet(1, "Mars", "The red planet", "Inner part of solar system"),
    Planet(2, "Jupiter", "The giant planet", "Outer part of the solar system"),
    Planet(3, "Pluto", "The no-longer a planet, planet", "The outer, outer limits"),
    Planet(4, "Venus", "The gassy one", "Inner planet, Earth's neighbor")
]

planets_bp = Blueprint("/planets", __name__, url_prefix="/planets")
@planets_bp.route("", methods=["GET"])
def get_planets():
    planets_response = []
    for planet in planets:
        response = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "distance": planet.distance,
            "status": 200
        }
        planets_response.append(response)
    return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            response = {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "distance": planet.distance,
                "status": 200
            }
    return jsonify(response)
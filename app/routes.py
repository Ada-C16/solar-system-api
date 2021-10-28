from flask import Blueprint, jsonify


class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }


planets = [
    Planet(1, "Mercury", "Coffee"),
    Planet(2, "Venus", "Girl"),
    Planet(3, "Earth", "Us"),
    Planet(4, "Mars", "Elon"),
    Planet(5, "Jupiter", "Big"),
    Planet(6, "Saturn", "Rings"),
    Planet(7, "Uranus", "Lol"),
    Planet(8, "Neptune", "Cold"),
    Planet(9, "Pluto", "Who?"),
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = [planet.to_json() for planet in planets]
    return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return planet.to_json()

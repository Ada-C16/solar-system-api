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
    Planet(1, "Venus", "Girl"),
    Planet(1, "Earth", "Us"),
    Planet(1, "Mars", "Elon"),
    Planet(1, "Jupiter", "Big"),
    Planet(1, "Saturn", "Rings"),
    Planet(1, "Uranus", "Lol"),
    Planet(1, "Neptune", "Cold"),
    Planet(1, "Pluto", "Who?"),
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = [planet.to_json() for planet in planets]
    return jsonify(planets_response)

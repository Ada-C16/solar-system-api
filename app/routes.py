from flask import Blueprint, jsonify
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

class Planet():

    def __init__(self, id, name, description, major_moons=None):
        self.id = id
        self.name = name
        self.description = description
        if major_moons == None:
            self.major_moons = []
        else:
            self.major_moons = major_moons

PLANETS = [
    Planet(1, "Mercury", "The smallest planet in our solar system", None),
    Planet(2, "Saturn", "Saturn is a gas giant made of mostly hydrogen and helium", ["Titan", "Dione", "Enceladus", "Hyperion"]),
    Planet(3, "Pluto", "Not sure if it's a real planet, but we like it", ["Charon"])
]

@planets_bp.route("", methods=["GET"])
def get_planets():
    planets_response = []
    for planet in PLANETS:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.major_moons
        })
    return jsonify(planets_response)


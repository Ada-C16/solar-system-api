from flask import Blueprint, jsonify
class Planet:
    def __init__(self, id, name, description, moons):
        self.id=id
        self.name=name
        self.description=description
        self.moons=moons

list_of_planets= [
    Planet(1, "Mercury", "Closest to the Sun.", 0),
    Planet(2, "Venus", "Second from the Sun.", 0),
    Planet(3, "Earth", "Our Home.", 1),
    Planet(4, "Mars", "Red Planet.", 2),
    Planet(5, "Jupiter", "Biggest planet.", 79),
    Planet(6, "Saturn", "Ringed planet.", 82),
    Planet(7, "Uranus", "Seventh planet from the Sun.", 27),
    Planet(8, "Neptune", "Most distant from the Sun.", 14),
    Planet(9, "Pluto", "Dwarf planet.", 5)
    ] 
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in list_of_planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons
        })
    return jsonify(planets_response)
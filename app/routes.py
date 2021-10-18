from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, size_rank):
        self.id = id
        self.name = name
        self.description = description
        self.size_rank = size_rank

    def to_dictionary(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "size_rank": self.size_rank         
            }

planets = [
    Planet(20, "Jupiter", "Planet in the Milky Way", 1),
    Planet(21, "Saturn", "Planet in the Milky Way", 2),
    Planet(22, "Uranus", "Planet in the Milky Way", 3),
    Planet(23, "Neptune", "Planet in the Milky Way", 4),
    Planet(24, "Earth", "Planet in the Milky Way", 5),
    Planet(25, "Venus", "Planet in the Milky Way", 6),
    Planet(26, "Mars", "Planet in the Milky Way", 7),
    Planet(27, "Mercury", "Planet in the Milky Way", 8),
    Planet(28, "Pluto", "Planet in the Milky Way", 9),
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("/", methods=["GET"])
def get_all_planets():
    response_list = []
    for planet in planets:
        response_list.append(planet.to_dictionary())
    return jsonify(response_list) 

@planets_bp.route("/<planet_id>", methods=["GET"],)
def get_one_planet_by_id(planet_id):
    for planet in planets:
        if int(planet_id) == planet.id:
            return planet.to_dictionary()


from flask import Blueprint, jsonify

planets_bp = Blueprint("Planet", __name__, url_prefix="/planets")


class Planet:
    def __init__(self, id, name, description, distance_from_sun_mi_million):
        self.id = id
        self.name = name
        self.description = description
        self.distance_from_sun = distance_from_sun_mi_million

planets = [ 
    Planet(1, "Mercury", "", 35), 
    Planet(2, "Venus", "", 67), 
    Planet(3, "Earth", "", 93), 
    Planet(4, "Mars", "", 142)
    ]

@planets_bp.route("", methods = ["GET"])
def handle_planets():
    return jsonify([vars(planet) for planet in planets])

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return vars(planet)
    return "Not found", 404

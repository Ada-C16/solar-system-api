from flask import Blueprint, jsonify
from .list_of_planets import planets

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():

    list_of_planets = []
    for planet in planets:
        list_of_planets.append(planet.create_planet_dictionary()), 200
    
    return jsonify(list_of_planets)

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    for planet in planets:
        if int(planet_id) == planet.id:
            return jsonify(planet.create_planet_dictionary())
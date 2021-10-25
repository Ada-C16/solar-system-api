# localhost:5000/   <-- add url endpoint/parameters here

from flask import Blueprint,jsonify, make_response, request
from app.models.planet import Planet


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# @blueprint_name.route("/endpoint/path/here", methods=["GET"])
@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []

    for planet in PLANETS:
        planets_response.append(planet.to_json())

    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet_id = int(planet_id)

    for planet in PLANETS:
        if planet.id == planet_id:
            return planet.to_json()
# localhost:5000/

from flask import Blueprint, jsonify


class Planet():
    def __init__(self, id, name, description, xenomorphs=False):
        self.id = id
        self.name = name
        self.description = description
        self.xenomorphs = xenomorphs


PLANETS = [

    Planet(426, "Nostromo's End", "Hostile weather.  Toxic atmosphere.  Evidence of civilization.", True),
    Planet(224, "JollyPlanet", "Okay. Decent. Will live for long time.", True)

]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# @blueprint_name.route("/endpoint/path/here", methods=["GET"])
@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []

    for planet in PLANETS:
        planets_response.append(vars(planet))

    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet_id = int(planet_id)

    for planet in PLANETS:
        if planet.id == planet_id:
            return vars(planet)
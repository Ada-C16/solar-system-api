from flask import Blueprint, json, jsonify
from .list_of_planets import planets

# create blueprint which is the decorator of the routes
# it will have a url prefix of /planets
# endpoint will have a prefix of an empty strings
# methods will be get
# create the function for handle planets
# empty list
# loop through planets and add to list
# return the list in json

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():

    list_of_planets = []
    for planet in planets:
        list_of_planets.append(planet.create_planet_dictionary()), 200
    
    return jsonify(list_of_planets)

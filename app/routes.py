from flask import Blueprint,jsonify

class Planet:
    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description

planets = [
    Planet(1, "Mercury", "Very windy."),
    Planet(2, "Venus", "Brightest planet."),
    Planet(3, "Saturn", "Icy rings.")
]

planet_system_bp = Blueprint("planet_system", __name__)
planets_bp = Blueprint("planets_py", __name__, url_prefix= "/planets")

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planets(planet_id):

    for planet in planets:
        if planet.id == int(planet_id):
            return {
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description
            }


@planet_system_bp.route("/planets", methods= ['GET'])
def get_planet_system_json():
    return {
        "planet_1" : "Mercury",
        "planet_2" : "Venus",
        "planet_3" : "Saturn"
    }





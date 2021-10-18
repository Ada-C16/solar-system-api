from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id , name , description , moons):
        self.id = id 
        self.name = name
        self.description = description
        self.moons = moons

planets = [
    Planet(1,"earth","our world",["Moon"]),
    Planet(2,"mars","The red planet",["Phobos","Deimos"]),
    Planet(3,"jupiter", "The biggest one",["Lo","Europa","Callisto","Gayemede"])
]

planets_bp = Blueprint("planet", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = [vars(planet) for planet in planets]

    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return vars(planet) 
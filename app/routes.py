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
    planets_response = []
    for planet in planets: 
        planets_response.append({
            "id": planet.id,
            "name": planet.name, 
            "description": planet.description, 
            "moons": planet.moons
        })
    return jsonify(planets_response)
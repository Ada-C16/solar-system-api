from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, sign):
        self.id = id
        self.name = name
        self.description = description
        self.sign = sign

venus = Planet(1, "Venus", "Planet of beauty", "Libra")
mercury = Planet(2, "Mercury", "Planet of very compute", "Virgo")
jupiter = Planet(3, "Jupiter", "Planet of luck", "Saggitarius")
    
planets = [venus, mercury, jupiter]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def get_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "sign": planet.sign
        })
    return jsonify(planets_response)

from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name 
        self.description = description
        self.color = color
    
    def return_planets(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "color": self.color  
        }
        

planets = [
    Planet(1,"Mercury", "hot", "brown"), 
    Planet(2, "Venus", "pretty", "redish brown"),
    Planet(3, "Earth", "wet", "greenis blue"),
    Planet(6, "Saturn", "rings", "purple and yellow" )

]
    

solar_systems_bp = Blueprint("planets", __name__, url_prefix="/planets")

@solar_systems_bp.route("", methods=["GET"])
def get_planet_json():
    planet_response = []
    for planet in planets:
        planet_response.append(
            planet.return_planets()
        )
    return jsonify(planet_response)

@solar_systems_bp.route("/<planet_id>", methods=["GET"])
def get_each_planet_with_id(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return jsonify(planet.return_planets())

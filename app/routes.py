from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, matter):
        self.id = id
        self.name = name
        self.description = description
        self.matter = matter


planets = [Planet(1, "Mercury", "small and red", "solid"),     
Planet(5, "Jupiter", "big and swirly", "gaseous"), 
Planet(6, "Saturn", "rings and swirls", "gaseous")]


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("",methods=["GET"])
def get_all_planets():
    planet_list=[]
    for planet in planets:
        planet_list.append({"id" : planet.id,
        "name":planet.name,
        "description":planet.description,
        "matter":planet.matter})
    return jsonify(planet_list)

@planets_bp.route("/<planet_id>",methods=["GET"])
def get_one_planet(planet_id):
    planet_id=int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {"id" : planet.id,
            "name":planet.name,
            "description":planet.description,
            "matter":planet.matter}

#    return_value=vars(Planet)
#    return jsonify(return_value)
# make __dict__ in planet class to work with vars
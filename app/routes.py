from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, matter):
        self.id = id
        self.name = name
        self.description = description
        self.matter = matter
    
    def make_dict(self):
        return {"id": self.id,
        "name": self.name,
        "description": self.description,
        "matter": self.matter}


planets = [Planet(1, "Mercury", "small and red", "solid"),     
Planet(5, "Jupiter", "big and swirly", "gaseous"), 
Planet(6, "Saturn", "rings and swirls", "gaseous")]


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("",methods=["GET"])
def get_all_planets():
    planet_list=[]
    for planet in planets:
        planet_list.append(planet.make_dict())
    return jsonify(planet_list)

@planets_bp.route("/<planet_id>",methods=["GET"])
def get_one_planet(planet_id):
    try:
        planet_id=int(planet_id)
    except:
        return("Not a number!")
    for planet in planets:
        if planet.id == planet_id:
            return jsonify(planet.make_dict())
    return ("Not Found!")
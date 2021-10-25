#define our class and make bluprints
from flask import Blueprint, jsonify
from app.models.planets import Planet
from app import db

#class are capitalized
# class Planet: 
#     def __init__(self, id, name, description, num_moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.num_moons = num_moons

# planets = [
#     Planet(1, "Earth", "Green and Blue", 1), 
#     Planet(2, "Mars", "Red and Orange", 2),
#     Planet(3, "Jupiter", "Gray and Brown", 79)
# ]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"]) #decorator communicates with flask
def get_planets(): #function does the work
    planets_response = []
    planets = Planet.query.all()

    for planet in planets:
        planets_response.append({
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "num_moons" : planet.num_moons
        })
    return jsonify(planets_response), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet_id = int(planet_id)
    planet = Planet.query.all(planet_id)
    
    if planet:
        return {
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "num_moons" : planet.num_moons
            }, 200
    
    return f'Planet {planet_id} not found', 404

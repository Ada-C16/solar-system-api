from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.Planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"], strict_slashes=False)
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body['name'], description=request_body['description'], biggest_moon=request_body['biggest_moon'])
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f'{new_planet.name} succesfully created', 201)

# class Planet():
    # def __init__(self, id, name, description, major_moons=None):
    #     self.id = id
    #     self.name = name
    #     self.description = description  
    #     if major_moons == None:
    #         self.major_moons = []
    #     else:
    #         self.major_moons = major_moons

# PLANETS = [
#     Planet(1, "Mercury", "The smallest planet in our solar system", None),
#     Planet(2, "Saturn", "Saturn is a gas giant made of mostly hydrogen and helium", ["Titan", "Dione", "Enceladus", "Hyperion"]),
#     Planet(3, "Pluto", "Not sure if it's a real planet, but we like it", ["Charon"])
# ]

# @planets_bp.route("", methods=["GET"], strict_slashes=False)
# def get_planets():
#     planets_response = []
#     for planet in PLANETS:
#         planets_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "moons": planet.major_moons
#         })
#     return jsonify(planets_response)

# @planets_bp.route("/<id>", methods=["GET"], strict_slashes=False)
# def get_planet(id):
#     id = int(id)
#     for planet in PLANETS:
#         if planet.id == id:
#             return {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "moons": planet.major_moons
#             }

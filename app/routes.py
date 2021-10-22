from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.planet import Planet

# class Planet:
#     def __init__(self, id, name, description, distance):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.distance = distance

# planets = [
#     Planet(1, "Mercury", "Hot, but not too hot for ice", "Innermost planet, closest to the Sun"),
#     Planet(2, "Venus", "The gassy one", "Inner planet, Earth's neighbor"),
#     Planet(3, "Earth", "Blue and green rock where we exist", "Inner solar system, Goldilocks"),
#     Planet(4, "Mars", "The red planet", "Inner part of solar system"),
#     Planet(5, "Jupiter", "The giant planet", "Outer part of the solar system"),
#     Planet(6, "Saturn", "The one with all of the (most visible) rings", "Outter part of the solar system"), 
#     Planet(7, "Uranus", "The lazy one that rotates on it's side", "Outter part of the solar system"),
#     Planet(8, "Neptune", "Named after it's beautiful blue color, but not discovered by sight, instead by mathematical calculations", "Outter part of the solar syatem"),
#     Planet(9, "Pluto", "The no-longer a planet, planet", "The outer, outer limits")
# ]

planets_bp = Blueprint("/planets", __name__, url_prefix="/planets")
@planets_bp.route("", methods=["GET"])
def get_planets():
    planets_response = []
    for planet in planets:
        response = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "distance": planet.distance,
            "status": 200
        }
        planets_response.append(response)
    return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            response = {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "distance": planet.distance,
                "status": 200
            }
    return jsonify(response)

PATH = "https://api.le-systeme-solaire.net/rest/bodies?filter[]%3D=isPlanet,neq,false"

bodies_bp = Blueprint("bodies", __name__, url_prefix="/bodies")
@bodies_bp.route("", methods = ["GET"])
def get_bodies():
    i = 0
    bodies_dict = {}
    response = requests.get(PATH)
    response_bodies = response.json()
    for body in response_bodies["bodies"]:
        bodies_dict[i] = {
            "id": body["id"],
            "english_name": body["englishName"],
            "is_planet": body["isPlanet"]
        }
        i +=1
    return bodies_dict

@bodies_bp.route("/<id>", methods = ["GET"])
def get_body_id(id):
    id = str(id.lower())
    response = requests.get(PATH)
    response_bodies = response.json()
    for body in response_bodies["bodies"]:
        if id == body["id"] or id == body["englishName"]:
            return jsonify(body)
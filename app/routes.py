from flask import Blueprint, jsonify
from planets import Planet


# class Planet:
#     def __init__(self, id, name, description, oxygen):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.oxygen = oxygen


planet1 = Planet(1, "mecury", "its a pretty planet", 0.2)
planet2 = Planet(2, "sun", "its friggin hot", 0)
planet3 = Planet(3, "moon", "its pretty at night", 2)


list_of_planets = [planet1, planet2, planet3]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    books_response = []

    for planet in list_of_planets:
        books_response.append(
            {
                "id" : planet.id,
                "name": planet.name,
                "description": planet.description,
                "oxygen": planet.oxygen
            }
        )

    return jsonify(books_response)

@planets_bp.route("/<planet_name>", methods = ["GET"])
def get_planet_by_name(planet_name):
    for planet in list_of_planets:
        if planet.name == planet_name:
            return {
                "id" : planet.id,
                "name": planet.name,
                "description" : planet.description,
                "oxygen_level" : planet.oxygen
            }



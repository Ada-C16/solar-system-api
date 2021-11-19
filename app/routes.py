from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.planets import Planet


# class Planet:
#     def __init__(self, id, name, description, oxygen):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.oxygen = oxygen


# planet1 = Planet(1, "mecury", "its a pretty planet", 0.2)
# planet2 = Planet(2, "sun", "its friggin hot", 0)
# planet3 = Planet(3, "moon", "its pretty at night", 2)


# list_of_planets = [planet1, planet2, planet3]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["GET", "POST"])
def handle_planets():
    request_body = request.get_json()

    if request.method == "GET":
        planet_response = []
        list_of_planets = Planet.query.all()
        for planet in list_of_planets:
            planet_response.append(
                {
                    "id" : planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "oxygen_level": planet.oxygen_level
                }
            )

        return jsonify(planet_response)
    elif request.method == "POST":
        if "name" not in request_body or "description" not in request_body or "oxygen_level" not in request_body:
            return make_response("Invalid request", 400)

        new_planet = Planet(
            name = request_body["name"],
            description = request_body["description"],
            oxygen_level = request_body["oxygen_level"]
        )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(
            f"Planet {new_planet.name} created", 200
        )
#@planets_bp.route("/<planet_name>", methods = ["GET"])
@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_planet_by_name(planet_id):
    planet = Planet.query.get(planet_id)
    #for planet in list_of_planets:
    #if planet.title == planet_name:
    try:
        return {
            "id" : planet.id,
            "name": planet.name,
            "description" : planet.description,
            "oxygen_level" : planet.oxygen_level
        }
    except:
        planet is None
        return make_response(f"planet {planet_id} is not found", 404)



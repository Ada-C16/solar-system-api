from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_db = Blueprint("planets_db", __name__, url_prefix= "/planets")

@planets_db.route("", methods = ["POST"])
def handle_planets():
    request_body = request.get_json()
    if "name" not in request_body or "description" not in request_body:
        return make_response("Invalid request", 400)
    
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"]
    )
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"Planet {new_planet.name} created successfully", 201)

# class Planet:
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description


# # list of planet
# planets = [
#     Planet(1, "Saturn", "Six planet from the Sun and a gas giant."),
#     Planet(2, "Venus", "Second planet from the Sun and the hottest planet in our solar system."),
#     Planet(3, "Mars", "Fourth planet from the Sun and it is the second smallest planet in our solar system.")

# ]

# planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


# @planets_bp.route("", methods=["GET"])
# def get_list_planets():
#     planets_list = []
#     for planet in planets:
#         planets_list.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description

#         })

#     return jsonify(planets_list)

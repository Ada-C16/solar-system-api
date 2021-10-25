from app import db
from flask import Blueprint, jsonify, make_response, request
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# create new planet
@planets_bp.route("", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        moons=request_body["moons"],
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"New planet {new_planet.name} successfully created!", 201)

# @planets_bp.route("", methods=["GET"])
# def handle_planets():
#     response = []
#     for planet in planets:
#         response.append(planet.to_dict())

#     return jsonify(response)


# @planets_bp.route("<id>", methods=["GET"])
# def handle_planet(id):
#     id = int(id)
#     for planet in planets:
#         if id == planet.id:
#             return planet.to_dict()

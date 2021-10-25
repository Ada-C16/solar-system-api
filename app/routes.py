from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, request, make_response

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"], strict_slashes=False)
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet(
                name=request_body["name"],
                description=request_body["description"],
                size_rank=request_body["size_rank"]
                )
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

# def get_all_planets():
#     response_list = []
#     for planet in planets:
#         response_list.append(planet.to_dictionary())
#     return jsonify(response_list) 

# @planets_bp.route("/<planet_id>", methods=["GET"],)
# def get_one_planet_by_id(planet_id):
#     if not planet_id.isdigit():
#         return {
#         "error": "Invalid planet id.",
#     }, 400 
#     for planet in planets:
#         if int(planet_id) == planet.id:
#             return planet.to_dictionary()
#     return {
#         "error": "Planet not found.",
#     }, 404 

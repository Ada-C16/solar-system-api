from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# Endpoint to create one planet or read all planets
@planets_bp.route("", methods=["POST", "GET"])
def create_planet():
    if request.method == "POST":
        request_body = request.get_json()

        if "name" not in request_body or "description" not in request_body or "color" not in request_body:
            return make_response("Invalid request", 400)

        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            color=request_body["color"]
        )

        db.session.add(new_planet)
        db.session.commit()

        return f"Planet {new_planet.name} created", 201

    elif request.method == "GET":
        planets=Planet.query.all()
        planets_response=[]
        for planet in planets:
            planets_response.append(
                {
                    "id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "color": planet.color
                }
            )
        return jsonify(planets_response)

# @planets_bp.route("", methods=["GET"])
# def handle_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append(
#             {
#                 "id":planet.id,
#                 "name":planet.name,
#                 "description":planet.description,
#                 "color":planet.color
#             }
#         )
#     return jsonify(planets_response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet_id=int(planet_id)
#     for planet in planets:
#         if planet.id == planet_id:
#             return {
#                 "id":planet.id,
#                 "name":planet.name,
#                 "description":planet.description,
#                 "color":planet.color
#             },200

# class Planet:
#     def __init__(self, id, name, description, color):
#         self.id=id
#         self.name=name
#         self.description=description
#         self.color=color

# planets=[
#     Planet(1, "Sun", "center of the solar system", "orange"),
#     Planet(2, "Saturn", "takes approx 29.5 years to complete its orbit", "yellow"),
#     Planet(3, "Mercury", "rules communication", "light grey")
# ]
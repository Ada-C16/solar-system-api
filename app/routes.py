from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, request

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST", "GET"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body:
            return jsonify("Invalid request"), 404

        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"]
        )
        db.session.add(new_planet)
        db.session.commit()

        return jsonify(f"Planet {new_planet.name} created successfully"), 201

    elif request.method == "GET":
        name_query = request.args.get("name")
        if name_query:
            planets = Planet.query.filter_by(name=name_query)
        else:
            planets = Planet.query.all()

        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            })

        return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):

    planet = Planet.query.get(planet_id)

    if planet is None:
        return jsonify("Not Found"), 404

    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        }

    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]

        db.session.commit()

        return jsonify(f"Planet #{planet.id} sucessfully updated"), 200

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return jsonify(f"Planet #{planet.id} sucessfully deleted"), 200

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

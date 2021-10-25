from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")
bodies_bp = Blueprint("bodies", __name__, url_prefix="/bodies")


@planets_bp.route("", methods=["POST", "GET"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        if ("name" or "description" or "distance") not in request_body:
            return make_response("Invalid Request", 400)

        new_planet = Planet(
            id=request_body["id"],
            name=request_body["name"],
            description=request_body["description"],
            distance=request_body["distance"]
        )
        db.session.add(new_planet)
        db.session.commit()
        return make_response(f"Planet {new_planet.name} was successfully created", 201)
    elif request.method == "GET":
        planets = Planet.query.all()
        planets_response = [
            {"id": planet.id, "name": planet.name, "description": planet.description,
             "distance": planet.distance} for planet in planets
        ]
        return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def get_one_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return make_response(f"Planet {planet_id} not found", 404)
    if request.method == "GET":
        response_body = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "distance": planet.distance
        }
        return jsonify(response_body)

    elif request.method == "PUT":
        response_body = request.get_json()
        planet.name = response_body["name"]
        planet.description = response_body["description"]
        planet.distance = response_body["distance"]
        db.session.commit()
        return jsonify(f"{planet.name} was successfully updated"), 200

    elif request.method == "PATCH":
        response_body = request.get_json()
        if "name" in response_body:
            planet.name = response_body["name"]
        elif "description" in response_body:
            planet.description = response_body["description"]
        elif "distance" in response_body:
            planet.distance = response_body["distance"]
        db.session.commit()
        return jsonify(f"{planet.name} was successfully updated"), 200

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return jsonify(f"{planet.name} was successfully deleted"), 200

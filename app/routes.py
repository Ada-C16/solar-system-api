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
            return jsonify("Invalid Request"), 404

        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            distance=request_body["distance"]
        )
        db.session.add(new_planet)
        db.session.commit()
        return jsonify(new_planet.planet_dict()), 201
    elif request.method == "GET":
        planet_name_query = request.args.get("name")
        if planet_name_query:
            planets = Planet.query.filter_by(name=planet_name_query)
        else:
            planets = Planet.query.all()

        planets_response = [
            planet.planet_dict() for planet in planets
        ]
        return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def get_one_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify(f"Planet {planet_id} not found"), 404

    if request.method == "GET":
        return jsonify(planet.planet_dict())

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

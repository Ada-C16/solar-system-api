from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST", "GET"])
def read_planets():
    if request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body:
            return {"error": "Incomplete request body"}, 400

        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            moon=request_body["moon"]
        )
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} created!", 201)

    elif request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append(
                planet.to_json()
            )
        return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def read_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return make_response ("This planet does not exist"), 404
    request_body = request.get_json()

    if request.method == "GET":
        return planet.to_json()

    elif request.method == "PUT":
        planet.name = request_body["name"]
        planet.description = request_body["description"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated")

    elif "name" not in request_body or "description" not in request_body:
        return {
            "message": "Request requires both a name and description"
        }, 400

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} successfully deleted"), 200
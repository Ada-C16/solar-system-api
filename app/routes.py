from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append(
                planet.to_json()
            )
        return jsonify(planets_response)
    
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                        description=request_body["description"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("/<planet_id>", methods=["GET", "PATCH", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if not planet:
        return make_response(f"Planet ID {planet_id} not valid", 404)

    if request.method == "GET":
        return planet.to_json()
    elif request.method == "PATCH":
        request_body = request.get_json()

        if "name" in request_body:
            planet.name = request_body["name"]
        if "description" in request_body:
            planet.description = request_body["description"]

        db.session.commit()

        return make_response(f"Planet {planet.name} updated successfully", 200)
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()

        return make_response(f"{planet.name} successfully deleted", 200)

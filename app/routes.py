from app import db
from flask import Blueprint, jsonify, make_response, request
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST", "GET"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            moons=request_body["moons"],
        )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"New planet {new_planet.name} successfully created!", 201)
    elif request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append(planet.to_dict())
        return jsonify(planets_response)


@planets_bp.route("<id>", methods=["GET", "PATCH", "DELETE"])
def handle_planet(id):
    try:
        planet = Planet.query.get(id)
    except:
        return make_response("Invalid ID", 400)
    if request.method == "GET":
        return planet.to_dict()
    
    elif request.method == "PATCH":
        request_body = request.get_json()
        if "name" in request_body:
            planet.name = request_body["name"]   
        if "description" in request_body:
            planet.description = request_body["description"]     
        if "moons" in request_body:
            planet.moons = request_body["moons"]
        db.session.commit()
        return jsonify([planet.to_dict(), "Update Successful"])
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response("Delete successful", 200)


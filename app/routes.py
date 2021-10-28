from flask import Blueprint, jsonify, request
from app.models.planets import Planet
from app import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_planets(): 
    planets_response = []
    planets = Planet.query.all()

    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response), 200

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet_id = int(planet_id)
    planet = Planet.query.get(planet_id)
    
    if not planet:
        return {"Error": f"Planet {planet_id} was not found"}, 404

    if request.method == "GET":
        return planet.to_dict(), 200
    elif request.method == "PUT":
        input_data = request.get_json()
        if "name" in input_data:
            planet.name = input_data["name"]
        if "description" in input_data:
            planet.description = input_data["description"]
        if "num_moons" in input_data:
            planet.num_moons = input_data["num_moons"]
        db.session.commit()

        return planet.to_dict(), 200
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()

        return (f"Planet {planet.id} successfully updated"), 200


@planets_bp.route("", methods=["POST"])
def create_new_planet():
    request_body = request.get_json()
    
    try:
        new_planet = Planet(name = request_body["name"], description = request_body["description"], num_moons = request_body["num_moons"])

    except KeyError:
        return ("Error! Must include data for all fields."), 400

    db.session.add(new_planet)
    db.session.commit()

    return f"{new_planet.name} Successfully Created", 201


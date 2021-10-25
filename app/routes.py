from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planet", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def get_planets(): 
    planets = Planet.query.all()
    planets_response = []
    for planet in planets: 
        planets_response.append({
            "id": planet.id,
            "name": planet.name, 
            "description": planet.description,
            "moons": planet.moons
        })
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet_id = int(planet_id)
    planets = Planet.query.all()
    for planet in planets:
        if planet.id == planet_id:
            return {
            "id": planet.id,
            "name": planet.name, 
            "description": planet.description,
            "moons": planet.moons
        }
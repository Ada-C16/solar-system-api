from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("Planet", __name__, url_prefix="/planets")


@planets_bp.route("", methods = ["GET", "POST"])
def handle_planets():

    if request.method == "GET":
        planets = Planet.query.all()
        
        planets_response = [planet.to_dict() for planet in planets]

        return jsonify(planets_response)


    elif request.method == "POST":
        request_body = request.get_json()

        new_planet = Planet(name = request_body["name"],
                        description = request_body["description"],
                        distance_from_sun = request_body["distance_from_sun"])
        
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"New Planet {new_planet.name} created", 201)


@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return vars(planet)
    return "Not found", 404

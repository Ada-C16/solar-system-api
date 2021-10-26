from flask import Blueprint, jsonify, request
# from .list_of_planets import planets
from app.models.planet import Planet
from app import db 

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()

        if type(request_body) == list:
            for planet in request_body:
                new_planet = Planet(name = planet["name"], description = planet["description"], has_moons = planet["has_moons"])

                db.session.add(new_planet)
                db.session.commit()
        else:
            new_planet = Planet(name = request_body["name"], description = request_body["description"], has_moons = request_body["has_moons"])
            if "name" not in request_body or "description" not in request_body or "has_moons" not in request_body:
                return jsonify({"message": "Missing information - you need name, description, and if the planet has moons."}), 400

            db.session.add(new_planet)
            db.session.commit()

        return f"New Planets Added!", 201

    elif request.method == "GET":
        planets = Planet.query.all()
        planet_list = []
        for planet in planets:
            planet_list.append(planet.create_planet_dictionary())
        
        return jsonify(planet_list), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):

    planet_id = int(planet_id)
    planet = Planet.query.get(planet_id)

    if planet:
        return jsonify(planet.create_planet_dictionary())

    return { "Error" : f"Planet {planet_id} was not found."}, 404


from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.planet import Planet


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET", "POST"])
def find_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
            })
        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"], description=request_body["description"], color=request_body["color"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"{new_planet.name} has been successfully created", 201)



@planets_bp.route("/<planet_id>", methods=["GET"])
def find_planet(planet_id):
    planet_id = int(planet_id)
    planets = Planet.query.all()
    for planet in planets:
        if planet_id == planet.id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
            }


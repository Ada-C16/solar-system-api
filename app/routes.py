from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = [planet.to_json() for planet in planets]

        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(
            name=request_body["name"], description=request_body["description"]
        )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("/<planet_id>", methods=["GET", "PUT"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if request.method == "GET":
        return planet.to_json()

    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]

        db.session.commit()

        return make_response(f"Book #{planet.id} successfully updated")

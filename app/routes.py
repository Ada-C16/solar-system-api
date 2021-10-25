from flask import Blueprint, jsonify, make_response, request
from app.models.planet import Planet
from app import db


planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")


@planet_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append(
                {
                    "id": planet.id,
                    "title": planet.title,
                    "description": planet.description,
                    "type": planet.type,
                }
            )
        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(title=request_body["title"],
                            description=request_body["description"],
                            type=request_body["type"],
                            )
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.title} successfully created", 201)


@planet_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def planet(planet_id):
    planet = Planet.query.get(planet_id)

    if request.method == "GET":
        return {
            "id": planet.id,
            "title": planet.title,
            "description": planet.description,
            "type": planet.type,
        }
    elif request.method == "PUT":
        form_data = request.get_json()

        planet.title = form_data["title"]
        planet.description = form_data["description"]
        planet.type = form_data["type"]

        db.session.commit()
        return make_response(f"Planet #{planet.id} successfully updated")

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} successfully deleted")

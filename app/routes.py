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
                    "name": planet.name,
                    "description": planet.description,
                    "type": planet.type,
                }
            )
        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                            description=request_body["description"],
                            type=request_body["type"],
                            )
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)


@planet_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE", "PATCH"])
def planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify(f"Error: Planet {planet.id} not found", 404)
    
    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "type": planet.type,
            }
    
    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.type = form_data["type"]

        db.session.commit()
        return jsonify(f"Planet #{planet.id} successfully updated")

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return jsonify(f"Planet #{planet.id} successfully deleted")

    elif request.method == "PATCH":
        request_body = request.get_json()
        
        if "name" in request_body:
            planet.name = request_body["name"]
            db.session.commit()
        if "description" in request_body:
            planet.description = request_body["description"]
            db.session.commit()

        return jsonify(f"Planet # {planet.id} succesfully updated")

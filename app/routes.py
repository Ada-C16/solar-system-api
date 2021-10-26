from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# Endpoint to create one planet or read all planets
@planets_bp.route("", methods=["POST", "GET"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()

        if "name" not in request_body or "description" not in request_body or "color" not in request_body:
            return make_response("Invalid request", 400)

        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            color=request_body["color"]
        )

        db.session.add(new_planet)
        db.session.commit()

        return f"Planet {new_planet.name} created", 201

    elif request.method == "GET":
        planets=Planet.query.all()
        planets_response=[]
        for planet in planets:
            planets_response.append(
                {
                    "id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "color": planet.color
                }
            )
        return jsonify(planets_response)
        
@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    
    if planet is None:
        return make_response(
            f"Planet {planet_id} not found", 404
        )
    if request.method == "GET":

        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
        }, 200

    elif request.method == "PUT":
        request_body=request.get_json()
        if "name" not in request_body or "description" not in request_body or "color" not in request_body:
            return make_response("Invalid request", 400)


        planet.name=request_body["name"]
        planet.description=request_body["description"]
        planet.color=request_body["color"]

        db.session.commit()
        return make_response(f"Planet '{planet.name}' successfully updated")

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet {planet.id} successfully deleted")
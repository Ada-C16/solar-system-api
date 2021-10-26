from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planet", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST", "GET"])
def handle_planet():
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        moons=request_body["moons"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)

    elif request.method == "GET": 
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

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_one_planet(planet_id):
    planet_id = int(planet_id)
    planet = Planet.query.get_or_404(planet_id)

    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name, 
            "description": planet.description,
            "moons": planet.moons
            }
    
    elif request.method == "PUT": 
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.moons = form_data["moons"]

        db.session.commit()

        return make_response(f"Planet {planet.name} successfully updated")
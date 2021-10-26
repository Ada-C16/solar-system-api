
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort
    
solar_systems_bp = Blueprint("planets", __name__, url_prefix="/planets")

@solar_systems_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color,
            })
        return jsonify(planets_response)
        
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        color=request_body["color"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)



def get_planet_from_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"error": "planet_id must be an integer"},400)) 
    return Planet.query.get_or_404(planet_id, description = "{planet not found}")


@solar_systems_bp.route("/<planet_id>", methods=["GET"])
def read_planet(planet_id):
    planet = get_planet_from_id(planet_id)

    return planet.to_dict()


@solar_systems_bp.route("/<planet_id>", methods=["PATCH"])
def update_planet(planet_id):
    planet = get_planet_from_id(planet_id)
    request_body = request.get_json()


    if "name" in request_body:
        planet.name = request_body["name"]
    if "color" in request_body:
        planet.color = request_body["color"]

    db.session.commit()
    return jsonify(planet.to_dict())


@solar_systems_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = get_planet_from_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return jsonify(planet.to_dict())

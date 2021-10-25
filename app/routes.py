from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort

planets_bp = Blueprint("Planet", __name__, url_prefix="/planets")


# Helper Functions

def valid_int(number, parameter_type):
    try:
        int(number)
    except:
        abort(make_response({"error": f"{parameter_type} must be an int"}, 400))

def get_planet_from_id(planet_id):
    valid_int(planet_id, "planet_id")
    return Planet.query.get_or_404(planet_id, description="{planet not found}")

# Routes
@planets_bp.route("", methods = ["GET", "POST"])
def handle_planets():

    if request.method == "GET":
        planets = Planet.query.all()
        
        planets_response = [planet.to_dict() for planet in planets]

        return jsonify(planets_response)


    elif request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body or "distance_from_sun" not in request_body:
            return make_response("Incomplete request body", 400)

        new_planet = Planet(name = request_body["name"],
                        description = request_body["description"],
                        distance_from_sun = request_body["distance_from_sun"])
        
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"New Planet {new_planet.name} created", 201)


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_planet(planet_id):
    planet = get_planet_from_id(planet_id)

    return planet.to_dict(), 200 

@planets_bp.route("/<planet_id>", methods=["PATCH"])
def update_planet(planet_id):
    planet = get_planet_from_id(planet_id)

    request_body = request.get_json()
    if "name" in request_body:
        planet.name = request_body["name"]
    if "description" in request_body:
        planet.description = request_body["description"]
    if "distance_from_sun" in request_body:
        planet.distance_from_sun = request_body["distance_from_sun"]
        
    db.session.commit()
    return jsonify(planet.to_dict())

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = get_planet_from_id(planet_id)

    db.session.delete(planet)
    db.session.commit()
    return make_response(f"Planet #{planet_id} is successfully deleted")
    

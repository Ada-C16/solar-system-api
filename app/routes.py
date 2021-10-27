# localhost:5000/   <-- add url endpoint/parameters here

from flask import Blueprint, jsonify, make_response, request, abort
from app.models.planet import Planet
from app import db

# Global Vars
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


# Helper Functions
def validate_int(user_input, attribute_name):
    try:
        user_input = int(user_input)
    except:
        abort(make_response({"error": "{attribute_name} must be an int"}, 404))

def get_planet(planet_id):
    validate_int(planet_id, "id")

    return Planet.query.get_or_404(planet_id, description="Planet does not exist.")

# Routes
@planets_bp.route("", methods=["POST"])
def create_planets():
    request_body = request.get_json()

    if request_body is None:
        return make_response("Invalid Request", 404)

    new_planet = Planet(
        name=request_body['name'],
        description=request_body['description'],
        xenomorphs=request_body['xenomorphs']
    )

    db.session.add(new_planet)  # like git, stagging changes
    db.session.commit()  # committing to database

    return make_response(f"Your planet, {new_planet.name}, has been created.", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    
    name_query = request.args.get("name")
    xenomorphs_query = request.args.get("xenomorphs")
    
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    elif xenomorphs_query:
        planets = Planet.query.filter_by(xenomorphs=xenomorphs_query)
    else:
        planets = Planet.query.all()

    planets_response = []

    # if planets is None:
    #     return make_response("ENVIRON CTR PURGE", 404)

    for planet in planets:
        planets_response.append(planet.to_json())

    return jsonify(planets_response, 200)


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_a_planet(planet_id):
    planet = get_planet(planet_id)
    return jsonify(planet.to_json(), 200)

@planets_bp.route("/<planet_id>", methods=["PATCH"])
def update_a_planet(planet_id):
    request_body = request.get_json()
    planet = get_planet(planet_id)

    if "id" in request_body:
        planet.id = request_body["id"]
    if "name" in request_body:
        planet.name = request_body["name"]
    if "description" in request_body:
        planet.description = request_body["description"]
    if "xenomorphs" in request_body:
        planet.xenomorphs = request_body["xenomorphs"]

    db.session.commit()
    return jsonify(planet.to_json(), 201)


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_a_planet(planet_id):
    planet = get_planet(planet_id)      

    db.session.delete(planet)
    db.session.commit()
    return make_response(f"Planet #{planet_id} successfully destroyed.", 200)
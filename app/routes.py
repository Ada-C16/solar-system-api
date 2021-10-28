from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, request, make_response, abort

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

#Helper functions
def valid_planet(planet_id):
    try: 
        int(planet_id)
    except:
        abort(make_response({"error": "planet_id must be an int"}, 400))

def get_planet_from_id(planet_id):
    valid_planet(planet_id)
    selected_planet = Planet.query.get_or_404(planet_id)
    return selected_planet

# Routes
@planets_bp.route("", methods=["POST"], strict_slashes=False)
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        size_rank=request_body["size_rank"]
        )
    db.session.add(new_planet)
    db.session.commit()
    return make_response({"planet": new_planet.to_dict()}, 201)

@planets_bp.route("", methods=["GET"], strict_slashes=False)
def get_all_planets():
    planet_objects = Planet.query.all() # returning list of objects
    response_list = []
    for planet in planet_objects:
        response_list.append(planet.to_dict())
    return make_response(jsonify(response_list), 200)

# Routes for single planet
@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    selected_planet = get_planet_from_id(planet_id)
    return make_response({"planet": selected_planet.to_dict()}, 200)

@planets_bp.route("/<planet_id>", methods=["PATCH"])
def update_planet(planet_id):
    selected_planet = get_planet_from_id(planet_id)
    request_body = request.get_json()
    if "name" in request_body:
        selected_planet.name = request_body["name"]
    if "description" in request_body:
        selected_planet.description = request_body["description"]
    if "size_rank" in request_body:
        selected_planet.size_rank = request_body["size_rank"]
    db.session.commit()
    return make_response(f"{selected_planet.name} updated", 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    selected_planet = get_planet_from_id(planet_id)
    db.session.delete(selected_planet)
    db.session.commit()
    return make_response(f"{selected_planet.name} deleted", 200)
        


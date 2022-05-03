from app import db
from flask import Blueprint, jsonify, make_response, request
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def make_input_valid(number):
    try:
        int(number)
    except:
        return make_response(f"{number} is not an int!", 400)

def is_parameter_valid(parameter_id):
    if make_input_valid(parameter_id) is not None:
        return make_input_valid(parameter_id)
    elif Planet.query.get(parameter_id) is None:
        return make_response(f"{parameter_id} is not a valid id!", 404)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planet_list = []
    for planet in planets:
        planet_list.append(planet.make_dict())
    return jsonify(planet_list)


@planets_bp.route("", methods=["POST"])
def post_new_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"], 
                        description=request_body["description"],
                        matter=request_body["matter"])    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created!", 201)


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_planet(planet_id):
    if is_parameter_valid(planet_id) is not None:
        return is_parameter_valid(planet_id)
    planet = Planet.query.get(planet_id)
    return planet.make_dict()


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    if is_parameter_valid(planet_id) is not None:
        return is_parameter_valid(planet_id)
    planet = Planet.query.get(planet_id)
    form_data = request.get_json()
    planet.name = form_data["name"]
    planet.description = form_data["description"]
    planet.matter = form_data["matter"]
    db.session.commit()
    return make_response(f"Planet {planet.name} successfully updated!", 200)

@planets_bp.route("/<planet_id>", methods=["PATCH"])
def update_planet_parameter(planet_id):
    if is_parameter_valid(planet_id) is not None:
        return is_parameter_valid(planet_id)
    planet = Planet.query.get(planet_id)
    form_data = request.get_json()
    if "name" in form_data:
        planet.name = form_data["name"]
    if "description" in form_data:
        planet.description = form_data["description"]
    if "matter" in form_data:
        planet.matter = form_data["matter"]
    db.session.commit()
    return make_response(f"Planet {planet.name} successfully updated!", 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    if is_parameter_valid(planet_id) is not None:
        return is_parameter_valid(planet_id)
    planet = Planet.query.get(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(f"Planet {planet.name} successfully deleted!", 200)




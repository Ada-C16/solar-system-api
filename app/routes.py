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

# Routes
@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    request_body = request.get_json()

    if request.method == "POST":
        if "name" not in request_body:
            return make_response("Invalid Request", 404)

        new_planet = Planet(
            name=request_body['name'],
            # description=request_body['description'],
            # xenomorphs=request_body['']
        )

        db.session.add(new_planet)  # like git, stagging changes
        db.session.commit()  # committing to database

        return make_response(f"Your planet, {new_planet.name}, has been created.", 201)

    elif request.method == "GET":
        planets = Planet.query.all()
        planets_response = []

        for planet in planets:
            planets_response.append(planet.to_json())

        return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET", "PATCH", "DELETE"])
def get_planet(planet_id):
    request_body = request.get_json()
    planet = Planet.query.get(planet_id)

    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"error": "planet_id must be an int"}, 400))

    if request.method == 'GET':
        if planet == None:
            return make_response("your planet ain't real.", 404)
        return planet.to_json()

    elif request.method == 'PATCH':
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
        
    elif request.method == 'DELETE':
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet_id} successfully destroyed.", 200)
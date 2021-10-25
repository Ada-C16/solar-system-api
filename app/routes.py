# localhost:5000/   <-- add url endpoint/parameters here

from flask import Blueprint,jsonify, make_response, request
from app.models.planet import Planet
from app import db


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# @blueprint_name.route("/endpoint/path/here", methods=["GET"])
@planets_bp.route("", methods=["GET", "POST"])

def handle_planets():

    if request.method == "POST":
        request_body = request.get_json()
        if "id" not in request_body or "name" not in request_body:
            return make_response("Invalid Request", 400)
        new_planet = Planet(
            name=request_body['name'],
            description=request_body['description'],
            #xenomorphs=request_body['']
        )
        db.session.add(new_planet) #like git, stagging changes
        db.session.commit() #committing to database

        return make_response(f"Your planet, {new_planet.name}, has been created.", 201)

    elif request.method == "GET":

        planets = Planet.query.all()
        planets_response = []

        for planet in planets:
            planets_response.append(planet.to_json())

        return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet_id = int(planet_id)
    planet = Planet.query.all(planet_id)

    if planet == None:
        return make_response("your planet ain't real.", 404)
        
    return planet.to_json()
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("Planet", __name__, url_prefix="/planets")


@planets_bp.route("", methods = ["GET", "POST"])
def handle_planets():

    if request.method == "GET":
        planets = Planet.query.all()
        
        planets_response = [planet.to_dict() for planet in planets]

        return jsonify(planets_response)


    elif request.method == "POST":
        request_body = request.get_json()

        new_planet = Planet(name = request_body["name"],
                        description = request_body["description"],
                        distance_from_sun = request_body["distance_from_sun"])
        
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"New Planet {new_planet.name} created", 201)


@planets_bp.route("/<planet_id>", methods=["GET", "PATCH", "DELETE"])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id) 
    if planet == None:
        return "Not found", 404
    if request.method == "GET":

        return planet.to_dict(), 200 
    elif request.method == "PATCH":
         request_body = request.get_json()
         if "name" in request_body:
             planet.name = request_body["name"]
         if "description" in request_body:
             planet.description = request_body["description"]
         if "distance_from_sun" in request_body:
             planet.distance_from_sun = request_body["distance_from_sun"]
         db.session.commit()
         return jsonify(planet.to_dict())
    
   
    
    
    

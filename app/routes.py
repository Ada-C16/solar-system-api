from app import db
from app.models.planet import Planet
from flask import json, request, Blueprint, jsonify, make_response
from flask.wrappers import JSONMixin

planets_bp = Blueprint("planets", __name__, url_prefix="/planet")

@planets_bp.route("", methods = ["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_respone = []
        for planet in planets:
            planets_respone.append({
                "id":planet.id,
                "name":planet.name,
                "description":planet.description                
            })
        return jsonify(planets_respone)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet =  Planet(name=request_body["name"],
                             description=request_body["description"])
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name}, {new_planet.id} successfully created", 201)

@planets_bp.route("/<planet_id>", methods = ["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet == None:
        return make_response("", 404)

    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        } 
    elif request.method == "PUT":
        from_data = request.get_json()
        
        planet.name = from_data["name"]  
        planet.description = from_data["description"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated")

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} successfully deleted")  
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request 
from app import db

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    
    if request.method == "GET":
        name_query = request.args.get("name")
        if name_query:
            planets = Planet.query.filter(Planet.name.ilike(name_query))
        else:
            planets = Planet.query.all()

        planets_response = [planet.to_json() for planet in planets]
        
        return jsonify(planets_response), 200

    elif request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body:
            return jsonify("Invalid Request"), 400
            
        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            has_moons=request_body["has_moons"]
        )

        db.session.add(new_planet)
        db.session.commit()
        
        return jsonify(f"created {new_planet.name}"), 201

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return make_response("", 404)
        
    if request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} successfully deleted.", 200)

    elif request.method == "GET":
        return planet.to_json(), 200

    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.has_moons = form_data["has_moons"]

        db.session.commit()

        return make_response(f"planet #{planet.id} successfully updated.", 200)
    

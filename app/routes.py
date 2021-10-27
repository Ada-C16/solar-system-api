from flask import Blueprint, jsonify, make_response, request
from app.models.planet import Planet
from app import db


planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")


@planet_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        name_from_url = request.args.get("name")
        if name_from_url:
            planets = Planet.query.filter_by(name=name_from_url).all()
            if not planets:
                planets = Planet.query.filter(Planet.name.contains(name_from_url))
                
        else:
            planets = Planet.query.all()
            
        planets_response = []
        for planet in planets:
            planets_response.append(planet.create_dict())
        
        if not planets_response:
            planets = Planet.query.all()
            for planet in planets:
                planets_response.append(planet.create_dict())
        
        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                            description=request_body["description"],
                            type=request_body["type"],
                            )
        db.session.add(new_planet)
        db.session.commit()

        # return make_response(new_planet.create_dict(), 201)
        return jsonify(f"Planet with id:{new_planet.id} successfully created"), 201

@planet_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE", "PATCH"])
def planet(planet_id):
    planet = Planet.query.get(planet_id)
    if not planet:
        return jsonify(f"Error: Planet {planet_id} not found"), 404
    
    if request.method == "GET":
        return (planet.create_dict())
            
    
    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.type = form_data["type"]

        db.session.commit()
        return jsonify(f"Planet #{planet.id} successfully updated")

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return jsonify(f"Planet #{planet.id} successfully deleted")

    elif request.method == "PATCH":
        request_body = request.get_json()
        
        if "name" in request_body:
            planet.name = request_body["name"]
            db.session.commit()
        if "description" in request_body:
            planet.description = request_body["description"]
            db.session.commit()
        if "type" in request_body:
            planet.type = request_body["type"]
            db.session.commit()

        return jsonify(f"Planet # {planet.id} succesfully updated")

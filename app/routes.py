from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, request, make_response

planets_bp = Blueprint('planets', __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST", "GET"])
def handle_all_planets():
  if request.method == "POST":
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"], description = request_body["description"], circum = request_body["circum"])
    
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"Planet {new_planet.name} create", 201)
  
  elif request.method == "GET":
    
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
      planets_response.append({"id": planet.id, "name": planet.name, "description": planet.description, "circumference in mkm": planet.circum})
    return jsonify(planets_response)

@planets_bp.route("/<planet_name>", methods=["GET", "PUT", "DELETE"])
def handle_one_planet(planet_name):
  planet = Planet.query.get(planet_name)
  
  if planet is None:
    return make_response(f"Error: Planet {planet_name} not found", 404)
  
  if request.method == "GET":
    return {"id": planet.id, "name": planet.name, "description": planet.description, "circumference": planet.circum} 
  
  elif request.method == "PUT":
    request_body = request.get_json()
    
    if request_body is None:
      return make_response(f"Error: Request requires name, description, and circumference", 400)
  
    elif "name" not in request_body or "description" not in request_body or "circum" not in request_body:
      return make_response(f"Error: Request requires name, description, and circumference", 400)
    
    planet.name = request_body['name']
    planet.description = request_body["description"]
    planet.circum = request_body["circum"]
    
    db.session.commit()
    
    return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "circum": planet.circum
            }, 200
  
  elif request.method == "DELETE":
    db.session.delete(planet)
    db.session.commit()
    return f"{planet.name} was successfully deleted", 200




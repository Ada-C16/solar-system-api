from app import db
from flask import Blueprint, jsonify, request,make_response
from app.models.planet import Planet

solarsystem_bp = Blueprint("solarsystem", __name__, url_prefix="/solarsystem")


@solarsystem_bp.route("", methods=["GET"])
def handle_solarsystem():
    requested_name = request.args.get('name')
    shorter_orbital_period=request.args.get("shorter_orbital_period")
    if requested_name:
        requested_name = requested_name.capitalize()
        planets=Planet.query.filter_by(name=requested_name)
    elif shorter_orbital_period:
        try:
            shorter_orbital_period = int(shorter_orbital_period)
        except ValueError:
            return {"Error": "Orbital period must be numeric"}, 400
        planets=Planet.query.filter(Planet.orbital_period < request.args.get("shorter/orbital_period"))
    elif request.args.get("order_by") == "name":
        planets = Planet.query.order_by(Planet.name.desc())
    else:
        planets = Planet.query.all()
    solarsystem_response = [] 
    for planet in planets:
        solarsystem_response.append(planet.to_dict())
        
    return jsonify(solarsystem_response) 

@solarsystem_bp.route("", methods=["POST"])
def create_solarsystem(): 
    request_date = request.get_json()
    if 'name' not in request_date or 'surface_area' not in request_date or 'orbital_period' not in request_date \
        or 'distance_from_sun' not in request_date or 'radius' not in request_date:
            return jsonify({'message': "missing data"}),400
    new_planet = Planet(
        name= request_date['name'],
        surface_area = request_date['surface_area'],
        orbital_period = request_date['orbital_period'],
        distance_from_sun = request_date['distance_from_sun'],
        radius = request_date['radius']
    )
    db.session.add(new_planet)
    db.session.commit()
    return f" Planet {new_planet.name} created", 201


@solarsystem_bp.route("/<planet_id>", methods=["GET"])  
def get_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"Error": "Id must be numeric"}, 400
    planet = Planet.query.get(planet_id)
    if not planet:
        return {"Error": f"Planet with id number {planet_id} was not found"}, 404
    if request.method == "GET":
        return jsonify(planet.to_dict()), 200

@solarsystem_bp.route("/<planet_id>", methods=["PUT"]) 
def update_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"Error": "Id must be numeric"}, 400
    planet = Planet.query.get(planet_id)

    form_data = request.get_json()
    
    if 'name' not in form_data or 'surface_area' not in form_data or 'orbital_period' not in form_data \
    or 'distance_from_sun' not in form_data or 'radius' not in form_data:
        return jsonify({'message': "missing data"}),400
    
    planet.name = form_data["name"],
    planet.surface_area = form_data["surface_area"]
    planet.orbital_period = form_data["orbital_period"]
    planet.distance_from_sun = form_data["distance_from_sun"]
    planet.radius = form_data["radius"]

    db.session.commit()

    return jsonify(planet.to_dict()), 200





@solarsystem_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"Error": "Id must be numeric"}, 400
    planet = Planet.query.get(planet_id)
    if planet:
        db.session.delete(planet)
        db.session.commit()
        return {"Message": f"Planet with id number {planet_id} deleted."}, 200

    else:
        return {"Message": f"Planet with id number {planet_id} not found"}, 404

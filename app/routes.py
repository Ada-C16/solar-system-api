from app import db
from flask import Blueprint, jsonify, request,make_response
from app.models.planet import Planet

solarsystem_bp = Blueprint("solarsystem", __name__, url_prefix="/solarsystem")


@solarsystem_bp.route("", methods=["GET"])
def handle_solarsystem():
    planets = Planet.query.all()
    # solarsystem_response =[vars(planet) for planet in planets] 
    solarsystem_response = [] 
    for planet in planets:
        solarsystem_response.append({
            'id':planet.id,
            'name':planet.name,
            'surface_area':planet.surface_area,
            'orbital_period':planet.orbital_period,
            'distance_from_sun':planet.distance_from_sun,
            'radius':planet.radius  
        })
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


@solarsystem_bp.route("/<planet_id>", methods=["GET", "PUT"])  
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if not planet:
        return {"Error": f"PLanet {planet_id} was not found"}, 404
    if request.method == "GET":
        return jsonify(planet.to_dict()), 200
    elif request.method == "PUT":
        form_data = request.get_json()
        planet.name = form_data["name"],
        planet.surface_area = form_data["surface_area"]
        planet.orbital_period = form_data["orbital_period"]
        planet.distance_from_sun = form_data["distance_from_sun"]
        planet.radius = form_data["radius"]

        db.session.commit()

        return jsonify(planet.to_dict()), 200


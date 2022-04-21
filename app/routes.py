
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort
    
solar_systems_bp = Blueprint("planets", __name__, url_prefix="/planets")


def valid_int(number,parameter_type):
    try:
        int(number)
    except:
        abort(make_response({"error": f"{parameter_type} must be an integer"},400)) 

def get_planet_from_id(planet_id):
    valid_int(planet_id, "planet_id")
    return Planet.query.get_or_404(planet_id, description = "{planet not found}")
    
#Routes
@solar_systems_bp.route("", methods=["GET"])
def read_all_planets():

        distance_query = request.args.get("distance")
        further_query = request.args.get("further")
        sort_query = request.args.get("sort")


        if distance_query:
            valid_int(distance_query, "distance")
            planets = Planet.query.filter_by(distance = distance_query)
        elif further_query:
            valid_int(further_query, "further")
            planets = Planet.query.filter(Planet.distance > further_query)
        elif sort_query == "asc":
            planets = Planet.query.order_by(Planet.distance.asc())
        elif sort_query == "desc":
            planets = Planet.query.order_by(Planet.distance.desc())
        else:
            planets = Planet.query.all()

        
        planets_response = []
        for planet in planets:
            planets_response.append(
                planet.to_dict()
            )
        return jsonify(planets_response)


@solar_systems_bp.route("", methods=["POST"])
def create_planets():
        request_body = request.get_json()
        if "name" not in request_body or "color" not in request_body or "description" not in request_body or "distance" not in request_body:
            return {"error": "incomplete request body"}, 400
        
        
        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            color=request_body["color"],
            distance=request_body["distance"]
        )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)


@solar_systems_bp.route("/<planet_id>", methods=["GET"])
def read_planet(planet_id):
    planet = get_planet_from_id(planet_id)

    return planet.to_dict()


@solar_systems_bp.route("/<planet_id>", methods=["PATCH"])
def update_planet(planet_id):
    planet = get_planet_from_id(planet_id)
    request_body = request.get_json()

    if "name" in request_body:
        planet.name = request_body["name"]
    if "color" in request_body:
        planet.color = request_body["color"]
    if "description" in request_body:
        planet.description = request_body["description"]
    if "distance" in request_body:
        planet.distance = request_body["distance"]


    db.session.commit()
    return jsonify(planet.to_dict())


@solar_systems_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = get_planet_from_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {jsonify(planet.to_dict())} successfully deleted")

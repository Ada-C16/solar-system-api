from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.planets import Planet


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["GET", "POST"])
def handle_planets():
    request_body = request.get_json()

    if request.method == "GET":
        planet_response = []

        #name_query_param = request.args.get("name")
        name_query_param = request.args.get("name")

        if name_query_param is not None:
            list_of_planets = Planet.query.filter_by(name = name_query_param)
            
        else:
            list_of_planets = Planet.query.all()
        for planet in list_of_planets:
            planet_response.append(
                {
                    "id" : planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "oxygen_level": planet.oxygen_level
                }
            )

        return jsonify(planet_response)
    elif request.method == "POST":
        if "name" not in request_body or "description" not in request_body or "oxygen_level" not in request_body:
            return make_response("Invalid request", 400)

        new_planet = Planet(
            name = request_body["name"],
            description = request_body["description"],
            oxygen_level = request_body["oxygen_level"]
        )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(
            f"Planet {new_planet.name} created", 200
        )
        # planet.query.filter_by(param) # use to filter query results
        # planet.query.limit(100).all() limit number of results
#@planets_bp.route("/<planet_name>", methods = ["GET"])
@planets_bp.route("/<planet_id>", methods = ["GET", "PUT", "DELETE"])
def get_planet_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    #for planet in list_of_planets:
    #if planet.title == planet_name:
    if request.method == "GET":
        try:
            return {
                "id" : planet.id,
                "name": planet.name,
                "description" : planet.description,
                "oxygen_level" : planet.oxygen_level
            }
        except:
            planet is None
            return make_response(f"planet {planet_id} is not found", 404)
    
    elif request.method == "PUT":
        form_data = request.get_json()

        if "name" not in form_data or "description" not in form_data or "oxygen_level" not in form_data:
            return make_response(f"you must include a name, description and oxygen_level for your planet", 400)

        try:
            planet.name = form_data["name"]
            planet.description = form_data["description"]
            planet.oxygen_level = form_data["oxygen_level"]

            return make_response(f"{planet.name} successfully updated", 200)
        except:
            planet is None
            return make_response(f"planet {planet.id} does not exist")
        
    elif request.method == "DELETE":
        planet_to_delete = planet
        try:
            db.session.delete(planet_to_delete)
            db.session.commit()

            return make_response(f"planet {planet.name} successfully deleted", 200)
        except:
            planet_to_delete is None
            return make_response(f"planet {planet_id} does not exsist", 404)




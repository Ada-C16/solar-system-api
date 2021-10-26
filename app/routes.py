from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, request, make_response, abort

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST", "GET"], strict_slashes=False)
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(
                    name=request_body["name"],
                    description=request_body["description"],
                    size_rank=request_body["size_rank"]
                    )
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)
    
    elif request.method == "GET":
        planet_objects = Planet.query.all() # returning list of objects
        response_list = []
        for planet in planet_objects:
            response_list.append(
                {
                    "id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "size_rank": planet.size_rank
                }
            )
        return make_response(jsonify(response_list), 200)


@planets_bp.route("/<planet_id>", methods=["GET", "PATCH", "DELETE"],)
def handle_single_planet(planet_id):
    try: 
        planet_id = int(planet_id)
    except:
        abort(make_response({"error": "planet_id must be an int"}, 400))
    
    selected_planet = Planet.query.get_or_404(planet_id)
    
    if request.method == "GET":
        return make_response({
            "id": selected_planet.id,
            "name": selected_planet.name,
            "description": selected_planet.description,
            "size_rank": selected_planet.size_rank
        }, 200)

    elif request.method == "PATCH":
        request_body = request.get_json()
        if "name" in request_body:
            selected_planet.name = request_body["name"]
        if "description" in request_body:
            selected_planet.description = request_body["description"]
        if "size_rank" in request_body:
            selected_planet.size_rank = request_body["size_rank"]
        db.session.commit()
        return make_response(f"{selected_planet.name} updated", 200)

    elif request.method == "DELETE":
        db.session.delete(selected_planet)
        db.session.commit()
        return make_response(f"{selected_planet.name} deleted", 200)
        


from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planet", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST", "GET"])
def handle_planets():
    """Handles POST and GET requests for /planets. 
        Returns success message if planet successfully created with POST request.
        Returns data on all planets in JSON with GET request."""
    
    if request.method == "POST":
        request_body = request.get_json()

        if "name" not in request_body or "description" not in request_body \
            or "moons" not in request_body: 
            return jsonify({"message": "Missing data"}), 400

        new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        moons=request_body["moons"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)

    elif request.method == "GET": 
        planets = Planet.query.all()
        planets_response = []
        for planet in planets: 
            planets_response.append(planet.to_dict())
        return jsonify(planets_response), 200

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_one_planet(planet_id):
    """Handles GET, PUT, and DELETE requests for one planet entry. 
        Reads and returns planet info for GET request with valid ID input or 404 for invalid ID input.
        Updates planet entry and returns success message for PUT request.
        Deletes specified planet entry and return success message for DELETE request."""
    
    planet_id = int(planet_id)
    planet = Planet.query.get_or_404(planet_id)

    if request.method == "GET":
        return jsonify(planet.to_dict()), 200
    
    elif request.method == "PUT": 
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.moons = form_data["moons"]

        db.session.commit()

        return make_response(f"Planet {planet.name} successfully updated")

    elif request.method == "DELETE": 
        db.session.delete(planet)
        db.session.commit()

        return make_response(f"Planet {planet.name} successfully deleted")
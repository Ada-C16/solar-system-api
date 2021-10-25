from flask import Blueprint, jsonify, request
# from .list_of_planets import planets
from app.models.planet import Planet
from app import db 

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()

        if type(request_body) == list:
            for planet in request_body:
                new_planet = Planet(name = planet["name"], description = planet["description"], has_moons = planet["has_moons"])
                db.session.add(new_planet)
                db.session.commit()
        else:
            new_planet = Planet(name = request_body["name"], description = request_body["description"], has_moons = request_body["has_moons"])
            if "name" not in request_body or "description" not in request_body or "has_moons" not in request_body:
                return jsonify({"message": "Missing information - you need name, description, and if the planet has moons."}), 400

            db.session.add(new_planet)
            db.session.commit()

        return f"New Planet {new_planet.name} Added!", 201
    elif request.method == "GET":
        planets = Planet.query.all()
        planet_list = []
        for planet in planets:
            planet_list.append(planet.create_planet_dictionary())
        
        return jsonify(planet_list), 200
# Able to take both Get and Post requests
# If POST: set up a variable to hold request body 
# Use variable to create new planet instance
# Add to .db session
# Comit db session
# Return a response with a 201 status code
# If GET: Query database, get all planets
# Create planets as dictionaries, put in a list
# Return jsonify list

# list_of_planets = []
# for planet in planets:
#     list_of_planets.append(planet.create_planet_dictionary()), 200

# return jsonify(list_of_planets)

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    pass
    # for planet in planets:
    #     if int(planet_id) == planet.id:
    #         return jsonify(planet.create_planet_dictionary())
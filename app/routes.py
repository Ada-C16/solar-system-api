from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST", "GET"])
def read_planets():
    if request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body:
            return {"error": "Incomplete request body"}, 400

        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            moon=request_body["moon"]
        )
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} created!", 201)

    elif request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append(
                planet.to_json()
            )
        return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return {"error": "planet_id must be an int"}, 400

    planet = Planet.query.get(planet_id)
    return planet.to_json()

    # planet_response = []
    # for planet in planets:
    #     planet_response.append(
    #     planet.to_json()
    #     )
    # return jsonify(planet_response)

# class Planet:
#     def __init__(self, id, name, description, moon):
#         self.id = id
#         self.name = name
#         self.description = description 
#         self.moon = moon 
    
#     def to_json(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "description": self.description,
#             "moon": self.moon
#         }

# planets = [
#     Planet(1, "Saturn", "A gassy, heavy, giant who's sixth from the sun. Most likely compposed of iron, nickel, and rock.", 82),
#     Planet(2, "Mercury", "When it retrogrades everything in the world sucks.", 0),
#     Planet(3, "Venus", "It is named after the goddess of love and beauty. Second brightest object in the sky.", 0)
# ]

# @planets_bp.route("", methods=["GET"])



# @planets_bp.route("/<planet_id>", methods=["GET"])
# def read_single_planet(planet_id): 
#     planet_id = int(planet_id)
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet.to_json()
        # consider writing conditional that returns
        # a message if planet id does not exist. 
    
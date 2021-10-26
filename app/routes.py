from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request




# class Planet:
#     def __init__(self, id, name, description, moons):
#         self.id=id
#         self.name=name
#         self.description=description
#         self.moons=moons

# list_of_planets= [
#     Planet(1, "Mercury", "Closest to the Sun.", 0),
#     Planet(2, "Venus", "Second from the Sun.", 0),
#     Planet(3, "Earth", "Our Home.", 1),
#     Planet(4, "Mars", "Red Planet.", 2),
#     Planet(5, "Jupiter", "Biggest planet.", 79),
#     Planet(6, "Saturn", "Ringed planet.", 82),
#     Planet(7, "Uranus", "Seventh planet from the Sun.", 27),
#     Planet(8, "Neptune", "Most distant from the Sun.", 14),
#     Planet(9, "Pluto", "Dwarf planet.", 5)
#     ] 
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_data=request.get_json()
    if "name" not in request_data or "description" not in request_data or "moons" not in request_data:
        return jsonify({"message": "missing data"}),400
    new_planet=Planet(name=request_data["name"],description=request_data["description"], moons=request_data["moons"])
    db.session.add(new_planet)
    db.session.commit()

    return f"Planet {new_planet.name} created", 201


@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet_id = int(planet_id)
    planet = Planet.query.get(planet_id)
    if not planet:
        return { "Error": f"Planet {planet_id} was not found"}, 404
    return jsonify(planet.to_dict()), 200
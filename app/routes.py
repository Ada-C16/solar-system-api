#define our class and make bluprints
from flask import Blueprint, jsonify, request
from app.models.planets import Planet
from app import db


#class are capitalized
# class Planet: 
#     def __init__(self, id, name, description, num_moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.num_moons = num_moons

# planets = [
#     Planet(1, "Earth", "Green and Blue", 1), 
#     Planet(2, "Mars", "Red and Orange", 2),
#     Planet(3, "Jupiter", "Gray and Brown", 79)
# ]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"]) #decorator communicates with flask
def get_planets(): #function does the work
    planets_response = []
    planets = Planet.query.all()

    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response), 200

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet_id = int(planet_id)
    planet = Planet.query.get(planet_id)
    
    if not planet:
        return {"error": f"Planet {planet_id} was not found"}, 404

    if request.method == "GET":
        return planet.to_dict(), 200
    elif request.method == "PUT":
        input_data = request.get_json()
        if "name" in input_data:
            planet.name = input_data["name"]
        if "description" in input_data:
            planet.description = input_data["description"]
        if "num_moons" in input_data:
            planet.num_moons = input_data["num_moons"]
        db.session.commit()

        return planet.to_dict(), 200
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()

        return (f"Planet {planet.id} successfully updated"), 200


@planets_bp.route("", methods=["POST"])
def create_new_planet():
    request_body = request.get_json()
    # if statement for 400
    new_planet = Planet(name = request_body["name"], description = request_body["description"], num_moons = request_body["num_moons"])

    db.session.add(new_planet)
    db.session.commit()

    return f"{new_planet.name} Successfully Created", 201


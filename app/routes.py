from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.Planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST","GET"], strict_slashes=False)
def create_planet():
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body['name'], description=request_body['description'], biggest_moon=request_body['biggest_moon'])
        db.session.add(new_planet)
        db.session.commit()
        return make_response(f'{new_planet.name} succesfully created', 201)
    elif request.method == "GET":
        planets = Planet.query.all()
        response = []
        for planet in planets:
            response.append(planet.to_dict())
        return jsonify(response), 200

@planets_bp.route("/<id>", methods=["GET"], strict_slashes=False)
def get_planet(id):
    id = int(id)
    planets = Planet.query.all()
    for planet in planets:
        if planet.id == id:
            return planet.to_dict(), 200

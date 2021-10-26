from app import db
from flask import Blueprint, jsonify, make_response, request, abort
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST", "GET"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            moons=request_body["moons"],
        )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"New planet {new_planet.name} successfully created!", 201)
    elif request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append(planet.to_dict())
        return jsonify(planets_response)


def get_planet_from_id(id):
    try:
        id = int(id)
    except:
        abort(400, {"error": "invalid id"})
    return Planet.query.get_or_404(id)


@planets_bp.route("<id>", methods=["GET"])
def read_planet(id):
    planet = get_planet_from_id(id)
    return planet.to_dict()


@planets_bp.route("<id>", methods=["PATCH"])
def update_planet(id):
    planet = get_planet_from_id(id)
    request_body = request.get_json()
    if "name" in request_body:
        planet.name = request_body["name"]
    if "description" in request_body:
        planet.description = request_body["description"]
    if "moons" in request_body:
        planet.moons = request_body["moons"]
    db.session.commit()
    return jsonify([planet.to_dict(), "Update Successful"])


@planets_bp.route("<id>", methods=["DELETE"])
def delete_planet(id):
    planet = get_planet_from_id(id)
    db.session.delete(planet)
    db.session.commit()
    return make_response("Delete successful", 200)

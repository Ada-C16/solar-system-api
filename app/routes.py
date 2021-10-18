from flask import Blueprint, jsonify

from .planet import Planet

planets = [
    Planet(1, "Mars", "Red Planet", ["Phobos", "Deimos"]),
    Planet(2, "Earth", "Blue Marbel", ["Luna"]),
    Planet(3, "Pluto", "It IS a planet!", [
           "Charon", "Nix", "Hydra", "Kerberos", "Styx"]),
    Planet(4, "Venus", "She's Pretty", [])
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"])
def handle_planets():
    response = []
    for planet in planets:
        response.append(planet.to_dict())

    return jsonify(response)


@planets_bp.route("<id>", methods=["GET"])
def handle_planet(id):
    id = int(id)
    for planet in planets:
        if id == planet.id:
            return planet.to_dict()

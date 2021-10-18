from flask import Blueprint, jsonify


class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


# list of planet
planets = [
    Planet(1, "Saturn", "Six planet from the Sun and a gas giant."),
    Planet(2, "Venus", "Second planet from the Sun and the hottest planet in our solar system."),
    Planet(3, "Mars", "Fourth planet from the Sun and it is the second smallest planet in our solar system.")

]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"])
def get_list_planets():
    planets_list = []
    for planet in planets:
        planets_list.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description

        })

    return jsonify(planets_list)

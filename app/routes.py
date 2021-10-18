from flask import Blueprint, jsonify


class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


# list of planets
planets = [
    Planet(1, "Saturn", "Six planet from the Sun and a gas giant."),
    Planet(2, "Venus", "Second planet from the Sun and the hottest planet in our solar system."),
    Planet(3, "Mars", "Fourth planet from the Sun and it is the second smallest planet in our solar system.")

]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# search request for list of planets


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

# search request for one planet and return 404 if not found


@planets_bp.route("/<planet_id>", methods=["GET"])
def planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet_id == planet.id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            }
        elif planet_id != planet.id:
            return (f"Planet {planet_id} not found."), 404

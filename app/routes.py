from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id=id
        self.name=name
        self.description=description
        self.color=color

planets=[
    Planet(1, "Sun", "center of the solar system", "orange"),
    Planet(2, "Saturn", "takes approx 29.5 years to complete its orbit", "yellow"),
    Planet(3, "Mercury", "rules communication", "light grey")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id":planet.id,
                "name":planet.name,
                "description":planet.description,
                "color":planet.color
            }
        )
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet_id=int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id":planet.id,
                "name":planet.name,
                "description":planet.description,
                "color":planet.color
            },200

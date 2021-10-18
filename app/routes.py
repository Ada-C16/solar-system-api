from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, title, description, moon):
        self.id = id
        self.title = title
        self.description = description
        self.moon = moon

planets= [
    Planet(1, "Mercury", "Diameter: 3,031 miles (4,878 km)", False), 
    Planet(2, "Venus", "Diameter: 7,521 miles (12,104 km)", False),
    Planet(3, "Earth", "Diameter: 7,926 miles (12,760 km)", True),
    Planet(4, "Mars", "Diameter: 4,217 miles (6,787 km)", True), 
    Planet(5, "Jupiter", "Diameter: 86,881 miles (139,822 km)", True), 
    Planet(6, "Saturn", "Diameter: 74,900 miles (120,500 km)", True),
    Planet(7, "Uranus", "Diameter: 31,763 miles (51,120 km)", True),
    Planet(8, "Neptune", "Diameter: 30,775 miles (49,530 km)", True)
]

planets_bp = Blueprint("planets_bp", __name__,url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
            "id": planet.id,
            "title": planet.title,
            "description": planet.description,
            "moon":planet.moon
            }
        )
    return jsonify(planets_response)
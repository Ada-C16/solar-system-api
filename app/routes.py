from flask import Blueprint, jsonify, render_template, make_response, request
from app import db
from app.models.planet import Planet

# class Planet:
#     def __init__(self, id, title, description, moon, picture):
#         self.id = id
#         self.title = title
#         self.description = description
#         self.moon = moon
#         self.picture = picture

# planets= [
#     Planet(1, "Mercury", "Diameter: 3,031 miles (4,878 km)", False, "https://cdn.mos.cms.futurecdn.net/oU94fqcyf9HzQc59wJyaHN-970-80.jpg"), 
#     Planet(2, "Venus", "Diameter: 7,521 miles (12,104 km)", False, "https://cdn.mos.cms.futurecdn.net/KhHofvaDG73pypCEzyLuab-970-80.png"),
#     Planet(3, "Earth", "Diameter: 7,926 miles (12,760 km)", True, "https://cdn.mos.cms.futurecdn.net/4aeTmiqCqpRKuFc8tkDcmm-970-80.jpg"),
#     Planet(4, "Mars", "Diameter: 4,217 miles (6,787 km)", True, "https://cdn.mos.cms.futurecdn.net/tQUhJUq9GXqMfZXjGYdw8c-970-80.jpg"), 
#     Planet(5, "Jupiter", "Diameter: 86,881 miles (139,822 km)", True, "https://cdn.mos.cms.futurecdn.net/WyxFYsiUAQAgU4peSSoBNZ-970-80.png"), 
#     Planet(6, "Saturn", "Diameter: 74,900 miles (120,500 km)", True, "https://cdn.mos.cms.futurecdn.net/bDVqRSjnbY9jMyVPmStUBY-970-80.png"),
#     Planet(7, "Uranus", "Diameter: 31,763 miles (51,120 km)", True, "https://cdn.mos.cms.futurecdn.net/kZXxHS85dDgVEAviQrM2KW-970-80.jpg"),
#     Planet(8, "Neptune", "Diameter: 30,775 miles (49,530 km)", True, "https://cdn.mos.cms.futurecdn.net/KW2AU72GRriUXQvsn5jAbg-970-80.jpg")
# ]

planets_bp = Blueprint("planets_bp", __name__,url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def handle_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(
            {"id": planet.id, 
            "name": planet.name,
            "diameter": planet.diameter,
            "moons": planet.moons,
            "picture": planet.picture})
    return jsonify(planets_response), 200
    

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    for planet in planets:
        if planet.id == int(planet_id):
            return {
                "id": planet.id,
                "title": planet.title,
                "description": planet.description,
                "moon":planet.moon, 
                "picture": planet.picture
                }

@planets_bp.route("/picture/<planet_id>", methods=["GET"])
def handle_planet_picture(planet_id):
    for planet in planets:
        if planet.id == int(planet_id):
            return render_template('planet_picture.html', url=planet.picture)

@planets_bp.route("/picturesummary/<planet_id>", methods=["GET"])
def handle_planet_summary(planet_id):
    for planet in planets:
        if planet.id == int(planet_id):
            if planet.moon == True:
                moon = "Yes"
            else:
                moon = "No"
            return render_template('planet_summary.html', 
                    url=planet.picture, 
                    title=planet.title,
                    diameter=planet.description,
                    moon=moon)

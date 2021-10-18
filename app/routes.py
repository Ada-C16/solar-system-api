from flask import Blueprint, jsonify

solarsystem_bp = Blueprint("solarsystem", __name__, url_prefix="/solarsystem")

class SolarSystem:
    def __init__(self, name, surface_area, orbital_period, distance_from_sun, radius):
        self.name = name
        # self.has_ring = True
        self.surface_area = surface_area 
        self.orbital_period = orbital_period
        self.distance_from_sun = distance_from_sun
        self.radius = radius

 
planets = [
     SolarSystem("Mercury", "28.88 million mi²", "88 days", 57900000, "1,516 mi"),
     SolarSystem("Venus", "177.7 million mi²", "225 days", 108200000, "3,760.4 mi"),
     SolarSystem("Earth", "196.9 million mi²", "365 days", 149600000, "3,958.8 mi"),
     SolarSystem("Mars", "55.91 million mi²", "687 days", 227900000,  "2,106.1 mi"),
     SolarSystem("Jupiter", "23.71 billion mi²", "12 years", 778600000, "43,441 mi"),
     SolarSystem("Saturn", "36,184 mi", "29 years", 1433500000, "36,184 mi"),
     SolarSystem("Uranus", "3.121 billion mi²", "84 years", 2872500000, "15,759 mi"),
     SolarSystem("Neptune", "2.941 billion mi²", "165 years", 4495100000, "15,299 mi")
 ]

         
@solarsystem_bp.route("", methods=["GET"])
def handle_solarsystem():
    solarsystem_response = []
    for planet in planets:
        solarsystem_response.append({
            "name": planet.name,
            "surface_area": planet.surface_area,
            "orbital_period": planet.orbital_period,
            "distance_from_sun": planet.distance_from_sun,
            "radius": planet.radius
        })
    return jsonify(solarsystem_response)  


@solarsystem_bp.route("/<name>", methods=["GET"])
def handle_planet(name):
    for planet in planets:
        if planet.name == name:
            return {
                "name": planet.name,
                "surface_area": planet.surface_area,
                "orbital_period": planet.orbital_period,
                "distance_from_sun": planet.distance_from_sun,
                "radius": planet.radius
            }


@solarsystem_bp.route("/<distance_from_sun>", methods=["GET"])
def handle_planet(name):
    
    for planet in planets:
        max_distance = max(planet.distance_from_sun)
        # farest_planet = None
        if planet.distance_from_sun == max_distance:
            return {
                "name": planet.name,
                "surface_area": planet.surface_area,
                "orbital_period": planet.orbital_period,
                "distance_from_sun": planet.distance_from_sun,
                "radius": planet.radius
            }         
        
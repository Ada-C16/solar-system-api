from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size

planets = [
    Planet(1, "Mercury", "closest planet to the sun", "1,516 mi radius"),
    Planet(2, "Venus", "the girl planet", "3,760 mi radius"),
    Planet(3, "Earth", "our planet", "3,959 mi radius"),
    Planet(4, "Mars", "the red planet", "2,106 mi radius"),
    Planet(5, "Jupiter", "the largest planet", "43,441 mi radius"),
    Planet(6, "Saturn", "the ringed plannet", "36,184 mi radius"),
    Planet(7, "Uranus", "BAHAHFABA UR ANUS", "15,759 mi radius"),
    Planet(8, "Neptune", "Pharrell's music group", "15,299 mi radius")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
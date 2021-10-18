from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, matter):
        self.id = id
        self.name = name
        self.description = description
        self.matter = matter


planets = [Planet(1, "Mercury", "small and red", "solid"),     Planet(5, "Jupiter", "big and swirly", "gaseous"), 
Planet(6, "Saturn", "rings and swirls", "gaseous")]


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")











from flask import Blueprint, jsonify

planets_bp = Blueprint('planets', __name__, url_prefix = '/planets')


class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color
    

planets = [Planet(1, 'Mars', '3rd planet from the sun', 'Red'), Planet(2, 'Jupiter', 'the largest planet in our solar system', 'Blue'), Planet(3, 'Venus', '2nd closest to the sun', 'Pink')]


@planets_bp.route('', methods = ['GET'])       
def get_all_planets():
    all_planets = []
    for planet in planets:
        all_planets.append({'id': planet.id,'name': planet.name, 'description':planet.description, 'color': planet.color} )
    return jsonify(all_planets)


@planets_bp.route('/<planet_name>', methods = ['GET'])
def get_specific_planet(planet_name):
    for planet in planets:
        if planet.name == planet_name:
            return {'id': planet.id,'name': planet.name, 'description':planet.description, 'color': planet.color}
        
    return 'Planet not found'
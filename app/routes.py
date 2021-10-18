from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

planets = [
    Planet('4fr', 'Earth', 'Only known life planet', 'blue'),
    Planet('6rw', 'Neptune', 'The farthest known planet from the Sun', 'blue'),
    Planet('ty6', 'Saturn', 'Sixth planet from the Sun', 'yellow'),
    Planet('48t', 'Mars', 'Fourth planet from the Sun. Colonization in process', 'red')
]

planet_bp = Blueprint('planets', __name__, url_prefix='/planets')

@planet_bp.route('', methods=['GET'])
def handle_planets():
    planets_response = list()

    for planet in planets:
        planets_response.append({
            'id': planet.id,
            'name': planet.name,
            'description': planet.description,
            'color': planet.color
        })
    return jsonify(planets_response)
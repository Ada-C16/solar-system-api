from flask import Blueprint, jsonify

# class Planet:
#     def __init__(self, id, name, description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'description': self.description,
#             'color': self.color
#             }

# planets = [
#     Planet('4fr', 'Earth', 'Only known life planet', 'blue'),
#     Planet('6rw', 'Neptune', 'The farthest known planet from the Sun', 'blue'),
#     Planet('ty6', 'Saturn', 'Sixth planet from the Sun', 'yellow'),
#     Planet('48t', 'Mars', 'Fourth planet from the Sun. Colonization in process', 'red')
# ]

planet_bp = Blueprint('planets', __name__, url_prefix='/planets')

@planet_bp.route('', methods=['GET'])
def handle_planets():
    planets_response = list()

    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)

@planet_bp.route('/<id>', methods=['GET'])
def handle_single_planet(id):
    for planet in planets:
        if planet.id == id:
            return jsonify(planet.to_dict())
    return 'Error: Planet ID not Found'    


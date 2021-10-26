from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.planet import Planet

planet_bp = Blueprint('planets', __name__, url_prefix='/planets')

@planet_bp.route('', methods=['POST', 'GET'])
def handle_planets():
    if request.method == 'POST':
        request_body = request.get_json()
        planet_to_add = Planet(
            name=request_body['name'],
            description=request_body['description'],
            color=request_body['color'])
        
        db.session.add(planet_to_add)
        db.session.commit()

        return make_response(f'Planet {planet_to_add.name} successfully created', 201)
    elif request.method == 'GET':
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append(planet.to_dict())
        return jsonify(planets_response)

# @planet_bp.route('/<id>', methods=['GET'])
# def handle_single_planet(id):
#     for planet in planets:
#         if planet.id == id:
#             return jsonify(planet.to_dict())
#     return 'Error: Planet ID not Found'    


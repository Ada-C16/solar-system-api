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

        return make_response(jsonify(planets_response), 200)

@planet_bp.route('/<id>', methods=['GET', 'PUT'])
def handle_single_planet(id):
    planet = Planet.query.get(id)
    if not planet:
            return make_response(f'Planet not found', 404)
            
    if request.method == 'GET':
        response_body = planet.to_dict()
        return make_response(jsonify(response_body), 200)
    elif request.method == 'PUT':
        request_body = requet.get_json()
        planet.name=request_body["name"]
        planet.description=request_body["description"]
        planet.color=request_body["description"]

        return make_response(f"Planet id {planet.id} updated successfully", 200)
    elif request.method == 'DELETE':
        db.session.delete(planet)
        db.session.commit()

        return make_response(f'Planet id {id} destroyed completely', 204)



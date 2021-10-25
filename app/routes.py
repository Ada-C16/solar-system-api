from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

# path = "https://api.le-systeme-solaire.net/rest.php/bodies"


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append(
                {
                    "id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "color": planet.color
                }
            )
        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                            description=request_body["description"],
                            color=request_body["color"]
                            )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    
    planet = Planet.query.get(planet_id)
    #this is where we tell it which id to grab

    if planet is None:
        return make_response(f"Planet {planet.id} not found", 404)

    if request.method == "GET":
        return {  # we're returning a json object using the planet that we found
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
        }
    elif request.method == "PUT":
        request_body = request.get_json()
        
        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.color = request_body["color"]

        db.session.commit()

        return jsonify(f"Planet #{planet.id} successfully updated"), 200

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return jsonify(f"Planet #{planet.id} successfully deleted"), 200



"""
@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
            }

def get_bodies():
    query_params = {
            "filter[]": "isPlanet,neq,false",
            "data": "englishName"
        }

    response = requests.get(path, params=query_params)
    return response.json()


print(get_bodies())

"""

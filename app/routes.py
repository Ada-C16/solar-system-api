from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")
bodies_bp = Blueprint("bodies", __name__, url_prefix="/bodies")

@planets_bp.route("", methods=["POST", "GET"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        print(request_body)
        if "name" not in request_body:
            return make_response("Invalid Request", 400)

        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            distance=request_body["distance"]
        )
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} was successfully created", 201)

    elif request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append(
                {
                    "name": planet.name,
                    "description": planet.description,
                    "distance": planet.distance
                }
            )
        return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):

    planet = Planet.query.get(planet_id)

    if planet is None:
        return make_response(f"Planet {planet_id} not found", 404)
    
    return {
        "name": planet.name,
        "description": planet.description,
        "distance": planet.distance
    }


# PATH = "https://api.le-systeme-solaire.net/rest/bodies?filter[]%3D=isPlanet,neq,false"


# @bodies_bp.route("", methods = ["GET"])
# def get_bodies():
#     i = 0
#     bodies_dict = {}
#     response = requests.get(PATH)
#     response_bodies = response.json()
#     for body in response_bodies["bodies"]:
#         bodies_dict[i] = {
#             "id": body["id"],
#             "english_name": body["englishName"],
#             "is_planet": body["isPlanet"]
#         }
#         i +=1
#     return bodies_dict

# @bodies_bp.route("/<id>", methods = ["GET"])
# def get_body_id(id):
#     id = str(id.lower())
#     response = requests.get(PATH)
#     response_bodies = response.json()
#     for body in response_bodies["bodies"]:
#         if id == body["id"] or id == body["englishName"]:
#             return jsonify(body)
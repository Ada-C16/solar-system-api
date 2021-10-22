from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

planets_bp = Blueprint('planets',__name__, url_prefix="/planets")
@planets_bp.route("", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.title} successfully created", 201)

# class Planets:
#     def __init__(self, id, name, description, attribute):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.add_attribute = attribute

# planets_list = [

# Planets(1,"Saturn","Ring System: Yes", "AVG Temp = -140C"),
# Planets(2,"Venus","Ring System: No", "AVG Temp = 464C"),
# Planets(3,"Uranus","Ring System: Yes", "AVG Temp = -195C"),
# Planets(4,"Earth","Ring System: Yes", "AVG Temp = 15C"),
# Planets(5,"Mars","Ring System: No", "AVG Temp = -65C"),
# Planets(6,"Jupiter","Ring System: Yes", "AVG Temp = -110C"),
# Planets(7,"Neptune","Ring System: Yes", "AVG Temp = -200C")

# ]



# @planets_bp.route("", methods=["GET"])
# def handle_planets():
#     planets_response=[]
#     for planet in planets_list:
#         planets_response.append(
#             {"id": planet.id,
#             "name": planet.name,
#             "description":planet.description,
#             "additional_attribute":planet.add_attribute
#         }
#         )
#     return jsonify(planets_response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet_id=int(planet_id)

#     for planet in planets_list:
#         if planet.id==planet_id:
#             return{
#             "id": planet.id,
#             "name": planet.name,
#             "description":planet.description,
#             "additional_attribute":planet.add_attribute
#             }
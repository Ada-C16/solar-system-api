from flask import Blueprint,jsonify

solarsystem_bp = Blueprint("solarsystem", __name__, url_prefix="/solarsystem")

class SolarSysten:
    def __init__(self, name,distance):
        self.name = name
        self.has_ring = True
        self.distance = distance
        
 @solarsystem_bp.route("solarsystem", methods=["GET"])
 
 planets = [
     SolarSysten("Mercury",False,0.39)
     
 ]
def handle_solarsystem():
    solarsystem_response = []
    for planet in SolarSysten:
        solarsystem_response.append({
            
        })
    return jsonify(solarsystem_response)       
        
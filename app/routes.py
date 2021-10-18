from flask import Blueprint

solarsystem_bp = Blueprint("solarsystem", __name__, url_prefix="/solarsystem")

class SolarSysten:
    def __init__(self, name,description):
        self.name = name
        self.has_ring = True
        self.description = description
        
 @solarsystem_bp.route("solarsystem", methods=["GET"])
 
 planets = [
     SolarSystem()
 ]
def handle_solarsystem():
    solarsystem_response = []
    for planet in solarsystem:
        solarsystem_response.append({
            
        })
    return jsonify(solarsystem_response)       
        
from flask import Blueprint, jsonify, render_template, make_response, request
from app import db
from app.models.planet import Planet


planets_bp = Blueprint("planets_bp", __name__,url_prefix="/planets")


@planets_bp.route("", methods = ["GET"])
def handle_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response), 200
    

@planets_bp.route("/<planet_id>", methods=["GET", "PATCH", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet_id = int(planet_id)
    planet = Planet.query.get(planet_id)
    if request.method == "GET":
        if planet:
            
            return (planet.to_dict()),200
        
        return { "Error": f"Planet {planet_id} was not found"}, 404
    
    elif request.method == "PATCH":
        form_data = request.get_json()
        try:
            planet.name = form_data["name"]
        except KeyError:
            pass
        try:
            planet.diameter = form_data["diameter"]
        except KeyError:
            pass
        try:
            planet.moons = form_data["moons"]
        except KeyError:
            pass
        try:
            planet.picture = form_data["picture"]
        except KeyError:
            pass
        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated")
    
    elif request.method == "PUT":
        form_data = request.get_json()
        planet.name = form_data["name"]
        planet.diameter = form_data["diameter"]
        planet.moons = form_data["moons"]
        planet.picture = form_data["picture"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated")
    
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        
        return {
            "message": f"Planet with title {planet.name} has been deleted"
        }, 200
    

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_data = request.get_json()

    if "name" not in request_data or "moons" not in request_data \
        or "diameter" not in request_data or "picture" not in request_data:
        
        return jsonify({"message": "Missing data"}), 400
    
    new_planet = Planet(name=request_data["name"], diameter=request_data["diameter"], 
                moons=request_data["moons"], picture=request_data["picture"])

    db.session.add(new_planet)
    db.session.commit()

    return f"Planet {new_planet.name} created", 201


@planets_bp.route("/picture/<planet_id>", methods=["GET"])
def handle_planet_picture(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        
        return render_template('planet_picture.html', url=planet.picture)
    
    return jsonify({"message": "Planet does not exist"}), 400


@planets_bp.route("/picturesummary/<planet_id>", methods=["GET"])
def handle_planet_summary(planet_id):
    planet = Planet.query.get(planet_id)
    if planet.moons == True:
        moon = "Yes"
    else:
        moon = "No"
    
    return render_template('planet_summary.html', 
                    url=planet.picture, 
                    title=planet.name,
                    diameter=planet.diameter,
                    moon=moon)

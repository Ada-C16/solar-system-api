from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    distance = db.Column(db.String)


# class Planet:
#     def __init__(self, id, name, description, distance):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.distance = distance

# planets = [
#     Planet(1, "Mercury", "Hot, but not too hot for ice", "Innermost planet, closest to the Sun"),
#     Planet(2, "Venus", "The gassy one", "Inner planet, Earth's neighbor"),
#     Planet(3, "Earth", "Blue and green rock where we exist", "Inner solar system, Goldilocks"),
#     Planet(4, "Mars", "The red planet", "Inner part of solar system"),
#     Planet(5, "Jupiter", "The giant planet", "Outer part of the solar system"),
#     Planet(6, "Saturn", "The one with all of the (most visible) rings", "Outter part of the solar system"), 
#     Planet(7, "Uranus", "The lazy one that rotates on it's side", "Outter part of the solar system"),
#     Planet(8, "Neptune", "Named after it's beautiful blue color, but not discovered by sight, instead by mathematical calculations", "Outter part of the solar syatem"),
#     Planet(9, "Pluto", "The no-longer a planet, planet", "The outer, outer limits")
# ]

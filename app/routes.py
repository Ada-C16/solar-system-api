from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, distance):
        self.id = id
        self.name = name
        self.description = description
        self.distance = distance

planets = [
    Planet(1, "Mars", "The red planet", "Inner part of solar system"),
    Planet(2, "Jupiter", "The giant planet", "Outer part of the solar system"),
    Planet(3, "Pluto", "The no-longer a planet, planet", "The outer, outer limits"),
    Planet(4, "Venus", "The gassy one", "Inner planet, Earth's neighbor")
]
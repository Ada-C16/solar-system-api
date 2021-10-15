from flask import Blueprint


class Planet:
    def __init__(self, id, name, description, color):
        self.planet_id = id
        self.name = name
        self.description = description
        self.color = color
    

planets = [Planet(1, 'Mars', '3rd planet from the sun', 'Red'), Planet(2, 'Jupiter', 'the largest planet in our solar system', 'Blue'), Planet(3, 'Venus', '2nd closest to the sun', 'Pink')]
        


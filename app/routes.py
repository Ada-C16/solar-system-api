from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, color):
        self.id=id
        self.name=name
        self.description=description
        self.color=color

planets=[
    Planet(1,"Sun", "center of the solar system", "orange"),
    Planet(2, "Saturn", "it takes approx 29.5 years to complete its orbit","yellow"),
    Planet(3, "Mercury", "rules communication", "light grey")
]
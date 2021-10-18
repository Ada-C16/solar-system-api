from flask import Blueprint

class Planets:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color


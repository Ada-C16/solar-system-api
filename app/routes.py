from flask import Blueprint


class Planet():
    def __init__(self, id, name, description, xenomorphs=None):
        self.id = id
        self.name = name
        self.description = description
        self.xenomorphs = xenomorphs


PLANETS = [

]

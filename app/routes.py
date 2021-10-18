from flask import Blueprint, jasonify

class Planet:
    def __init__(self, id , name , description , moons):
        self.id = id 
        self.name = name
        self.description = description
        self.moons = moons

planets = [
    Planet(1,"earth","our world",["Moon"]),
    Planet(2,"mars","The red planet",["Phobos","Deimos"]),
    Planet(3,"jupiter", "The biggest one",["Lo","Europa","Callisto","Gayemede"])
    
]


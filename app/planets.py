# Define the class 
# Create an init
# Class variable that is number of planets (ID)
# Parameters of init = self, name, description, has_moons = boolean
# Inside init: set variables, call update number of planets, set id = number of planets
# Class method: update number of planets

class Planet:
    number_of_planets = 0
    def __init__(self, name, description, has_moons=True):
        self.name = name
        self.description = description
        self.has_moons = has_moons
        self.id = Planet.number_of_planets 
        Planet.increase_number_of_planets()

    @classmethod
    def increase_number_of_planets(Planet):
        Planet.number_of_planets += 1
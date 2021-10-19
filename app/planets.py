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

    def create_planet_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "has moons": self.has_moons
        }
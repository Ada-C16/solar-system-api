# create a list of planets array
# fill out name, description, has moons boolean
from planets import Planet

planets = [
    Planet("Mercury", "Closest to the sun, hot.", False),
    Planet("Venus", "Spins the opposite direction of other planets.", False),
    Planet("Earth", "You are here."),
    Planet("Mars", "Red planet."),
    Planet("Jupiter", "Gas Giant."),
    Planet("Saturn", "Has rings."),
    Planet("Uranus", "Controversy over pronunciation"),
    Planet("Neptune", "Smallest gas giant, with faint rings."),
    Planet("Pluto", "Brooke still believes!")
]

for planet in planets:
    print(planet.create_planet_dictionary())
from flask import Blueprint

from .planet import Planet

planets = [
    Planet(1, "Mars", "Red Planet", ["Phobos", "Deimos"]),
    Planet(2, "Earth", "Blue Marbel", ["Luna"]),
    Planet(3, "Pluto", "It IS a planet!", ["Charon", "Nix", "Hydra", "Kerberos", "Styx"]),
    Planet(4, "Venus", "She's Pretty", [])
]

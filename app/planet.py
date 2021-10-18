class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

    def to_dict(self):
        if not self.moons:
            moons = "NO moons"
        else:
            moons = self.moons

        return {
            "id":self.id,
            "name":self.name,
            "description":self.description,
            "moons":moons
        }
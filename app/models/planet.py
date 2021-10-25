from app import routes

class Planet:
    def __init__(self, id, name, description, matter):
        self.id = id
        self.name = name
        self.description = description
        self.matter = matter
    
    def make_dict(self):
        return {"id": self.id,
        "name": self.name,
        "description": self.description,
        "matter": self.matter}
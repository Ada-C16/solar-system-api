from app import db
#"This is where we CREATE OUR PLANET! (class)"

class Planet():
    def __init__(self, id, name, description, xenomorphs=False):
        self.id = id
        self.name = name
        self.description = description
        self.xenomorphs = xenomorphs

    def to_json(self):
        json_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "xenomorphs": self.xenomorphs
        }
        return json_dict
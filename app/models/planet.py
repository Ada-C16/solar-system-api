from app import db
#"This is where we CREATE OUR PLANET! (class)"

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String) 
    xenomorphs = db.Column(db.Boolean) 

    def to_json(self):
        json_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "xenomorphs": self.xenomorphs
        }
        return json_dict
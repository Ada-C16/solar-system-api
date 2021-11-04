from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name= db.Column(db.String)
    description = db.Column(db.String)
    has_moons = db.Column(db.Boolean)

    def to_json(self):
        return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "has_moons": self.has_moons
    }
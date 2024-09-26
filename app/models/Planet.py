from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    biggest_moon = db.Column(db.String)

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "description": self.description,
            "biggest_moon": self.biggest_moon
        }
from app import db

class Planet(db.Model):
    __tablename__ = "Planets"
    id = db.Column(db.Integer,primary_key=True,autoincrement = True)
    name = db.Column(db.String)
    diameter = db.Column(db.String)
    moons = db.Column(db.Boolean)
    picture = db.Column(db.String)

    def to_dict(self):
        return ({"id": self.id, 
                "name": self.name,
                "diameter": self.diameter,
                "moons": self.moons,
                "picture": self.picture})
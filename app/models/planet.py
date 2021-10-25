from app import db

class Planet(db.Model):
    __name__ = 'planets'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.Column(db.String)
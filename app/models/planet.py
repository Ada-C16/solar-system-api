from app import db

class Planet(bd.Model):

    id = bd.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String
    distance = db.Column(db.String)
from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    name = db.Column(db.String(64))
    surface_area= db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    distance_from_sun = db.Column(db.Integer)
    radius = db.Column(db.Integer)
    
    
    
    
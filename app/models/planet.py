from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    name = db.Column(db.String(64))
    surface_area= db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    distance_from_sun = db.Column(db.Integer)
    radius = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'surface_area':self.surface_area,
            'orbital_period':self.orbital_period,
            'distance_from_sun':self.distance_from_sun,
            'radius':self.radius  
        }


    
    
    
    
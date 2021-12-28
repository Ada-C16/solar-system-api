from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    name = db.Column(db.String)
    description = db.Column(db.String)
    oxygen_level = db.Column(db.String)
    #__tablename__ = "planets" we can reset the default table name SQLA sets using this line

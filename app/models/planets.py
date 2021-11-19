from app import db
# class Planet:
#     def __init__(self, id, name, description, oxygen):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.oxygen = oxygen

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    name = db.Column(db.String)
    description = db.Column(db.String)
    oxygen_level = db.Column(db.String)
    #__tablename__ = "planets" we can reset the default table name SQLA sets using this line

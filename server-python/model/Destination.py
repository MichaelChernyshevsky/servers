from config.extensions import db

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    parent_id = db.Column(db.Integer,db.ForeignKey('destination.id'))
    is_active = db.Column(db.Boolean, default=True)
  

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_active': self.is_active,
            'parent_id': self.parent_id
        }
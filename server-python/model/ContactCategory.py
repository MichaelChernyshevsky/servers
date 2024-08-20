from config.extensions import db

class ContactCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(500))
  

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
from config.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250))
    has_car = db.Column(db.Boolean)
    has_children = db.Column(db.Boolean)
    citizenship_id = db.Column(db.Integer,db.ForeignKey('citizenship.id'))
    destination_id = db.Column(db.Integer,db.ForeignKey('destination.id'))

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'has_car': self.has_car,
            'has_children': self.has_children,
            'citizenship_id': self.citizenship_id,
            'destination_id': self.destination_id,
        }
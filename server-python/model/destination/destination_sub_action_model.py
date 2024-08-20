from services.db_service import db

class DestinationSubActionModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destinationActionId = db.Column(db.Integer)
    field = db.Column(db.String(500))


  

    def serialize(self):
        return {
            'id': self.id,
            'destinationActionId': self.destinationActionId,
            'field': self.field,
        }
from services.db_service import db

class DestinationActionModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destinationId = db.Column(db.Integer,db.ForeignKey('destination_model.id'))
    field = db.Column(db.String(500))


  

    def serialize(self):
        return {
            'id': self.id,
            'destinationId': self.destinationId,
            'field': self.field,
        }
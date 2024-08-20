from services.db_service import db

class DestinationStayInfoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    availableDays = db.Column(db.Integer)
    touristDays = db.Column(db.Integer)
    destinationId = db.Column(db.Integer,db.ForeignKey('destination_model.id'))


  

    def serialize(self):
        return {
            'id': self.id,
            'availableDays': self.availableDays,
            'touristDays': self.touristDays,
            'destinationId': self.destinationId,
        }
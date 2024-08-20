from services.db_service import db

class UserDestinationHistoryModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entryDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    previousDestination = db.Column(db.Integer)
    currentDestination = db.Column(db.Integer)
    userId = db.Column(db.Integer)
    leaveDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    type = db.Column(db.String(250))



    def serialize(self):
        return {
            'id': self.id,
            'entryDate': self.entryDate,
            'previousDestination': self.previousDestination,
            'currentDestination': self.currentDestination,
            'userId': self.userId,
            'leaveDate': self.leaveDate,
            'type': self.type,
        }
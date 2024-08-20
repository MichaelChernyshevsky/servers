from services.db_service import db

class UserActionModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,db.ForeignKey('user_model.id'))
    destinationActionId = db.Column(db.Integer)

   

    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'destinationActionId': self.destinationActionId,
        } 
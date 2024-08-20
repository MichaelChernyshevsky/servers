from services.db_service import db

class UserSubActionodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destinationSubActionId = db.Column(db.Integer,db.ForeignKey('destinatoin_sub_action_model.id'))
    isActive = db.Column(db.Boolean)


   

    def serialize(self):
        return {
            'id': self.id,
            'destinationSubActionId': self.destinationSubActionId,
            'isActive': self.isActive,

        } 
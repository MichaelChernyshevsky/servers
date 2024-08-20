from services.db_service import db

class DestinationSubActionTypeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destinationSubActionId = db.Column(db.Integer,db.ForeignKey('destination_sub_action_model.id'))
    info = db.Column(db.String(500))


  

    def serialize(self):
        return {
            'id': self.id,
            'destinationSubActionId': self.destinationSubActionId,
            'info': self.info,
        }
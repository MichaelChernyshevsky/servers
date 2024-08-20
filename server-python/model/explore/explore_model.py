from services.db_service import db

class ExploreModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descriptionId = db.Column(db.Integer)
    info = db.Column(db.String(250))

  

    def serialize(self):
        return {
            'id': self.id,
            'descriptionId': self.descriptionId,
            'info': self.info,
           
        }
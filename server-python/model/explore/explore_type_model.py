from services.db_service import db

class ExploreTypeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    isPremium = db.Column(db.Boolean)

  

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'isPremium': self.isPremium,
        }
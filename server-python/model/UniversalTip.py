from config.extensions import db

class UniversalTipInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    info = db.Column(db.String(500))
  

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'info': self.info,
        }
from config.extensions import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer,db.ForeignKey('contact_category.id'))
    category = db.relationship('ContactCategory', backref='contacts')
    phone = db.Column(db.String(250))
    is_SOS = db.Column(db.Boolean)
    destination_id = db.Column(db.Integer,db.ForeignKey('destination.id'))
    name = db.Column(db.String(250))
    notes = db.Column(db.String(500))
    geolocation = db.Column(db.String(250))
    chat = db.Column(db.String(250))
    cover = db.Column(db.String(750))
    latitude = db.Column(db.String(250))
    longitude = db.Column(db.String(250))
    icon = db.Column(db.String(750))
    marker = db.Column(db.String(750))

    def serialize(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'category': self.category.serialize(),
            'phone': self.phone,
            'is_SOS': self.is_SOS,
            'destination_id': self.destination_id,
            'name': self.name,
            'notes': self.notes,
            'geolocation': self.geolocation,
            'chat': self.chat,
            'cover': self.cover,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'icon': self.icon,
            'marker': self.marker            
        }
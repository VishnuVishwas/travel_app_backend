# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# places data model
class Place(db.Model):
    __tablename__ = 'places'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    description = db.Column(db.Text)
    is_favorite = db.Column(db.Integer, default=0)
    rating = db.Column(db.Float, default=0.0)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'description': self.description,
            'is_favorite': self.is_favorite,
            'rating': self.rating
        }

# photos db model
class Photo(db.Model):
    __tablename__ = 'photos' 
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'), nullable=False)  # Referencing the correct table
    photo_url = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'place_id': self.place_id,
            'photo_url': self.photo_url
        }

# bookings db model
class Booking(db.Model):
    __tablename__ = 'bookings'  
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'), nullable=False)  # Referencing the correct table
    booking_date = db.Column(db.String(20))
    number_of_people = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'booking_date': self.booking_date,
            'number_of_people': self.number_of_people
        }

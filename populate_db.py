# populate_db.py

from app import app
from models import db, Place, Photo, Booking

with app.app_context():
    # Create sample data
    place = Place(name="Shri Krishna Temple", address="Udupi", latitude=13.341, longitude=74.785, description="A famous temple in Udupi.", is_favorite=0, rating=4.5)
    db.session.add(place)
    db.session.commit()

    # Add a photo for the place
    photo = Photo(place_id=place.id, photo_url="path/to/photo.jpg")
    db.session.add(photo)
    db.session.commit()

    # Create a booking
    booking = Booking(user_id=1, place_id=place.id, booking_date="2024-09-20", number_of_people=2)
    db.session.add(booking)
    db.session.commit()

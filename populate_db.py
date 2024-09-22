from app import app
from models import db, Place, Photo, Booking, User

with app.app_context():
    # Create sample users
    user1 = User(name="Vishnu Vishwas", email="vishnuvishwas@gmail.com", profile_picture_url="https://drive.google.com/file/d/1My2pSvMx1Kd1B1zxuD14UB_CkdGZXe2h/view?usp=sharing")
    user2 = User(name="Satoru Gojo", email="gojo@gmail.com", profile_picture_url="https://drive.google.com/file/d/1qGZNpcvKHq_IyyPwi63fbXMvLVQvfbTS/view?usp=sharing")
    db.session.add_all([user1, user2])
    db.session.commit()

    # Create sample place data
    place = Place(
        name="Shri Krishna Temple", 
        address="Udupi", 
        latitude=13.341, 
        longitude=74.785, 
        description="A famous temple in Udupi.", 
        is_favorite=0, 
        rating=4.5
    )
    db.session.add(place)
    db.session.commit()

    # Add a photo for the place
    photo = Photo(
        place_id=place.id, 
        photo_url="path/to/photo.jpg"
    )
    db.session.add(photo)
    db.session.commit()

    # Create bookings for the users
    booking1 = Booking(
        user_id=user1.id, 
        place_id=place.id, 
        booking_date="2024-09-20", 
        number_of_people=2
    )
    booking2 = Booking(
        user_id=user2.id, 
        place_id=place.id, 
        booking_date="2024-09-21", 
        number_of_people=4
    )
    db.session.add_all([booking1, booking2])
    db.session.commit()

    print("Sample data added successfully!")

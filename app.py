from flask import Flask, request, jsonify
from models import db, Place, Photo, Booking, User
import config
from sqlalchemy import inspect

app = Flask(__name__)
app.config.from_object(config.Config)

# Initialize SQLAlchemy with Flask
db.init_app(app)

# Create tables if they don't exist
with app.app_context():
        db.create_all()

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Udupi Insights API!'})



# **Places Endpoints**
# get all places
@app.route('/places', methods=['GET'])
def get_places():
    places = Place.query.all()
    return jsonify([place.to_dict() for place in places])

# get place by id
@app.route('/places/<int:id>', methods=['GET'])
def get_place(id):
    place = Place.query.get_or_404(id)
    photos = Photo.query.filter_by(place_id=id).all()
    place_data = place.to_dict()
    place_data['photos'] = [photo.to_dict() for photo in photos]
    return jsonify(place_data)

# post a place
@app.route('/places', methods=['POST'])
def add_place():
    data = request.json
    new_place = Place(
        name=data['name'],
        address=data['address'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        description=data['description'],
        is_favorite=data.get('is_favorite', 0),
        rating=data.get('rating', 0.0)
    )
    db.session.add(new_place)
    db.session.commit()
    return jsonify(new_place.to_dict()), 201

# update place
@app.route('/places/<int:id>', methods=['PUT'])
def update_place(id):
    data = request.json
    place = Place.query.get_or_404(id)
    place.name = data.get('name', place.name)
    place.address = data.get('address', place.address)
    place.latitude = data.get('latitude', place.latitude)
    place.longitude = data.get('longitude', place.longitude)
    place.description = data.get('description', place.description)
    place.is_favorite = data.get('is_favorite', place.is_favorite)
    place.rating = data.get('rating', place.rating)
    db.session.commit()
    return jsonify(place.to_dict())

# delete place
@app.route('/places/<int:id>', methods=['DELETE'])
def delete_place(id):
    place = Place.query.get_or_404(id)
    db.session.delete(place)
    db.session.commit()
    return jsonify({'message': 'Place deleted successfully!'})

# favorite place
@app.route('/places/<int:id>/favorite', methods=['POST'])
def toggle_favorite(id):
    place = Place.query.get_or_404(id)
    place.is_favorite = 1 - place.is_favorite  # Toggle favorite status
    db.session.commit()
    return jsonify(place.to_dict())




# **Photos Endpoints**
# get all photos 
@app.route('/photos', methods=['GET'])
def get_photos():
    photos = Photo.query.all()
    return jsonify([photo.to_dict() for photo in photos])

# get photo by id
@app.route('/photos/<int:id>', methods=['GET'])
def get_photo(id):
    photo = Photo.query.get_or_404(id)
    return jsonify(photo.to_dict())

# post photo
@app.route('/photos', methods=['POST'])
def add_photo():
    data = request.json
    new_photo = Photo(
        place_id=data['place_id'],
        photo_url=data['photo_url']
    )
    db.session.add(new_photo)
    db.session.commit()
    return jsonify(new_photo.to_dict()), 201

# update photo
@app.route('/photos/<int:id>', methods=['PUT'])
def update_photo(id):
    data = request.json
    photo = Photo.query.get_or_404(id)
    photo.place_id = data.get('place_id', photo.place_id)
    photo.photo_url = data.get('photo_url', photo.photo_url)
    db.session.commit()
    return jsonify(photo.to_dict())

# delete photo
@app.route('/photos/<int:id>', methods=['DELETE'])
def delete_photo(id):
    photo = Photo.query.get_or_404(id)
    db.session.delete(photo)
    db.session.commit()
    return jsonify({'message': 'Photo deleted successfully!'})

# **Bookings Endpoints**
# get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    return jsonify([booking.to_dict() for booking in bookings])

# get booking by id
@app.route('/bookings/<int:id>', methods=['GET'])
def get_booking(id):
    booking = Booking.query.get_or_404(id)
    return jsonify(booking.to_dict())

# post booking
@app.route('/bookings', methods=['POST'])
def add_booking():
    data = request.json
    new_booking = Booking(
        user_id=data['user_id'],
        place_id=data['place_id'],
        booking_date=data['booking_date'],
        number_of_people=data['number_of_people']
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify(new_booking.to_dict()), 201

# update booking
@app.route('/bookings/<int:id>', methods=['PUT'])
def update_booking(id):
    data = request.json
    booking = Booking.query.get_or_404(id)
    booking.user_id = data.get('user_id', booking.user_id)
    booking.place_id = data.get('place_id', booking.place_id)
    booking.booking_date = data.get('booking_date', booking.booking_date)
    booking.number_of_people = data.get('number_of_people', booking.number_of_people)
    db.session.commit()
    return jsonify(booking.to_dict())

# delete booking
@app.route('/bookings/<int:id>', methods=['DELETE'])
def delete_booking(id):
    booking = Booking.query.get_or_404(id)
    db.session.delete(booking)
    db.session.commit()
    return jsonify({'message': 'Booking deleted successfully!'})

# **Users Endpoints**
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(
        name=data['name'],
        email=data['email'],
        profile_picture_url=data['profile_picture_url']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    user = User.query.get_or_404(id)
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.profile_picture_url = data.get('profile_picture_url', user.profile_picture_url)
    db.session.commit()
    return jsonify(user.to_dict())

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
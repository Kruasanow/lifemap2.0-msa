from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    names = db.Column(db.String(150), nullable=False)
    sname = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True, nullable=False)
    passwords = db.Column(db.String(150), nullable=False)
    secrets = db.Column(db.String(150), nullable=False)
    tg = db.Column(db.String(150), unique=True)
    friends = db.Column(db.String(550))
    roles = db.Column(db.String(10), nullable=False)
    comment = db.Column(db.String(250))
    birthday = db.Column(db.String(50))
    register_date = db.Column(db.String(50), nullable=False)
    sex = db.Column(db.String(3), nullable=False)
    phone = db.Column(db.String(12), nullable=False)

class Events(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    locations = db.Column(db.String(150), nullable=False)
    coordinates_latitude = db.Column(db.String(150), nullable=False)
    coordinates_longitude = db.Column(db.String(150), nullable=False)
    img_ways = db.Column(db.String(1050))
    descriptions = db.Column(db.String(500))
    short_description = db.Column(db.String(550))
    story = db.Column(db.String(150), nullable=False)
    privates = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
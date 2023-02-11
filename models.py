from sqlalchemy import Enum
from config import db, app

import uuid
import enum
from datetime import datetime
from hmac import compare_digest


def generate_key():
    return lambda: str(uuid.uuid4())


class User(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_key())
    username = db.Column(db.String(30), nullable=False, unique=True)
    full_name = db.Column(db.String(55), nullable=False)
    password = db.Column(db.String(55), nullable=False)

    def check_password(self, password):
        return compare_digest(password, self.password)


class ColorEnum(enum.Enum):
    blue = "blue"
    gray = "gray"
    yellow = "yellow"

    def __str__(self):
        return self.value


class ModelEnum(enum.Enum):
    convertible = "convertible"
    hatch = "hatch",
    sedan = "sedan"

    def __str__(self):
        return self.value


class Person(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_key())
    name = db.Column(db.String(40))
    phone = db.Column(db.String(30))
    mail = db.Column(db.String(30))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class Vehicle(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_key())
    color = db.Column(db.Enum(ColorEnum), nullable=False)
    model = db.Column(db.Enum(ModelEnum), nullable=False)
    person_id = db.Column(db.String, db.ForeignKey('person.id'), nullable=False)
    person = db.relationship('Person', backref="vehicles", lazy='subquery')
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


with app.app_context():
    db.create_all()
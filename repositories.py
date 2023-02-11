from config import db
from models import Person, Vehicle, User
from abc import ABC, abstractclassmethod
from flask import abort
from sqlalchemy import func


class BaseRepository(ABC):

    @abstractclassmethod
    def query(self, id=None):
        raise NotImplementedError

    @abstractclassmethod
    def store(self, data):
        raise NotImplementedError

    @abstractclassmethod
    def destroy(self, id):
        raise NotImplementedError

    @abstractclassmethod
    def update(self, id, content):
        raise NotImplementedError


class PersonRepository(BaseRepository):
    def query(self, id=None):
        if id:
            return Person.query.filter(Person.id == id).one_or_none()
        else:
            return Person.query.all()

    def store(self, new_person):
        db.session.add(new_person)
        db.session.commit()

        return new_person

    def update(self, id, new_person):
        person = Person.query.filter(Person.id == id).one_or_none()
        if not person:
            abort(404)

        person.name = new_person.name
        person.phone = new_person.phone
        person.mail = new_person.mail
        
        db.session.add(person)
        db.session.commit()
        return person

    def destroy(self, id):
        person = Person.query.filter(Person.id == id).one_or_none()
        if not person:
            abort(404)
        db.session.delete(person)
        db.session.commit()
        return person


class VehicleRepository(BaseRepository):
    def query(self, id=None):
        if id:
            return Vehicle.query.filter(Vehicle.id == id).one_or_none()
        else:
            return Vehicle.query.all()

    def store(self, new_vehicle):
        db.session.add(new_vehicle)
        db.session.commit()

        return new_vehicle

    def update(self, id, new_vehicle):
        vehicle = Vehicle.query.filter(Vehicle.id == id).one_or_none()

        if not vehicle:
            abort(404)
        vehicle.color = new_vehicle.color
        vehicle.model = new_vehicle.model

        db.session.add(vehicle)
        db.session.commit()

        return vehicle

    def destroy(self, id):
        vehicle = Vehicle.query.filter(Vehicle.id == id).one_or_none()
        if not vehicle:
            abort(404)

        db.session.delete(vehicle)
        db.session.commit()
        return vehicle

    def quantity_by_person_id(self, id):
        return db.session.query(func.count(Vehicle.id)) \
            .filter(Vehicle.person_id == id).scalar()


class UserRepository():
    
    def get_user_by_id(self, id):
        return User.query.filter(User.id == id).one_or_none()

    def get_user_by_username(self, username):
        return User.query.filter_by(username=username).one_or_none()

    def store(self, new_user):
        db.session.add(new_user)
        db.session.commit()

        return new_user


person_repository = PersonRepository()
vehicle_repository = VehicleRepository()
user_repository = UserRepository()
import json
from abc import ABC, abstractclassmethod
from flask import abort, jsonify
from flask_jwt_extended import create_access_token

from config import db
from models import Person, Vehicle
from schemas import (person_schema, people_schema, 
    vehicle_schema, vehicles_schema, user_schema)
from repositories import (person_repository, vehicle_repository, user_repository)


class BaseService(ABC):

    def __init__(self, repository):
        self.repository = repository

    @abstractclassmethod
    def query(self, id):
        raise NotImplementedError

    @abstractclassmethod
    def store(self, data):
        raise NotImplementedError

    @abstractclassmethod
    def update(self, id, content):
        raise NotImplementedError

    @abstractclassmethod
    def destroy(self, id):
        raise NotImplemented


class PersonService(BaseService):

    def query(self, id=None):
        if id:
            person = self.repository.query(id)
            return person_schema.dump(person)
        else:
            people = self.repository.query()
            return people_schema.dump(people)

    def store(self, person):
        new_person = person_schema.load(person)
        result = self.repository.store(new_person)
        return person_schema.dump(result)

    def update(self, id, content):
        new_person = person_schema.load(content)
        result = self.repository.update(id, new_person)
        return person_schema.dump(result)
        
    def destroy(self, id):
        result = self.repository.destroy(id)
        return person_schema.dump(result)


class VehicleService(BaseService):

    def query(self, id=None):
        if id:
            vehicle = Vehicle.query.filter(Vehicle.id == id).one_or_none()
            return vehicle_schema.dump(vehicle)
        else:
            vehicles = Vehicle.query.all()
            return vehicles_schema.dump(vehicles)

    def store(self, vehicle):
        new_vehicle = vehicle_schema.load(vehicle)
        count = self.repository.quantity_by_person_id(new_vehicle.person_id)
        if count >= 3:
            abort(404)

        result = self.repository.store(new_vehicle)
        return vehicle_schema.dump(result)

    def update(self, id, content):
        new_vehicle = vehicle_schema.load(content)
        result = self.repository.update(id, new_vehicle)
        return vehicle_schema.dump(result)

    def destroy(self, id):
        result = self.repository.destroy(id)
        return vehicle_schema.dump(result)

    def quantity_by_person_id(self, person_id):
        return self.repository.quantity_by_person_id(person_id)


class UserService():

    def __init__(self, user_repository):
        self.repository = user_repository

    def get_user_by_id(self, id):
        return self.repository.get_user_by_id(id)

    def get_access_token(self, username, password):
        user = self.repository.get_user_by_username(username)
        if not user or not user.check_password(password):
            return jsonify("Wrong username or password!"), 401

        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token)

    def store(self, user):
        new_user = user_schema.load(user)

        result = self.repository.store(new_user)
        return user_schema.dump(result)


person_service = PersonService(person_repository)
vehicle_service = VehicleService(vehicle_repository)
user_service = UserService(user_repository)
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user

from config import app, jwt
from services import (person_service, vehicle_service, user_service)


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return user_service.get_user_by_id(id=identity)


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    return user_service.get_access_token(username=username, password=password)


@app.route("/signup", methods=["POST"])
def signup():
    user = request.json
    return user_service.store(user)


@app.route("/whoami", methods=["GET"])
@jwt_required()
def protected():
    return jsonify(
        id=current_user.id,
        full_name=current_user.full_name,
        username=current_user.username,
    )


@app.route("/", methods=['GET'])
def home():
    return "OK!"


@app.route("/person", methods=['GET'])
@jwt_required()
def get_all_people():
    return person_service.query()


@app.route("/person/<id>", methods=['GET'])
@jwt_required()
def get_person(id):
    return person_service.query(id=id)


@app.route("/person", methods=['POST'])
@jwt_required()
def create_person():
    content = request.json
    return person_service.store(content)


@app.route("/person/<id>", methods=['PATCH'])
@jwt_required()
def update_person(id):
    content = request.json
    return person_service.update(id, content=content)


@app.route("/person/<id>", methods=['DELETE'])
@jwt_required()
def delete_person(id):
    return person_service.destroy(id)


@app.route("/vehicle", methods=['GET'])
@jwt_required()
def get_all_vehicle():
    return vehicle_service.query()


@app.route("/vehicle/<id>", methods=['GET'])
@jwt_required()
def get_vehicle(id):
    return vehicle_service.query(id=id)


@app.route("/vehicle", methods=['POST'])
@jwt_required()
def create_vehicle():
    content = request.json
    return vehicle_service.store(content)


@app.route("/vehicle/<id>", methods=['PATCH'])
@jwt_required()
def update_vehicle(id):
    content = request.json
    return vehicle_service.update(id, content=content)


@app.route("/vehicle/<id>", methods=['DELETE'])
@jwt_required()
def delete_vehicle(id):
    return vehicle_service.destroy(id)
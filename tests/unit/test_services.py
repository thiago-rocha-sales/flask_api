import pytest
from services import user_service, person_service, vehicle_service
from app import user_identity_lookup, user_lookup_callback


def test_create_user(app, user_dict):
    with app.app_context():
        result = user_service.store(user_dict)
        assert result


def test_login_user(app, user_name_and_password):
    with app.app_context():
        username, password = user_name_and_password
        result = user_service.get_access_token(username, password)
        assert result.status_code == 200


def test_create_person(app, person_dict):
    with app.app_context():
        result = person_service.store(person_dict)
        assert result


def test_update_person(app, person_dict, person_id):
    with app.app_context():
        result = person_service.update(person_id, person_dict)
        assert result


def test_delete_person(app, person_id):
    with app.app_context():
        result = person_service.destroy(person_id)
        assert result


def test_query_person(app, person_id):
    with app.app_context():
        result = person_service.query(person_id)
        assert result


def test_create_vehicle(app, vehicle_dict):
    with app.app_context():
        result = vehicle_service.store(vehicle_dict)
        assert result


def test_update_vehicle(app, vehicle_dict, vehicle_id):
    with app.app_context():
        result = vehicle_service.update(vehicle_id, vehicle_dict)
        assert result


def test_delete_vehicle(app, vehicle_id):
    with app.app_context():
        result = vehicle_service.destroy(vehicle_id)
        assert result


def test_query_vehicle(app, vehicle_id):
    with app.app_context():
        result = vehicle_service.query(vehicle_id)
        assert result
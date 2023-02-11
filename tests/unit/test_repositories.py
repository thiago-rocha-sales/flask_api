import pytest
from repositories import user_repository, person_repository, vehicle_repository


def test_create_user(app, user_obj):
    with app.app_context():
        result = user_repository.store(user_obj)
        assert result


def test_create_person(app, person_obj):
    with app.app_context():
        result = person_repository.store(person_obj)
        assert result


def test_delete_person(app, person_id):
    with app.app_context():
        result = person_repository.destroy(person_id)
        assert result


def test_update_person(app, person_id, person_obj):
    with app.app_context():
        result = person_repository.update(person_id, person_obj)
        assert result


def test_get_person(app, person_id):
    with app.app_context():
        result = person_repository.query(person_id)
        assert result


def test_create_vehicle(app, vehicle_obj):
    with app.app_context():
        result = vehicle_repository.store(vehicle_obj)
        assert result


def test_delete_vehicle(app, vehicle_id):
    with app.app_context():
        result = vehicle_repository.destroy(vehicle_id)
        assert result


def test_update_vehicle(app, vehicle_id, vehicle_obj):
    with app.app_context():
        result = vehicle_repository.update(vehicle_id, vehicle_obj)
        assert result


def test_get_vehicle(app, vehicle_id):
    with app.app_context():
        result = vehicle_repository.query(vehicle_id)
        assert result

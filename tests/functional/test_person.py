import pytest
from services import user_service


def test_create_person(client, person_dict, authorization_header):
    with client:
        response = client.post("/person", json=person_dict, headers=authorization_header)
        assert response.status_code == 200


def test_get_person(client, person_id, authorization_header):
    with client:
        response = client.get(f"/person/{person_id}", headers=authorization_header)
        assert response.status_code == 200


def test_update_person(client, person_id, person_dict, authorization_header):
    with client:
        response = client.patch(f"/person/{person_id}", json=person_dict, headers=authorization_header)
        assert response.status_code == 200


def test_delete_person(client, person_id, authorization_header):
    with client:
        response = client.delete(f"/person/{person_id}", headers=authorization_header)
        assert response.status_code == 200
import pytest
from services import vehicle_service


def test_create_vehicle(client, vehicle_dict, authorization_header):
    with client:
        response = client.post("/vehicle", json=vehicle_dict, headers=authorization_header)
        assert response.status_code == 200


def test_get_vehicle(client, vehicle_id, authorization_header):
    with client:
        response = client.get(f"/vehicle/{vehicle_id}", headers=authorization_header)
        assert response.status_code == 200


def test_update_vehicle(client, vehicle_id, vehicle_dict, authorization_header):
    with client:
        response = client.patch(f"/vehicle/{vehicle_id}", json=vehicle_dict, headers=authorization_header)
        assert response.status_code == 200


def test_delete_vehicle(client, vehicle_id, authorization_header):
    with client:
        response = client.delete(f"/vehicle/{vehicle_id}", headers=authorization_header)
        assert response.status_code == 200
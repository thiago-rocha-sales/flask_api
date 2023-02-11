import pytest
import json


def test_signup(client, user_dict):
    with client:
        response = client.post("/signup", json=user_dict)
        assert response.status_code == 200


def test_login(client, user_name_and_password):
    with client:
        username, password = user_name_and_password
        payload = {"username": username, "password": password}
        response = client.post("/login", json=payload)
        assert response.status_code == 200
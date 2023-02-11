import pytest
import json
from faker import Faker
from config import connex_app, db
from models import User, Person, Vehicle
from services import user_service
from repositories import person_repository


faker = Faker()


@pytest.fixture
def app():
    app = connex_app.app
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(scope="module")
def user_obj():
    return User(username=faker.user_name(), 
        full_name=faker.name(), password=faker.password())


@pytest.fixture(scope="module")
def user_dict():
    data = {
        'username': faker.user_name(),
        'full_name': faker.name(),
        'password': faker.password()
    }
    yield data


@pytest.fixture()
def user_id(app):
    with app.app_context():
        user = User(username=faker.user_name(), 
            full_name=faker.name(), password=faker.password())
        db.session.add(user)
        db.session.commit()
        yield user.id


@pytest.fixture()
def user_name_and_password(app):
    with app.app_context():
        user = User(username=faker.user_name(), 
            full_name=faker.name(), password=faker.password())
        db.session.add(user)
        db.session.commit()
        yield (user.username, user.password)


@pytest.fixture()
def authorization_header(user_name_and_password):
    username, password = user_name_and_password
    result = user_service.get_access_token(username=username, password=password)
    token = json.loads(result.response[0].decode("utf-8"))
    yield {"Authorization": f"Bearer {token.get('access_token')}"}


@pytest.fixture
def person_dict():
    return {
        "name": faker.name(), 
        "phone":faker.phone_number(), 
        "mail":faker.email()
    }


@pytest.fixture
def person_obj():
    return Person(name=faker.name(), 
            phone=faker.phone_number(), mail=faker.email())


@pytest.fixture()
def person_id(app):
    with app.app_context():
        person = Person(name=faker.name(), 
            phone=faker.phone_number(), mail=faker.email())
        db.session.add(person)
        db.session.commit()
        yield person.id


@pytest.fixture
def vehicle_dict(person_id):
    return {
        "color": "yellow",
        "model": "sedan",
        "person_id": person_id
    }


@pytest.fixture
def vehicle_obj(app, person_id):
    with app.app_context():
        person = person_repository.query(person_id)
        return Vehicle(color="blue", model="convertible", person=person)


@pytest.fixture
def vehicle_id(app, vehicle_obj):
    with app.app_context():
        vehicle = vehicle_obj
        db.session.add(vehicle)
        db.session.commit()
        return vehicle.id
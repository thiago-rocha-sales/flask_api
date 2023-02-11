from config import ma
from models import Person, Vehicle, ColorEnum, ModelEnum, User
from marshmallow_enum import EnumField


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True

    vehicles = ma.List(ma.Nested(lambda: VehicleSchema(exclude=("person",))), dump_only=True)


class VehicleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vehicle
        include_fk = True
        load_instance = True

    color = EnumField(ColorEnum, required=True)
    model = EnumField(ModelEnum, required=True)
    person = ma.Nested(PersonSchema)


person_schema = PersonSchema()
people_schema = PersonSchema(many=True)

vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)

user_schema = UserSchema()
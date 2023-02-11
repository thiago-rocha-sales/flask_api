from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_jwt_extended import JWTManager

import connexion
import pathlib
import os


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.FlaskApp(__name__, specification_dir=basedir)

app = connex_app.app

app.config["JWT_SECRET_KEY"] = "flask-api-secret"
# app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'database.db'}"
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@db/{DB_DATABASE}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

jwt = JWTManager(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
import os
import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import get_postgres_database_uri


app = Flask(__name__)
db = SQLAlchemy()

if "SQL_DATABASE_TYPE" in os.environ and os.environ["SQL_DATABASE_TYPE"] == "postgres":
    app.config["SQLALCHEMY_DATABASE_URI"] = get_postgres_database_uri()
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

app.config["SECRET_KEY"] = secrets.token_hex()

db.init_app(app)

import models

with app.app_context():
    db.create_all()

import auth
app.register_blueprint(auth.bp)

import views
app.register_blueprint(views.bp)
app.add_url_rule('/', endpoint='index')

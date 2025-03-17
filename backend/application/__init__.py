import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_folder='../../frontend', static_url_path='https://services.entretienrjs.ca/')

app.config['SECRET_KEY'] = 'mysecret'

# Database setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///' + os.path.join(basedir, 'wash-services-db.sqlite')"  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
Migrate(app, db)
from application.models import *
with app.app_context():
    db.create_all()






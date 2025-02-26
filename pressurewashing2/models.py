# Define the User model
from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    name = db.Column(db.String(100), nullable=False)  # User's name
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(100), unique=True,nullable=False)
    address= db.Column(db.String(300),unique=False,nullable =False)
# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each service
    name = db.Column(db.String(100), nullable=False)  # Service name
    description = db.Column(db.Text, nullable=True)  # Description of the service

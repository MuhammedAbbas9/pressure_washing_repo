from flask_sqlalchemy import SQLAlchemy
from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity' : 'user',
        'polymorphic_on' : role
    }

    def __repr__(self):
        return f"User First name: {self.first_name}, Last name: {self.last_name}"
    

class Customer(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    service_requests = db.relationship('ServiceRequest', backref='customer', lazy = True)

    __mapper_args__ = {
        'polymorphic_identity' : 'customer'
    }

class Admin(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    orders = db.relationship('Order', backref='admin', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity' : 'admin'
    }

class WashService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    images_path = db.Column(db.String(200))

    def __repr__(self):
        return f"Wash Service: {self.type} - price: ${self.price}"
    
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    wash_services = db.relationship('WashService', secondary ='service_request_washservice', backref = 'service_requests')

    def __repr__(self):
        return f""
    
service_request_washservice = db.Table(
    'service_request_washservice',
    db.Column('service_request_id', db.Integer, db.ForeignKey('service_request.id', primary_key = True)),
    db.Column('wash_service_id', db.Integer, db.ForeignKey('wash_service.id', primary_key= True))
)


class Order:
    id = db.Column(db.Integer, primary_key=True)
    total_cost = db.Column(db.Float, nullable=False)
    expenses = db.Column(db.Float, nullable=False)
    tax = db.Column(db.Float, nullable=False)
    net_profit = db.Column(db.Float, nullable=False)
    service_request = db.relationship('ServiceRequest', backref= db.backref('order', useList=False))
    review = db.relationship('Review', backref= db.backref('order', useList=False))

    def __repr__(self):
        return f"Order: {self.id} - Net profit= {self.net_profit}"
    
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Rate: {self.rate}, Review: {self.message}"

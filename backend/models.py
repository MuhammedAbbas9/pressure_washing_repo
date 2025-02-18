from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

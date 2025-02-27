from crypt import methods

from flask import Flask, jsonify, request
from flask.sansio.blueprints import Blueprint
from sqlalchemy import delete

app = Flask(__name__)


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure SQLite database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "database.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    name = db.Column(db.String(100), nullable=False)  # User's name
    email = db.Column(db.String(100), unique=True, nullable=False)  # Unique email
    phone = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(300), unique=False, nullable=False)
# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each service
    name = db.Column(db.String(100), nullable=False)  # Service name
    description = db.Column(db.Text, nullable=True)  # Description of the service

# Create tables
with app.app_context():
    db.create_all()
    print("Database and tables created successfully!")

if __name__ == "__main__":
    app.run(debug=True)



#user_bp= Blueprint('user_bp',__name__,url_prefix='/users')
#app.register_blueprint(user_bp)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json(silent=True)
    new_user = User(name=data['name'], email=data['email'],phone=data['phone'],address=data['address'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully"}), 201

@app.route('/users',methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id":u.id,"name":u.name,"email":u.email,"phone":u.phone,"address":u.address} for u in users])


@app.route("/users<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200
@app.route("/users<int:id>",methods=["PUT"])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    user.phone = data.get("phone", user.phone)
    user.address = data.get("address", user.address)

    db.session.commit()
    return jsonify({"message": "User updated successfully"}), 200



@app.route("/users<int:id>",methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200
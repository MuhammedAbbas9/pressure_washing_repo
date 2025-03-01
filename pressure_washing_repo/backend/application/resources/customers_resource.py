from flask import Blueprint
from flask_restful import Api, reqparse
from flask_restful import Resource, reqparse


from backend.application.dtos.customer_detail_dto import Customer_detail_DTO
#from models import db, Customer, User
#from dtos import Customer_detail_dto

from backend.application.models import Customer, User

customer_detail_bp = Blueprint("customer_detail_bp", __name__)
api = Api(customer_detail_bp)

class CustomerDetailResource(Resource):
    def get(self, customer_id):
        """获取客户联系信息"""
        customer = Customer.query.get(customer_id)
        if not customer:
            return {"message": "Customer not found"}, 404

        customer_detail_dto = Customer_detail_DTO.from_model(customer)
        return customer_detail_dto.__dict__, 200

    def post(self):
        """创建新客户"""
        parser = reqparse.RequestParser()
        parser.add_argument("first_name", type=str, required=True, help="First name is required")
        parser.add_argument("last_name", type=str, required=True, help="Last name is required")
        parser.add_argument("phone", type=str, required=True, help="Phone number is required")
        parser.add_argument("email", type=str, required=True, help="Email is required")
        args = parser.parse_args()

        # 创建 User 实例
        new_user = User(
            first_name=args["first_name"],
            last_name=args["last_name"],
            phone=args["phone"],
            email=args["email"],
            role="customer"
        )
        db.session.add(new_user)
        db.session.commit()

        # 创建 Customer 实例
        new_customer = Customer(id=new_user.id)
        db.session.add(new_customer)
        db.session.commit()

        return {"message": "Customer created successfully", "customer_id": new_customer.id}, 201

    def put(self, customer_id):
        """更新客户联系信息"""
        customer = Customer.query.get(customer_id)
        if not customer:
            return {"message": "Customer not found"}, 404

        parser = reqparse.RequestParser()
        parser.add_argument("phone", type=str)
        parser.add_argument("email", type=str)
        args = parser.parse_args()

        if args["phone"]:
            customer.phone = args["phone"]
        if args["email"]:
            customer.email = args["email"]

        db.session.commit()
        return {"message": "Customer updated successfully"}, 200

    def delete(self, customer_id):
        """删除客户"""
        customer = Customer.query.get(customer_id)
        if not customer:
            return {"message": "Customer not found"}, 404

        # 先删除 Customer，再删除 User
        db.session.delete(customer)
        user = User.query.get(customer.id)
        if user:
            db.session.delete(user)

        db.session.commit()
        return {"message": "Customer deleted successfully"}, 200

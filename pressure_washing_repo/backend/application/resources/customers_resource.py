from flask import Blueprint
from flask_restful import Api, reqparse
from flask_restful import Resource, reqparse
from application.services.customer_service import CustomerService
from  dtos.customer_detail_dto import Customer_detail_DTO

from backend.application.dtos.customer_detail_dto import Customer_detail_DTO
#from models import db, Customer, User
#from dtos import Customer_detail_dto

from backend.application.models import Customer, User

customer_detail_bp = Blueprint("customer_detail_bp", __name__)
api = Api(customer_detail_bp)



class CustomerResource(Resource):
    def get(self, customer_id):
        customer = CustomerService.get_customer_by_id(customer_id)
        if not customer:
            return {'message': 'Customer not found'}, 404
        customer_dto = CustomerDTO.from_model(customer)
        return customer_dto.__dict__, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name is required')
        parser.add_argument('email', type=str, required=True, help='Email is required')
        parser.add_argument('phone', type=str, required=True, help='Phone is required')
        data = parser.parse_args()
        customer = CustomerService.create_customer(data)
        customer_dto = CustomerDTO.from_model(customer)
        return customer_dto.__dict__, 201

    def put(self, customer_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=str)
        data = parser.parse_args()
        customer = CustomerService.get_customer_by_id(customer_id)
        if not customer:
            return {'message': 'Customer not found'}, 404
        customer = CustomerService.update_customer(customer, data)
        customer_detail_dto = Customer_detail_DTO.from_model(customer)
        return customer_dto.__dict__, 200

    def delete(self, customer_id):
        customer = CustomerService.get_customer_by_id(customer_id)
        if not customer:
            return {'message': 'Customer not found'}, 404
        CustomerService.delete_customer(customer)
        return {'message': 'Customer deleted successfully'}, 200

api.add_resource(CustomerResource, '/customers', '/customers/<int:customer_id>')
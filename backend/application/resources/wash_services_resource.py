# from config import Resource
from application.services.wash_service import WashServiceService
from flask import Blueprint
from flask_restful import Api, Resource, reqparse

wash_service_bp = Blueprint("wash_service_bp", __name__)
api = Api(wash_service_bp)

class WashServiceResource(Resource):

    def get(self, id=None):
        if id == None:
            # Fetch all wash services if no ID is provided
            wash_service_Result_List = WashServiceService.get_all_wash_services()
            return wash_service_Result_List, 200
    
        #Fetch the requested wash service by id.
        wash_service_Result = WashServiceService.get_wash_service_by_id(id)
        if not wash_service_Result:
            return {"message" : "Service not found"}, 404
        return wash_service_Result, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("type", type=str, required=True, help="Type of service is required")
        parser.add_argument("description", type=str, required=False)
        parser.add_argument("price", type=float, required=True, help="Price is required")
        parser.add_argument("images_path", type=str, required=False)
        parser.add_argument("icon_path", type=str, required=False)
        data = parser.parse_args()

        new_service = WashServiceService.create_wash_service(data)
        return new_service, 201
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("type", type=str, required=False)
        parser.add_argument("description", type=str, required=False)
        parser.add_argument("price", type=float, required=False)
        parser.add_argument("images_path", type=str, required=False)
        parser.add_argument("icon_path", type=str, required=False)
        data = parser.parse_args()

        updated_service = WashServiceService.update_wash_service(id, data)
        if not updated_service:
            return {"message": "Service not found or no fields to update"}, 404
        return updated_service, 200
    

api.add_resource(WashServiceResource, '/wash_services/<int:id>', '/wash_services')

 

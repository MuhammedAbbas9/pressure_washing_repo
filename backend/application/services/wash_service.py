from application.models import WashServiceModel, db
from application.dtos.wash_service_dto import WashServiceDTO

class WashServiceService:

    @staticmethod
    def get_all_wash_services():
        """Fetch all wash services and return serialized DTOs"""
        wash_services_list = WashServiceModel.query.all()
        return WashServiceDTO().dump(wash_services_list, many = True)
    
    @staticmethod
    def get_wash_service_by_id(id):
        """ Fetch a single wash service and return serialized DTO """
        wash_service_result = WashServiceModel.query.get(id)
        return WashServiceDTO().dump(wash_service_result) if wash_service_result else None
    
    @staticmethod
    def create_wash_service(data):
        """ Create a new wash service """
        new_service = WashServiceModel(
            type=data["type"],
            price=data["price"],
            images_path=data.get("images_path")
        )
        db.session.add(new_service)
        db.session.commit()
        return WashServiceDTO().dump(new_service)  # Serialize single object
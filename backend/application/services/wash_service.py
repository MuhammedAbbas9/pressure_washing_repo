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
            description=data.get("description"),
            price=data["price"],
            images_path=data.get("images_path"),
            icon_path=data.get("icon_path")
        )
        db.session.add(new_service)
        db.session.commit()
        return WashServiceDTO().dump(new_service)  # Serialize single object
    

    @staticmethod
    def update_wash_service(id, data):
        # Fetch the wash service by id
        wash_service = WashServiceModel.query.get(id)
        if not wash_service:
            return None

        # Update the fields if provided
        if data.get("type"):
            wash_service.type = data["type"]
        if data.get("description"):
            wash_service.description = data["description"]   
        if data.get("price"):
            wash_service.price = data["price"]
        if data.get("images_path"):
            wash_service.images_path = data["images_path"]
        if data.get("icon_path"):
            wash_service.icon_path = data["icon_path"]

        db.session.commit()

        return WashServiceDTO().dump(wash_service)  # Serialize single object

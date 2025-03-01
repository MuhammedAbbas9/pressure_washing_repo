from marshmallow import Schema

class Customer_detail_DTO(Schema):
    def __init__(self, id, phone, email):
        self.id = id
        self.phone = phone
        self.email = email

    @classmethod
    def from_model(cls, customer):
        return cls(
            id=customer.id,
            phone=customer.phone,
            email=customer.email
        )

from marshmallow import Schema, fields

class WashServiceDTO(Schema):
    """ DTO for WashService Serialization """
    id = fields.Int(dump_only=True) # Read-only field
    type = fields.Str(required = True)
    price = fields.Float(required = True)
    description = fields.Str(allow_none= True) # Optional field
    images_path = fields.Str(allow_none= True) # Optional field
    icon_path = fields.Str(allow_none= True) # Optional field


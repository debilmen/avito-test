from marshmallow import Schema, fields

from api.base import RequestDto


class RequestCreateDtoSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    photo = fields.List(fields.Str())
    price = fields.Int()


class RequestCreateDto(RequestDto, RequestCreateDtoSchema):
    __schema__ = RequestCreateDtoSchema


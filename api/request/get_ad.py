from marshmallow import Schema, fields

from api.base import RequestDto


class RequestGetDtoSchema(Schema):
    id = fields.Int()
    Fields = fields.Bool(default=False, required=False)


class RequestGetDto(RequestDto, RequestGetDtoSchema):
    __schema__ = RequestGetDtoSchema

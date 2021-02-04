from marshmallow import Schema, fields, pre_load, post_load

from api.base import ResponseDto
from api.request import RequestGetDto


class ResponseGetDtoSchema(Schema):
    name = fields.Str()
    photo = fields.Str()
    price = fields.Int()
    description = fields.Str(required=False)
    all_photo = fields.Str(required=False)


class ResponseGetDto(ResponseDto, ResponseGetDtoSchema):
    __schema__ = ResponseGetDtoSchema


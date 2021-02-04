import datetime

from marshmallow import Schema, fields, pre_load, post_load

from api.base import ResponseDto


class ResponseCreateDtoSchema(Schema):
    id = fields.Int(required=True)
    status_code = fields.Int()


class ResponseCreateDto(ResponseDto, ResponseCreateDtoSchema):
    __schema__ = ResponseCreateDtoSchema

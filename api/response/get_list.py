from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseListDtoSchema(Schema):
    name = fields.Str()
    photo = fields.Str()
    price = fields.Int()


class ResponseListDto(ResponseDto, ResponseListDtoSchema):
    __schema__ = ResponseListDtoSchema


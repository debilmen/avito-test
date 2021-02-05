from marshmallow import Schema, fields

from api.base import RequestDto


class RequestListDtoSchema(Schema):
    ascend_price = fields.Bool()
    ascend_date = fields.Bool()


class RequestListDto(RequestDto, RequestListDtoSchema):
    __schema__ = RequestListDtoSchema

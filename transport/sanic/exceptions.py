from sanic.exceptions import SanicException


class SanicDBException(SanicException):
    status_code = 400

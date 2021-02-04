from sanic.exceptions import SanicException


class DBIntegrityException(Exception):
    pass


class DBAdNotExistException(SanicException):
    status_code = 404


class DBDataException(Exception):
    pass
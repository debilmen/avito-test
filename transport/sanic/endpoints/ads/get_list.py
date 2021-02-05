from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response import ResponseListDto
from api.request import RequestListDto
from db.exceptions import DBDataException, DBIntegrityException
from db.queries import ad_queries
from transport.sanic.endpoints import BaseEndpoint

from transport.sanic.exceptions import SanicDBException


class GetListEndpoint(BaseEndpoint):

    async def method_get(self, request: Request, body: dict, session, page_n: int, *args, **kwargs) -> BaseHTTPResponse:
        request_model = RequestListDto(body)

        try:
            request_model.ascend_price
        except AttributeError:
            request_model.ascend_price = None

        try:
            request_model.ascend_date
        except AttributeError:
            request_model.ascend_date = None

        if (request_model.ascend_date is not None) and (request_model.ascend_price is not None):
            raise SanicDBException("cant sort")

        lst = ad_queries.get_list(session, page_n, request_model.ascend_price, request_model.ascend_date)

        response_model = ResponseListDto(lst, many=True)

        return await self.make_response_json(status=200, body=response_model.dump())

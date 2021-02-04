from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response import ResponseListDto
from db.exceptions import DBDataException, DBIntegrityException
from db.queries import ad_queries
from transport.sanic.endpoints import BaseEndpoint

from transport.sanic.exceptions import SanicDBException


class GetListEndpoint(BaseEndpoint):

    async def method_get(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:
        lst = ad_queries.get_list(session)

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))
        response_model = ResponseListDto(lst)
        return await self.make_response_json(status=200, body=response_model.dump())

from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestCreateDto
from api.response.create_ad import ResponseCreateDto
from db.exceptions import DBDataException, DBIntegrityException
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException

from db.queries import ad_queries


class CreateEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateDto(body)
        try:
            db_ad = ad_queries.create_ad(session, request_model)
        except AttributeError as e:
            raise SanicDBException("")
        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))
        response_model = ResponseCreateDto(db_ad)

        return await self.make_response_json(body=response_model.dump(), status=201)

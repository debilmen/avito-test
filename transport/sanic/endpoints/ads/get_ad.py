from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response import ResponseGetDto
from db.exceptions import DBDataException, DBIntegrityException
from db.queries import ad_queries
from transport.sanic.endpoints import BaseEndpoint
from api.request import RequestGetDto
from transport.sanic.exceptions import SanicDBException


class GetEndpoint(BaseEndpoint):

    async def method_get(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestGetDto(body)
        ad_id = request_model.id
        try:
            is_fields = request_model.Fields
        except AttributeError:
            is_fields = False
        db_ad = ad_queries.get_ad(session, ad_id)

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))
        if is_fields is False or None:
            response_model = ResponseGetDto(db_ad, all=False)
        else:
            response_model = ResponseGetDto(db_ad, all=True)
        return await self.make_response_json(body=response_model.dump(), status=201)

import pytest

from transport.sanic.endpoints.ads.get_list import GetListEndpoint


@pytest.mark.asyncio
async def test_get_list_endpoint(request_factory, patched_context, mocker):
    patched_query = mocker.patch('db.queries.ad_queries.get_list')
    patched_query.return_value = []

    request = request_factory(method='get')
    endpoint = GetListEndpoint(None, patched_context, '', ())

    response = await endpoint(request)

    assert response.status == 200

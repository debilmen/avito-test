import pytest

from transport.sanic.endpoints.ads.get_ad import GetEndpoint


@pytest.mark.asyncio
async def test_get_ad_endpoint(request_factory, patched_context, mocker):
    patched_query = mocker.patch('db.queries.ad_queries.get_ad')
    patched_query.return_value = []

    request = request_factory(method='get')
    endpoint = GetEndpoint(None, patched_context, '', ())

    response = await endpoint(request)

    assert response.status == 200

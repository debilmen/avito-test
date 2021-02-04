from typing import Tuple

from configs.config import ApplicationConfig
from context import Context
from transport.sanic import endpoints


def get_routes(config: ApplicationConfig, context: Context) -> Tuple:
    return (
        endpoints.CreateEndpoint(
            config, context, uri='/ad', methods=['POST'],
        ),
        endpoints.GetEndpoint(
            config, context, uri='/ad', methods=['GET'],
        ),
        endpoints.GetListEndpoint(
            config, context, uri='/ads', methods=['GET'],
        )
    )

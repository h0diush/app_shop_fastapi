from fastapi_users.authentication import (
    AuthenticationBackend,
)

from core.authentication.transport import authentication_transport
from .strategy import get_database_strategy

authentication_backend = AuthenticationBackend(
    name="access_tokens_db",
    transport=authentication_transport,
    get_strategy=get_database_strategy,
)

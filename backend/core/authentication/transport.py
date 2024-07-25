from fastapi_users.authentication import BearerTransport

authentication_transport = BearerTransport(tokenUrl="api/v1/auth")

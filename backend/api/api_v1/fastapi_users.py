from fastapi_users import FastAPIUsers

from core.models import User
from core.types.user_id import UserIdType
from api.dependencies.authentication.backend import authentication_backend
from api.dependencies.authentication.user_manager import get_user_manager

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)

current_user = fastapi_users.current_user(active=True)
superuser = fastapi_users.current_user(superuser=True, active=True)

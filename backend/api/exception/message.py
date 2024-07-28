from fastapi import HTTPException, status

NO_PROFILE = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Данный профиль не существует",
)

PROFILE_EXISTS = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Профиль уже существует",
)


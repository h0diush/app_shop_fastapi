from fastapi import HTTPException, status

NO_PROFILE = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Профиль не существует",
)

PROFILE_EXISTS = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Профиль уже существует",
)

NO_ADDRESS = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Адрес не существует",
)


NO_CATEGORY = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Данной группы не существует"
)

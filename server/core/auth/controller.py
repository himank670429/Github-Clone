from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from core.auth.constants import (
    BEARER_AUTHENTICATE_HEADER,
    INVALID_CREDENTIALS_MESSAGE,
)
from core.auth.dtos.auth import (
    AuthResponse,
    LoginRequest,
    RegisterRequest,
    UserResponse,
)
from core.auth.service import authenticate_user, register_user


def register(payload: RegisterRequest, db: Session) -> UserResponse:
    try:
        return register_user(db, payload)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error


def login(payload: LoginRequest, db: Session) -> AuthResponse:
    auth_response = authenticate_user(db, payload)
    if auth_response is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=INVALID_CREDENTIALS_MESSAGE,
            headers={"WWW-Authenticate": BEARER_AUTHENTICATE_HEADER},
        )
    return auth_response

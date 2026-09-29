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
from core.auth.service import AuthService


class AuthController:
    def __init__(self, service: AuthService | None = None) -> None:
        self.service = service or AuthService()

    def register(self, payload: RegisterRequest, db: Session) -> UserResponse:
        try:
            return self.service.register_user(db, payload)
        except ValueError as error:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=str(error),
            ) from error

    def login(self, payload: LoginRequest, db: Session) -> AuthResponse:
        auth_response = self.service.authenticate_user(db, payload)
        if auth_response is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=INVALID_CREDENTIALS_MESSAGE,
                headers={"WWW-Authenticate": BEARER_AUTHENTICATE_HEADER},
            )
        return auth_response

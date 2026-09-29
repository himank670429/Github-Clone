from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.auth.controller import AuthController
from core.auth.dtos.auth import (
    AuthResponse,
    LoginRequest,
    RegisterRequest,
    UserResponse,
)
from dependencies.database import get_db


class AuthRouter:
    def __init__(self) -> None:
        self.router = APIRouter(prefix="/auth", tags=["auth"])
        self.controller = AuthController()

        self.router.post(
            "/register",
            response_model=UserResponse,
            status_code=status.HTTP_201_CREATED,
        )(self.register)
        self.router.post("/login", response_model=AuthResponse)(self.login)

    def register(
        self, payload: RegisterRequest, db: Annotated[Session, Depends(get_db)]
    ) -> UserResponse:
        return self.controller.register(payload, db)

    def login(
        self, payload: LoginRequest, db: Annotated[Session, Depends(get_db)]
    ) -> AuthResponse:
        return self.controller.login(payload, db)


auth_router = AuthRouter().router

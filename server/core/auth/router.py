from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.auth.controller import login, register
from core.auth.dtos.auth import (
    AuthResponse,
    LoginRequest,
    RegisterRequest,
    UserResponse,
)
from dependencies.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def register_route(
    payload: RegisterRequest, db: Annotated[Session, Depends(get_db)]
) -> UserResponse:
    return register(payload, db)


@router.post("/login", response_model=AuthResponse)
def login_route(
    payload: LoginRequest, db: Annotated[Session, Depends(get_db)]
) -> AuthResponse:
    return login(payload, db)

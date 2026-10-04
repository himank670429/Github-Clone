from typing import Annotated

from fastapi import Depends, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from core.auth.dtos import RegisterRequest, UserResponse
from core.auth.service import AuthService
from core.auth.utils import hash_password, normalize_identifier
from decorators import rollback_on_error
from dependencies.database import get_db

from exceptions import ExceptionWithErrorCode

class AuthController:
    def __init__(self, service: AuthService | None = None) -> None:
        self.service = service or AuthService()

    @rollback_on_error
    def register(
        self, data: RegisterRequest, db: Annotated[Session, Depends(get_db)]
    ) -> UserResponse:
        email = normalize_identifier(data.email).lower()
        username = normalize_identifier(data.username)
        hashed_password = hash_password(data.password)

        already_eixisting_email = self.service.get_user_by_email(db, email)
        already_existing_username = self.service.get_user_by_username(db, username)

        if already_eixisting_email:
            raise ExceptionWithErrorCode("E-10003", http_status_code=status.HTTP_409_CONFLICT)

        if already_existing_username:
            raise ExceptionWithErrorCode("E-10002", http_status_code=status.HTTP_409_CONFLICT)

        payload = RegisterRequest(
            email=email,
            username=username,
            password=hashed_password
        )

        try:
            user = self.service.create_user(
                db=db,
                payload=payload
            )
        except IntegrityError:
            raise

        return UserResponse.model_validate(user)

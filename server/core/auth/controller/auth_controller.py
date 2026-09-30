from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from core.auth.constants import DUPLICATE_USER_MESSAGE
from core.auth.dtos import RegisterRequest, UserResponse
from core.auth.service import AuthService
from core.auth.utils import hash_password, normalize_identifier
from decorators import rollback_on_error
from dependencies.database import get_db


class AuthController:
    def __init__(self, service: AuthService | None = None) -> None:
        self.service = service or AuthService()

    @rollback_on_error
    def register(
        self, data: RegisterRequest, db: Annotated[Session, Depends(get_db)]
    ) -> UserResponse:
        email = normalize_identifier(data.email).lower()
        username = normalize_identifier(data.username)

        already_eixisting_email = self.service.get_user_by_email(db, email)
        already_existing_username = self.service.get_user_by_username(db, username)

        if already_eixisting_email or already_existing_username:
            raise HTTPException(status.HTTP_409_CONFLICT, DUPLICATE_USER_MESSAGE)

        try:
            user = self.service.create_user(
                db,
                username=username,
                email=email,
                password_hash=hash_password(data.password),
            )
        except IntegrityError:
            # Concurrent registration slipped past the existence check
            raise HTTPException(
                status.HTTP_409_CONFLICT, DUPLICATE_USER_MESSAGE
            ) from None

        return UserResponse.model_validate(user)

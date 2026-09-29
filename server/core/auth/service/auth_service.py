from sqlalchemy import or_, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from core.auth.constants import DUPLICATE_USER_MESSAGE
from core.auth.dtos.auth import (
    AuthResponse,
    LoginRequest,
    RegisterRequest,
    UserResponse,
)
from core.auth.models.user import User
from core.auth.utils import (
    create_access_token,
    hash_password,
    normalize_identifier,
    verify_password,
)


class AuthService:
    def register_user(self, db: Session, payload: RegisterRequest) -> UserResponse:
        user = User(
            username=payload.username,
            email=payload.email.lower(),
            password_hash=hash_password(payload.password),
        )
        db.add(user)
        try:
            db.commit()
        except IntegrityError as error:
            db.rollback()
            raise ValueError(DUPLICATE_USER_MESSAGE) from error

        db.refresh(user)
        return UserResponse.model_validate(user)


    def authenticate_user(
        self, db: Session, payload: LoginRequest
    ) -> AuthResponse | None:
        identifier = normalize_identifier(payload.username_or_email)
        user = db.scalar(
            select(User).where(
                or_(User.username == identifier, User.email == identifier.lower())
            )
        )
        if user is None or not verify_password(payload.password, user.password_hash):
            return None

        return AuthResponse(
            access_token=create_access_token(str(user.id)),
            user=UserResponse.model_validate(user),
        )

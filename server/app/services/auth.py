from sqlalchemy import or_, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User
from app.schemas.auth import AuthResponse, LoginRequest, RegisterRequest, UserResponse


def register_user(db: Session, payload: RegisterRequest) -> UserResponse:
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
        raise ValueError("Username or email is already registered") from error

    db.refresh(user)
    return UserResponse.model_validate(user)


def authenticate_user(db: Session, payload: LoginRequest) -> AuthResponse | None:
    identifier = payload.username_or_email.strip()
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

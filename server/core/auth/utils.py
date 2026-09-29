from datetime import UTC, datetime, timedelta

import jwt
from pwdlib import PasswordHash

from env import get_settings

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(subject: str) -> str:
    settings = get_settings()
    expires_at = datetime.now(UTC) + timedelta(
        minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        {"sub": subject, "exp": expires_at},
        settings.JWT_SECRET_KEY,
        algorithm="HS256",
    )


def normalize_identifier(identifier: str) -> str:
    return identifier.strip()

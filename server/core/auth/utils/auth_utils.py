from datetime import UTC, datetime, timedelta

import jwt
from pwdlib import PasswordHash

from env import JWT_ACCESS_TOKEN_EXPIRE_MINUTES, JWT_SECRET_KEY

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(subject: str) -> str:
    expires_at = datetime.now(UTC) + timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(
        {"sub": subject, "exp": expires_at},
        JWT_SECRET_KEY,
        algorithm="HS256",
    )


def normalize_identifier(identifier: str) -> str:
    return identifier.strip()

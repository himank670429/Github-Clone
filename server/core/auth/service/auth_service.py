from sqlalchemy import select
from sqlalchemy.orm import Session

from core.auth.dtos.auth import RegisterRequest
from core.auth.models import User


class AuthService:
    def get_user_by_email(self, db: Session, email: str) -> User | None:
        return db.scalar(select(User).where(User.email == email))

    def get_user_by_username(self, db: Session, username: str) -> User | None:
        return db.scalar(select(User).where(User.username == username))

    def create_user(
        self, db: Session, payload: RegisterRequest
    ) -> User:
        user = User(username=payload.username, email=payload.email, password_hash=payload.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

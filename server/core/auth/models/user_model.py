from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database import Base
from infrastructure.database.base_model import BaseModel


class User(BaseModel, Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))

    biography: Mapped[str | None] = mapped_column(String(1024), nullable=True)

    avatar_url: Mapped[str | None] = mapped_column(String(255), nullable=True)

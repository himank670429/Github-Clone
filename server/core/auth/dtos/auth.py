from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_serializer


class RegisterRequest(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=32, pattern=r"^[a-zA-Z0-9_-]+$")
    password: str = Field(min_length=8, max_length=128)


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: str
    email: EmailStr
    biography: str | None = None
    avatar_url: str | None = None
    created_at: datetime

    @field_serializer("created_at")
    def serialize_created_at(self, value: datetime) -> str:
        return value.isoformat()

    @field_serializer("id")
    def serialize_id(self, value: UUID) -> str:
        return str(value)
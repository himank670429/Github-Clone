from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Database settings
    DATABASE_URL: str = "sqlite:///./github_clone.db"

    # JWT settings
    JWT_SECRET_KEY: str = "development-secret-change-me-32-bytes"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # cors
    ALLOWED_ORIGINS: str = "http://localhost:5173"


settings = Settings()

DATABASE_URL = settings.DATABASE_URL
JWT_SECRET_KEY = settings.JWT_SECRET_KEY
JWT_ALGORITHM = settings.JWT_ALGORITHM
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
ALLOWED_ORIGINS = settings.ALLOWED_ORIGINS


__all__ = [
    'settings',
    "DATABASE_URL",
    "JWT_SECRET_KEY",
    "JWT_ALGORITHM",
    "JWT_ACCESS_TOKEN_EXPIRE_MINUTES",
    "ALLOWED_ORIGINS",
]
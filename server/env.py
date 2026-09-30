
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Database settings
    DATABASE_URL: str
    # Database Pooling
    DB_POOL_SIZE: int
    DB_MAX_OVERFLOW: int
    DB_POOL_PRE_PING: bool
    DB_POOL_RECYCLE: int
    DB_POOL_TIMEOUT: int

    # JWT settings
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int

    # cors
    ALLOWED_ORIGINS: str


settings = Settings()

DATABASE_URL = settings.DATABASE_URL
JWT_SECRET_KEY = settings.JWT_SECRET_KEY
JWT_ALGORITHM = settings.JWT_ALGORITHM
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
ALLOWED_ORIGINS = settings.ALLOWED_ORIGINS
DB_POOL_SIZE = settings.DB_POOL_SIZE
DB_MAX_OVERFLOW = settings.DB_MAX_OVERFLOW
DB_POOL_PRE_PING = settings.DB_POOL_PRE_PING
DB_POOL_RECYCLE = settings.DB_POOL_RECYCLE
DB_POOL_TIMEOUT = settings.DB_POOL_TIMEOUT



__all__ = [
    "ALLOWED_ORIGINS",
    "DATABASE_URL",
    "DB_MAX_OVERFLOW",
    "DB_POOL_PRE_PING",
    "DB_POOL_RECYCLE",
    "DB_POOL_SIZE",
    "DB_POOL_TIMEOUT",
    "JWT_ACCESS_TOKEN_EXPIRE_MINUTES",
    "JWT_ALGORITHM",
    "JWT_SECRET_KEY",
    'settings',
]
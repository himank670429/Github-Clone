from enum import StrEnum

from fastapi import APIRouter, FastAPI

from core.auth.router import auth_router


class ApiVersion(StrEnum):
    V1 = "v1"


def api_version_prefix(version: ApiVersion) -> str:
    return f"/api/{version}"


registered_routers: list[tuple[APIRouter, ApiVersion]] = [
    (auth_router, ApiVersion.V1),
]


def include_routers(app: FastAPI) -> None:
    for router, version in registered_routers:
        app.include_router(router, prefix=api_version_prefix(version))


__all__ = [
    "ApiVersion",
    "api_version_prefix",
    "include_routers",
    "registered_routers",
]

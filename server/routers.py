from collections.abc import Callable
from enum import StrEnum
from typing import TypeVar

from fastapi import APIRouter, FastAPI


class ApiVersion(StrEnum):
    V1 = "v1"


def api_version_prefix(version: ApiVersion) -> str:
    return f"/api/{version}"


RouterClass = TypeVar("RouterClass")


class RouterRegistry:
    def __init__(self) -> None:
        self._registered_routers: list[tuple[APIRouter, ApiVersion]] = []

    def register(self, router: APIRouter, version: ApiVersion) -> None:
        self._registered_routers.append((router, version))

    def include_in(self, app: FastAPI) -> None:
        for router, version in self._registered_routers:
            app.include_router(router, prefix=api_version_prefix(version))


router_registry = RouterRegistry()


def register_router(
    version: ApiVersion,
) -> Callable[[type[RouterClass]], type[RouterClass]]:
    def decorator(router_class: type[RouterClass]) -> type[RouterClass]:
        router_instance = router_class()
        router = router_instance.router
        if not isinstance(router, APIRouter):
            raise TypeError(
                "Registered router classes must expose an APIRouter as .router"
            )
        router_registry.register(router, version)
        return router_class

    return decorator


__all__ = [
    "ApiVersion",
    "RouterRegistry",
    "api_version_prefix",
    "register_router",
    "router_registry",
]

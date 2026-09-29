
from fastapi import APIRouter

from core.auth.controller import AuthController


class AuthRouter:
    def __init__(self) -> None:
        self.router = APIRouter(prefix="/auth", tags=["auth"])
        self.controller = AuthController()


auth_router = AuthRouter().router

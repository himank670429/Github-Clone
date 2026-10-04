from fastapi import APIRouter, status

from core.auth.controller import AuthController
from core.auth.dtos import UserResponse


class AuthRouter:
    def __init__(self) -> None:
        self.router = APIRouter(prefix="/auth", tags=["auth"])
        self.controller = AuthController()

        self.router.post("/register")(self.controller.register)


auth_router = AuthRouter().router

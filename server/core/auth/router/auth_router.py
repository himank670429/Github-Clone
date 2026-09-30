from fastapi import APIRouter, status

from core.auth.controller import AuthController
from core.auth.dtos import UserResponse


class AuthRouter:
    def __init__(self) -> None:
        self.router = APIRouter(prefix="/auth", tags=["auth"])
        self.controller = AuthController()

        self.router.add_api_route(
            "/register",
            self.controller.register,
            methods=["POST"],
            response_model=UserResponse,
            status_code=status.HTTP_201_CREATED,
        )


auth_router = AuthRouter().router

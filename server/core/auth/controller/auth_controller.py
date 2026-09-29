
from core.auth.service import AuthService


class AuthController:
    def __init__(self, service: AuthService | None = None) -> None:
        self.service = service or AuthService()

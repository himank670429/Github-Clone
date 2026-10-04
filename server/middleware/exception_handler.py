import traceback

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from exceptions import ExceptionWithErrorCode
from utils.response_utils import Res


class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except ExceptionWithErrorCode as e:
            return Res.error(
                e.error_code, e.message, http_status_code=e.http_status_code
            )
        except Exception as e:
            traceback.print_exc()  # Print the traceback to the console for debugging
            return Res.error("E-10001", str(e))

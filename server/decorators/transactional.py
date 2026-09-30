import inspect
from collections.abc import Callable
from functools import wraps
from typing import Any, ParamSpec, TypeVar

from sqlalchemy.orm import Session

P = ParamSpec("P")
R = TypeVar("R")


def _find_session(args: tuple[Any, ...], kwargs: dict[str, Any]) -> Session | None:
    for value in (*args, *kwargs.values()):
        if isinstance(value, Session):
            return value
    return None


def rollback_on_error(func: Callable[P, R]) -> Callable[P, R]:
    """Roll back the request's DB session if the wrapped controller raises."""
    if inspect.iscoroutinefunction(func):

        @wraps(func)
        async def async_wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            try:
                return await func(*args, **kwargs)
            except Exception:
                db = _find_session(args, kwargs)
                if db is not None:
                    db.rollback()
                raise

        return async_wrapper  # type: ignore[return-value]

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return func(*args, **kwargs)
        except Exception:
            db = _find_session(args, kwargs)
            if db is not None:
                db.rollback()
            raise

    return wrapper

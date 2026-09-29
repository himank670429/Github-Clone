from collections.abc import Generator

from fastapi import Request
from sqlalchemy.orm import Session


def get_db(request: Request) -> Generator[Session, None, None]:
    db = request.app.state.db_session_maker()
    try:
        yield db
    finally:
        db.close()

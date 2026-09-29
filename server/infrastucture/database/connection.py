from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from env import get_settings

settings = get_settings()


def get_db_engine():
    connect_args = (
        {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}
    )
    return create_engine(settings.DATABASE_URL, connect_args=connect_args)

def get_db_session_maker(engine: Engine) -> sessionmaker[Session]:
    return sessionmaker(bind=engine, autocommit=False, autoflush=False)


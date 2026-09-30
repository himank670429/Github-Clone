from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from env import ALLOWED_ORIGINS
from infrastructure.database.connection import get_db_engine, get_db_session_maker
from routers import include_routers


@asynccontextmanager
async def lifespan(application: FastAPI):
    engine = get_db_engine()
    application.state.db_engine = engine
    application.state.db_session_maker = get_db_session_maker(engine)
    try:
        yield
    finally:
        engine.dispose()


def create_app() -> FastAPI:

    app = FastAPI(title="GitHub Clone API", version="0.1.0", lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    include_routers(app)
    return app


app = create_app()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


__all__ = ["app"]

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.auth.router import router as auth_router
from env import get_settings
from infrastucture.database.connection import get_db_engine, get_db_session_maker


@asynccontextmanager
async def lifespan(application: FastAPI):
    engine = get_db_engine()
    application.state.db_engine = engine
    application.state.db_session_maker = get_db_session_maker(engine)
    try:
        yield
    finally:
        engine.dispose()


settings = get_settings()
app = FastAPI(title="GitHub Clone API", version="0.1.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router, prefix="/api/v1")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


__all__ = ["app"]

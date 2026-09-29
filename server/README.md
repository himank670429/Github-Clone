# GitHub Clone API

## Setup

From the `server` directory, sync the Python environment and install dependencies with uv:

```bash
uv sync
```

Copy `.env.example` to `.env`, set a long `JWT_SECRET_KEY`, then start the API:

```bash
uv run uvicorn main:app --reload
```

The default SQLite database is `server/github_clone.db`. Its schema is managed by Alembic.

Apply database migrations before starting the API:

```bash
uv run alembic upgrade head
```

All schema migrations live in `migrations/versions/`. To create a migration after changing a model:

```bash
uv run alembic revision --autogenerate -m "describe the change"
uv run alembic upgrade head
```

The API lifespan opens the SQLAlchemy engine and session factory and disposes the engine on shutdown. It does not create tables directly.

## Backend structure

```text
server/
├── constants/                 # Shared application constants
├── core/                      # Core application features
│   └── auth/                  # Auth feature and its mini-structure
│       ├── constants/
│       ├── controller/
│       ├── dtos/
│       ├── models/
│       ├── router/
│       ├── service/
│       └── utils/
├── dependencies/              # FastAPI dependency functions
├── features/                  # Non-core features
├── infrastucture/             # Third-party service connections
│   └── database/
├── routers.py                 # Central router imports and versioning
└── utils/                     # Shared helper functions
```

All core and misc feature routers are imported and versioned in `routers.py`:

```python
from core.auth.router import auth_router
from routers import ApiVersion, registered_routers


registered_routers.append((auth_router, ApiVersion.V1))
```

The application mounts every entry under its versioned `/api/{version}` prefix.

## Auth endpoints

### Register

`POST /api/v1/auth/register`

```json
{
  "username": "octocat",
  "email": "octocat@example.com",
  "password": "strong-password"
}
```

### Login

`POST /api/v1/auth/login`

The identifier accepts either the registered username or email address.

```json
{
  "username_or_email": "octocat",
  "password": "strong-password"
}
```

The response contains a JWT in `access_token` and the authenticated user in `user`. Send it to protected endpoints as `Authorization: Bearer <token>`.

`GET /health` is available for a basic server check.

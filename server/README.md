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

The default SQLite database is `server/github_clone.db`. Tables are created when the application starts.

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

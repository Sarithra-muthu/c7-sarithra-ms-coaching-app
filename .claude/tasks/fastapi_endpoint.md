# Task: FastAPI endpoint for analyse_work + GET /health

## Status: Completed

## Description
Wrapped `analyse_work()` in a FastAPI HTTP API so it can be called from any client
(frontend, Postman, other services). Also added a `GET /health` liveness check endpoint.

## What was built

### `api.py`
- `POST /analyse` — accepts `{ subject, work_content }`, calls `analyse_work()`, returns `{ subject, feedback }`
- `GET /health` — returns `{ "status": "ok" }` for liveness checks
- `AnalyseRequest` Pydantic model with `work_content: str = Field(min_length=1)` so empty strings are rejected with HTTP 422
- `AnalyseResponse` Pydantic model gives automatic OpenAPI schema generation
- `ValueError` from `analyse_work` (invalid subject) mapped to HTTP 400 via `HTTPException`
- Auto-generated Swagger UI available at `/docs` when server is running

### Design decisions
- POST over GET for `/analyse` — `work_content` can be large
- `main.py` left untouched; `api.py` is purely the HTTP layer
- `min_length=1` on `work_content` enforces validation at the Pydantic layer (422) before the endpoint runs

## How to run
```
uvicorn api:app --reload
```

## Files changed
| File | Change |
|------|--------|
| `api.py` | Created |

## Dependencies added
- `fastapi==0.136.3`
- `uvicorn==0.49.0`

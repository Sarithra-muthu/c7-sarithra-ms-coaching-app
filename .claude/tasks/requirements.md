# Task: requirements.txt — project dependencies

## Status: Completed

## Description
Added `requirements.txt` with pinned versions of all direct project dependencies
so the app can be installed and deployed reproducibly.

## What was built

### `requirements.txt`
| Package | Version | Purpose |
|---------|---------|---------|
| `groq` | 1.4.0 | Groq LLM API client (used in `main.py`) |
| `python-dotenv` | 1.2.2 | Loads `GROQ_API_KEY` from `.env` |
| `fastapi` | 0.136.3 | HTTP API framework (`api.py`) |
| `uvicorn` | 0.49.0 | ASGI server to run the FastAPI app |
| `httpx` | 0.28.1 | Required by FastAPI's TestClient (`test_api.py`) |
| `pytest` | 9.1.1 | Test runner |

Only direct dependencies are listed; transitive dependencies (pydantic, starlette, etc.)
are installed automatically by pip.

## How to install
```
pip install -r requirements.txt
```

## Files changed
| File | Change |
|------|--------|
| `requirements.txt` | Created |
| `.gitignore` | Created (excludes `.env`, `__pycache__`, `.pytest_cache`) |

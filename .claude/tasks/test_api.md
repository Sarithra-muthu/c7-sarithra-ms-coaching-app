# Task: test_api.py — FastAPI endpoint tests

## Status: Completed

## Description
Created a test suite for all endpoints in `api.py` using FastAPI's `TestClient`
and `unittest.mock`. No real Groq API calls are made — `analyse_work` is patched
at the `api` module level.

## What was built

### `test_api.py`
Four test cases covering:

| Test | Expectation |
|------|-------------|
| `GET /health` | HTTP 200, body `{"status": "ok"}` |
| `POST /analyse` with valid subject | HTTP 200, response contains `subject` and `feedback` fields |
| `POST /analyse` with invalid subject | HTTP 400 (ValueError mapped by endpoint) |
| `POST /analyse` with empty `work_content` | HTTP 422 (Pydantic min_length=1 validation) |

### Mock target
`"api.analyse_work"` — patched in the `api` module's namespace (where the name lives
after `from main import analyse_work`). Patching `main.analyse_work` would not
intercept the call.

## How to run
```
py -m pytest test_api.py -v
```

## Files changed
| File | Change |
|------|--------|
| `test_api.py` | Created |
| `api.py` | Added `Field(min_length=1)` to `AnalyseRequest.work_content` to enable 422 on empty input |

## Dependencies added
- `httpx==0.28.1` (required by FastAPI TestClient)
- `pytest==9.1.1`

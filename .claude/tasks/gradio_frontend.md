# Task: app.py — Gradio frontend for CSSE 11+ analyser

## Status: Completed

## Description
Created a Gradio web UI so parents can select a subject, paste their child's work,
and receive CSSE 11+ feedback in a chat-style interface. The UI calls the FastAPI
`POST /analyse` endpoint and keeps the full conversation history visible so multiple
submissions can be compared side by side.

## What was built

### `app.py`
- `gr.Blocks` layout with a `gr.Chatbot` (chat-style display) plus dropdown and textbox inputs above
- Subject dropdown: Maths, Comprehension, Creative Writing
- Multiline textbox for pasting student work
- **Analyse** button — calls `POST /analyse` on the backend, appends user message and feedback to the chatbot
- **Clear** button — resets the chatbot, state, and textbox
- Submit clears the textbox after each submission so the parent can immediately paste the next piece of work
- Empty submission guard: shows a prompt message without calling the backend
- HTTP errors (4xx/5xx) displayed inline in the chat
- `ConnectError` caught and shown as a friendly message if the backend is down
- 60 s timeout on backend calls (LLM responses can take several seconds)

### Configuration
- `BACKEND_URL` read from environment, defaulting to `http://127.0.0.1:8000/analyse`

### Design decisions
- `gr.Blocks` + `gr.Chatbot` over `gr.ChatInterface` — gives full layout control (dropdown + multiline input above the chat area)
- `type="messages"` on `gr.Chatbot` — modern Gradio 6.x dict format
- `gr.State` holds history list so previous analyses remain visible

## How to run
```
# Terminal 1 — backend
uvicorn api:app --reload

# Terminal 2 — frontend
py app.py
```
Then open `http://127.0.0.1:7860` in a browser.

## Files changed
| File | Change |
|------|--------|
| `app.py` | Created |
| `requirements.txt` | Added `gradio==6.18.0` |

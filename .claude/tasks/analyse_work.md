# Task: analyse_work function

## Status: Completed

## Implementation

Added `analyse_work(subject, work_content)` to `main.py`.

### What was built
- Loads Groq API key from `.env` via `python-dotenv` at module import time
- Initialises a module-level `Groq` client (singleton)
- `SUBJECT_CONFIG` dict holds CSSE 11+ total marks and criteria for each subject
- `analyse_work` validates the subject, builds a subject-specific system prompt anchored to CSSE 11+ criteria, then calls `llama-3.1-8b-instant` via the Groq SDK
- Returns a plain-text string with four labelled sections: MARKS, DONE WELL, WENT WRONG, STEPS TO IMPROVE

### Subjects and mark totals
| Subject          | Total |
|------------------|-------|
| Maths            | 50    |
| Comprehension    | 25    |
| Creative Writing | 20    |

### Dependencies
- `groq` 1.4.0 (already installed)
- `python-dotenv` 1.2.2 (already installed)
- Python launcher: `py` (`C:\Users\sarii\AppData\Local\Programs\Python\Python314\python.exe`)

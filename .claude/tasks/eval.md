# Task: eval.py — manual test harness for analyse_work

## Status: Completed

## Description
Created a runnable script that calls `analyse_work()` with one realistic sample
input per CSSE 11+ subject and prints the full LLM feedback to the terminal.
Used to manually verify end-to-end behaviour without writing automated tests.

## What was built
- `eval.py` at the project root
- `SAMPLES` dict with one piece of student work per subject (Maths, Comprehension, Creative Writing)
- Maths sample includes deliberate arithmetic errors so the LLM has real weaknesses to flag
- Comprehension sample has a short passage with four questions across retrieval, inference, vocabulary, and impressions
- Creative Writing sample is intentionally flat and repetitive to surface clear weaknesses
- `main()` loops over all subjects, prints a separator and the full feedback block for each

## How to run
```
py eval.py
```

## Files changed
| File | Change |
|------|--------|
| `eval.py` | Created |

# Quiz module

A Kerala PSC–style MCQ quiz for any course pack. One self-contained HTML page per course, built from the pack's `questions`.

| File | What it is |
|---|---|
| `template.html` | The quiz page (layout, logic). Edit this to change every course's quiz. |
| `<course>.html` | Built page with the course's questions embedded. Open it in a browser, host it, or share the file. |

Build or rebuild after changing a pack:

```sh
python3 scripts/validate_pack.py courses/cardiology/pack.json
python3 scripts/build_quiz.py courses/cardiology/pack.json   # writes quiz/cardiology.html
```

## How it works

- **Modes** (from the Recallio engine's test kinds): Quick test (5 Q), Mini test (10 Q), Mock exam (every question in the chosen module, timed).
- **Filter by syllabus module**, or all modules.
- **Kerala PSC marking**: +1 correct, −⅓ wrong, 0 skipped. Mock time is 72 s per question (100 questions in 120 minutes).
- Quick/mini tests show the answer and explanation after each question; the mock shows them at the end.
- Questions and options are shuffled each attempt.
- Result screen: marks, topics to revise, full answer review, and a ready-to-copy score line for social media posts.
- Best score is kept in the browser only.

## Adding a course

Write the course's `questions` in its `pack.json` (each needs `covers` pointing at the cards that teach it), validate, then run `build_quiz.py` on it.

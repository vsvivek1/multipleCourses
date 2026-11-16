# Cardiology — Kerala PSC Assistant Professor (Medical Education)

First Recallio-style course module, built from the official syllabus in
[`syllabi/medical/cardiology.txt`](../../syllabi/medical/cardiology.txt).

## Files

| File | What it is |
|---|---|
| `pack.json` | Recallio content pack (schema 1.0): topics, study cards, practice MCQs |
| `review.csv` | One row per card for the clinical reviewer (id, topic, type, key text, source, status) |

Check the pack with `python3 scripts/validate_pack.py courses/cardiology/pack.json`.

## Structure — mirrors the syllabus

| Module | Topics (marks) | Cards so far |
|---|---|---|
| 1 Basic cardiology (10) | Anatomy/physiology/pharmacology/embryology/pathology (3), Investigations (5), Genetics (2) | **Full**: 17 fact, 2 steps, 2 math, 1 diagram, 3 summary, 10 MCQs |
| 2 Clinical cardiology (15) | ACS/CCS, Valvular, Congenital | Summary card each |
| 3 (15) | Heart failure, Hypertension, Arrhythmia/SCD | Summary card each |
| 4 (5) | Cardiomyopathy | Summary card |
| 5 (5) | Pericardial disease | Summary card |
| 6 (10) | Infective endocarditis, Prosthetic valves/TAVI | Summary card each |
| 7 (5) | Pulmonary hypertension | Summary card |
| 8 (10) | Stroke, Atrial fibrillation | Summary card each |
| 9 (5) | Non-cardiac surgery | Summary card |
| 10 (20) | Aorta, PAD, DM & lipids, Pregnancy, Pulmonary embolism | Summary card each |

Topic ids are `cardio.mNN.<topic>`; every topic after Module 1 lists Module 1 basics as a prerequisite.

## Decisions and caveats

- **English only.** The exam is in English for specialists, so `languages` is `["en"]`.
- **Topic `freq` = syllabus marks ÷ 10** (5-mark topics 0.5). No past papers yet, so this is a proxy; replace it with a real frequency map once papers are added.
- **Exam date is a placeholder** (`2027-06-30`, `estimated`). No notification found; update when Kerala PSC announces it.
- **All cards are `needs_review`.** Facts follow standard references (Braunwald 12th ed., current ESC/ACC guidelines) but page numbers are not verified. A cardiologist should review before publishing.
- **MCQs are practice items**, not past-paper questions.
- Module 10 lists five 5-mark items under a 20-mark heading in the official PDF; all five are included.

## Next steps

Fill Modules 2–10 with full fact/steps/math cards, one module per PR, and add past papers for real frequency weighting.

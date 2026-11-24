#!/usr/bin/env python3
"""Build the self-contained quiz page for a course pack.

Usage:
    python3 scripts/build_quiz.py courses/cardiology/pack.json            # writes quiz/<slug>.html
    python3 scripts/build_quiz.py PACK.json --out FILE.html [--fragment]

The page embeds the pack's topics and questions, so it works offline and can be
hosted anywhere (GitHub Pages, a website, or shared as a single file).
--fragment leaves out the <!doctype>/<html>/<body> wrapper (for hosts that add their own).
"""
import argparse
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "quiz" / "template.html"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pack")
    ap.add_argument("--out")
    ap.add_argument("--fragment", action="store_true")
    args = ap.parse_args()
    pack_path = pathlib.Path(args.pack)
    pack = json.loads(pack_path.read_text(encoding="utf-8"))
    data = {
        "course": pack["course"],
        "topics": [{k: t.get(k) for k in ("id", "subject", "title")} for t in pack["topics"]],
        "questions": pack["questions"],
    }
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    title = pack["course"]["title"]["en"].split("—")[-1].strip() + " Quiz"
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*__PACK__*/null", blob).replace("__TITLE__", title)
    if not args.fragment:
        html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                "</head>\n<body>\n" + html + "\n</body>\n</html>\n")
    out = pathlib.Path(args.out) if args.out else ROOT / "quiz" / f"{pack_path.parent.name}.html"
    out.write_text(html, encoding="utf-8")
    print(f"Wrote {out} ({len(pack['questions'])} questions)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Delivery Gate for a MagangHub daily report.

Usage: check_report.py report.json      (or JSON on stdin)
Input: {"aktivitas": "- ...\n- ...", "pelajaran": "...", "kendala": "..."}
Exit 0 = PASS, 1 = FAIL. Prints one line per check.
Word lists below are Indonesian on purpose: the report text is Indonesian.
"""
import json
import re
import sys

MIN_CHARS = 100
FIRST_PERSON = re.compile(r"\b(saya|aku|kami|kita|penulis|gue|gua|gw)\b", re.I)
META = re.compile(r"\[INFERENCE|\bcatatan\s*:|\bperlu konfirmasi\b|\banda\b|\bsilakan\b|\bsemoga\b", re.I)
EM_DASH = re.compile(r"—|\s--\s")
CLICHES = [
    "pengalaman berharga", "sangat bermanfaat", "luar biasa", "di era modern", "di era digital",
    "tidak hanya", "sebuah perjalanan", "membuka wawasan", "semakin meningkat",
]
# Nouns and names that start with "Di" but are not passive verbs.
DI_NOT_PASSIVE = {"digital", "diagram", "dinas", "disk", "diskusi", "dimensi", "direktori", "distribusi", "dinamis"}

def load() -> dict:
    src = open(sys.argv[1], encoding="utf-8") if len(sys.argv) > 1 else sys.stdin
    return json.load(src)

def main() -> int:
    data = load()
    fields = {k: str(data.get(k, "")).strip() for k in ("aktivitas", "pelajaran", "kendala")}
    results: list[tuple[bool, str]] = []

    def check(ok: bool, msg: str) -> None:
        results.append((ok, msg))

    for name, text in fields.items():
        check(len(text) >= MIN_CHARS, f"G-1 {name}: {len(text)} chars (min {MIN_CHARS})")

    joined = "\n".join(fields.values())
    m = FIRST_PERSON.search(joined)
    check(not m, "G-2 no person pronouns" + (f": found '{m.group(0)}'" if m else ""))
    m = META.search(joined)
    check(not m, "G-3 no meta tags/notes" + (f": found '{m.group(0)}'" if m else ""))
    m = EM_DASH.search(joined)
    check(not m, "G-4 no em dash" + (f": found '{m.group(0).strip()}'" if m else ""))

    lines = [l for l in fields["aktivitas"].splitlines() if l.strip()]
    bullets = [l for l in lines if l.lstrip().startswith("- ")]
    check(lines and len(bullets) == len(lines) and 3 <= len(lines) <= 7,
          f"G-5 aktivitas: {len(bullets)}/{len(lines)} lines start with '- ' (need 3-7 lines, all bulleted)")

    passive = []
    for l in bullets:
        word = re.sub(r"^[-\s]+", "", l).split(" ")[0].lower()
        if re.fullmatch(r"di[a-z]{3,}", word) and word not in DI_NOT_PASSIVE:
            passive.append(word)
    check(not passive, "G-8 activities open with active meN- verbs" + (f": passive found {', '.join(passive)}" if passive else ""))

    for name in ("pelajaran", "kendala"):
        t = fields[name]
        check("\n" not in t and not t.lstrip().startswith(("-", "*")), f"G-6 {name}: one paragraph, no bullets")

    found = [c for c in CLICHES if c in joined.lower()]
    check(not found, "G-7 no empty cliches" + (f": {', '.join(found)}" if found else ""))

    for ok, msg in results:
        print(("PASS " if ok else "FAIL ") + msg)
    failed = sum(not ok for ok, _ in results)
    print(f"\n{'PASS' if not failed else 'FAIL'}: {len(results) - failed}/{len(results)} checks passed")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())

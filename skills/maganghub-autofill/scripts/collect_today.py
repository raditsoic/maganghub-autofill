#!/usr/bin/env python3
"""Collect today's work evidence: Claude Code chat prompts + git commits.

Usage: collect_today.py [YYYY-MM-DD]   (default: today, local timezone)

Chats: ~/.claude/projects/*/*.jsonl and ~/.omp/agent/sessions/*/*.jsonl,
       user prompts whose local date matches.
Git:   every repo (cwd) seen in today's chats, plus the current directory's
       repo, commits authored by the repo's configured user.name.
"""
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

day = sys.argv[1] if len(sys.argv) > 1 else datetime.now().astimezone().strftime("%Y-%m-%d")
root = Path.home() / ".claude" / "projects"
omp_root = Path.home() / ".omp" / "agent" / "sessions"
MAX_PROMPT = 1500

def local_day(ts: str) -> str:
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone().strftime("%Y-%m-%d")

def prompt_text(msg: dict) -> str:
    c = msg.get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return " ".join(p.get("text", "") for p in c if isinstance(p, dict) and p.get("type") == "text")
    return ""

chats: dict[str, list[tuple[str, str]]] = {}
cwds: set[str] = {str(Path.cwd())}

def add(cwd: str, ts: str, text: str) -> None:
    text = text.strip()
    if not text or text.startswith(("<", "Caveman", "[Request interrupted")):
        return
    cwds.add(cwd)
    t = datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone().strftime("%H:%M")
    chats.setdefault(cwd, []).append((t, text[:MAX_PROMPT].replace("\n", " ")))

for f in [*root.glob("*/*.jsonl"), *omp_root.glob("*/*.jsonl")]:
    if datetime.fromtimestamp(f.stat().st_mtime).astimezone().strftime("%Y-%m-%d") < day:
        continue
    omp_cwd = "?"
    for line in f.open(errors="replace"):
        try:
            o = json.loads(line)
        except ValueError:
            continue
        if o.get("type") == "session":  # omp header
            omp_cwd = o.get("cwd", "?")
            continue
        ts = o.get("timestamp")
        if not ts or local_day(ts) != day:
            continue
        if o.get("type") == "user" and not o.get("isSidechain") and not o.get("isMeta"):  # claude code
            add(o.get("cwd", "?"), ts, prompt_text(o.get("message", {})))
        elif o.get("type") == "message" and o.get("message", {}).get("role") == "user":  # omp
            add(omp_cwd, ts, prompt_text(o["message"]))

print(f"# Date: {day}\n\n## Agent chats (user prompts)")
if not chats:
    print("(none)")
for cwd, items in sorted(chats.items()):
    print(f"\n### {cwd}")
    for t, text in sorted(items):
        print(f"- {t} {text}")

print("\n## Git commits")
seen: set[str] = set()
found = False
for cwd in sorted(cwds):
    if not Path(cwd).is_dir():
        continue
    top = subprocess.run(["git", "-C", cwd, "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if top.returncode or top.stdout.strip() in seen:
        continue
    repo = top.stdout.strip()
    seen.add(repo)
    author = subprocess.run(["git", "-C", repo, "config", "user.name"], capture_output=True, text=True).stdout.strip()
    cmd = ["git", "-C", repo, "log", "--all", f"--since={day} 00:00", f"--until={day} 23:59:59",
           "--shortstat", "--pretty=format:%h %s"]
    if author:
        cmd.append(f"--author={author}")
    log = subprocess.run(cmd, capture_output=True, text=True).stdout.strip()
    if log:
        found = True
        print(f"\n### {repo}\n{log}")
if not found:
    print("(none)")

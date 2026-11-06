---
name: maganghub-autofill
description: "Draft and fill the daily report on the MagangHub Monev portal (Kemnaker, Indonesia's government internship program) from today's agent chats, today's git commits, and optional user notes. The report has three parts (activities, lessons learned, struggles) and is written in Indonesian with no first-person perspective. Use when the user runs /maganghub-autofill [notes], or asks to fill in their daily report, logbook, or internship journal. Fills the form in the browser but never ticks the confirmation checkbox or submits."
license: MIT
compatibility: Python 3.9+ (standard library only). Filling the form needs a browser tool in the agent (omp browser relay with Brave or Chrome, Playwright, or Chrome MCP) and a logged-in MagangHub Monev account; without one the skill outputs copy-paste text.
allowed-tools: Read Bash Glob Grep
---

# maganghub-autofill

Drafts the MagangHub daily report from real work evidence, then fills the form in the browser.

> [!IMPORTANT]
> **Two invariants.**
> 1. **The report text is always Indonesian**, even though this skill is written in English and the user may chat in English.
> 2. **Only the user submits.** The skill never ticks the confirmation checkbox and never clicks "Simpan dan Kirim". Submitting also records attendance.

Invocation: `/maganghub-autofill [user notes]`. Without notes, automatic evidence only.

## Requirements

| Need | Used for |
|---|---|
| Python 3.9+, standard library only | `collect_today.py`, `check_report.py` |
| Read access to `~/.claude/projects/`, `~/.omp/agent/sessions/`, and `git` | chat history and commits |
| A browser tool and a logged-in Monev account (`monev.maganghub.kemnaker.go.id`) | fill step only; Brave/Chrome setup with omp: "Relay notes" in `references/form.md` |

## Workflow

| # | Step | Tool or reference |
|---|---|---|
| 1 | Collect evidence | `scripts/collect_today.py` |
| 2 | Merge with user notes, filter | |
| 3 | Write the three parts | `references/writing-rules.md` |
| 4 | Delivery Gate | `scripts/check_report.py` |
| 5 | Show the draft to the user | |
| 6 | Fill the form in the browser | `references/form.md` |
| 7 | Report back, stop before submit | |

## Step 1: Collect evidence

```bash
python3 <skill-dir>/scripts/collect_today.py [YYYY-MM-DD]
```

`<skill-dir>` is this skill's directory. The date defaults to today (local timezone). Output:

- the user's prompts from Claude Code and omp chats on that date, grouped by working directory
- git commits on that date, in every repo touched by that day's chats and in the current directory's repo, limited to the repo's configured `user.name`

Prompts are truncated at 1500 characters. If a truncation drops important context, read the source session directly.

## Step 2: Merge and filter

- User notes (the skill argument) override guesses from the logs: add, correct, or drop items the user says are irrelevant. If the user names another date, use it in Step 1.
- Drop non-work: throwaway tests (`tes`), small talk, one-off tooling commands with no outcome.
- Drop meta-work: running, testing, or debugging this skill itself (prompts such as "use the maganghub-autofill skill", "run the collector", "show the draft"). Keep real work done on the skill's code only if the user's notes say it is internship work.
- Merge prompts and commits that belong to one piece of work into one activity.
- Facts only from evidence or user notes (W-01). No facts in either → **stop and ask the user** what was done. Never guess.
- Struggles: look for errors, bugs, reverts, or repeated retries in the evidence. Nothing found and the user did not mention any → ask the user (W-02). Never invent a struggle.

## Step 3: Write

Read `references/writing-rules.md`. Hard rules in short:

| ID | Rule |
|---|---|
| W-01 | Facts only from evidence or user notes |
| W-02 | Struggles must be real; none found → ask |
| W-10 | No person perspective: not saya, aku, kami, kita, penulis, Anda |
| W-11 | Each activity opens with an active meN- verb (Membuat, Menyusun, Memasang), not a di- passive |
| W-20 | Standard Indonesian; technical terms stay in their original form |
| W-21 | No empty vocabulary: pengalaman berharga, luar biasa, etc. |
| W-22 | No em dash |
| W-30 | Activities: 3-7 bullets starting with `- `, one concrete sentence each |
| W-31 | Lessons and struggles: one paragraph each |
| W-32 | Every part at least 100 characters |
| W-40 | No tokens, credentials, internal URLs/IPs, personal data |
| W-50 | Form text is report content only: no tags, notes, greetings |

Tone and full examples: `references/examples.md`.

## Step 4: Delivery Gate

Save the draft as JSON in `/tmp/maganghub-report.json` (never inside the user's project), then check it:

```bash
python3 <skill-dir>/scripts/check_report.py /tmp/maganghub-report.json
```

```json
{"aktivitas": "- ...\n- ...\n- ...", "pelajaran": "...", "kendala": "..."}
```

| Key | Form label |
|---|---|
| `aktivitas` | Uraian aktivitas |
| `pelajaran` | Pembelajaran yang diperoleh |
| `kendala` | Kendala yang dialami |

Automatic checks:

| Check | Content |
|---|---|
| G-1 | Every part at least 100 characters |
| G-2 | No person pronouns |
| G-3 | No meta tags or notes |
| G-4 | No em dash |
| G-5 | Activities: 3-7 lines, all bulleted |
| G-8 | Each activity opens with an active meN- verb, not a di- passive |
| G-6 | Lessons and struggles: one paragraph, no bullets |
| G-7 | No empty clichés |

On failure, fix and rerun until `PASS`.

> [!NOTE]
> The script cannot judge W-01 or W-02. Check those two yourself: every claim in the draft must trace to an evidence line or a user-note sentence.

## Step 5: Show the draft

Show the three parts in chat as clean text. Notes for the user (thin evidence, assumptions, parts needing confirmation) go separately below the draft, never inside text that will go into the form.

## Step 6: Fill the form

Read `references/form.md`. In short:

1. **Preflight, do not wait for login.** The skill expects a browser already logged in to Monev. Open `https://monev.maganghub.kemnaker.go.id/dashboard/evaluasi` in the agent's own tab and check the page: logged in shows the tabs Beranda, Riwayat, Perkembangan, Akun. Anything else (login page, redirect to SSO) means not logged in: **stop, do not poll or wait**, show the draft text per field, and tell the user to log in once in that browser and rerun. Never ask for or type credentials.
2. Go to `https://monev.maganghub.kemnaker.go.id/dashboard` (Beranda) and click **Isi Laporan Hari Ini**. For another date, open `/dashboard/riwayat?date=YYYY-MM-DD&view=edit`.
3. Fill the three textareas **Uraian aktivitas**, **Pembelajaran yang diperoleh**, **Kendala yang dialami**.
4. Read the three values back from the page, compare with the draft, confirm no validation message.
5. **Stop.** Do not tick the confirmation checkbox. Do not click "Simpan dan Kirim".

A day that is already submitted must not be overwritten: tell the user. No browser tool: show the text per field for copying.

## Step 7: Report

One or two sentences: the date filled, the Delivery Gate result, and which part the user should double-check. Tell the user the remaining manual steps: review, tick the confirmation checkbox, submit. No long summary.

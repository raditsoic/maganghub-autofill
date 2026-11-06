# Writing rules for the daily report

Each rule has an ID (`W-xx`) referenced from `SKILL.md`. Rule explanations are in English; every **Before** and **After** sample is Indonesian because the report itself is written in Indonesian. Pattern format: **Pattern**, **Why it fails**, **Before**, **After**.

| Group | Rules |
|---|---|
| Facts | W-01 facts only from evidence, W-02 real struggles only, W-03 lessons follow activities |
| Perspective | W-10 no person perspective, W-11 active verbs, not di- passives |
| Language | W-20 standard Indonesian, W-21 empty vocabulary, W-22 em dash and openers, W-23 hyperbole |
| Structure | W-30 activity bullets, W-31 one paragraph, W-32 100 characters, W-33 outline level only |
| Safety | W-40 no secrets |
| Form text | W-50 no meta |

> [!IMPORTANT]
> **Never invent facts** (W-01). A rewrite adds no activity, tool, number, person, or incident that is not in the evidence or the user's notes. If detail is missing, ask the user or write a shorter honest version.

> [!TIP]
> **Do not over-sterilize.** A report with no specifics reads as machine-made just as clearly as one full of clichés. Use real feature, module, tool, and outcome names from the evidence.

## Facts

### W-01 Facts only from evidence

- **Pattern:** an activity, result, or struggle that appears neither in the `collect_today.py` output nor in the user's notes.
- **Why it fails:** the mentor reads the report and uses it for evaluation. A fabrication sounds convincing but is false, and it is the one pattern that is always a defect even when it reads well.
- **Before:**
  > Mengadakan rapat koordinasi dengan tim produk untuk membahas roadmap kuartal depan.
  > (no meeting in the evidence or notes)
- **After:**
  > Merancang skema tabel `users` dan `sessions` untuk modul autentikasi.
  > (taken from a real commit or prompt)

### W-02 Struggles only if real

- **Pattern:** a generic struggle made up from general context: "sempat kesulitan memahami konsep baru", "keterbatasan waktu".
- **Why it fails:** an invented struggle looks honest but is false. Mentors read the struggle section to find real blockers.
- **Rule:** take struggles from errors, bugs, reverts, repeated retries, or hard decisions in the evidence, or from the user's notes. None found → **ask the user**, do not fill. If the user says there were none, write a short honest sentence that reaches the 100-character minimum without inventing an incident (see the no-struggle day in `examples.md`).
- **Before:**
  > Kendala yang dialami berupa kesulitan memahami alur kerja yang kompleks sehingga membutuhkan waktu lebih lama.
- **After:**
  > Konfigurasi middleware menolak token yang valid. Masalah ditelusuri lewat urutan pemrosesan permintaan dan diselesaikan dengan memperbaiki urutan middleware.

### W-03 Lessons follow activities

- **Pattern:** a lesson about something not done that day, or a claim that was not tested.
- **Why it fails:** every lesson must trace back to an activity above it.
- **Before:**
  > Pemahaman tentang arsitektur microservice dan Kubernetes bertambah.
  > (the day's work was form validation only)
- **After:**
  > Pemahaman tentang validasi input di sisi klien dan server bertambah, termasuk perlunya pesan galat yang spesifik untuk tiap aturan validasi.

## Perspective

### W-10 No person perspective

- **Pattern:** "saya", "aku", "kami", "kita", "penulis", and other pronouns that point at the actor. Includes "Anda" and the suffix "-ku".
- **Why it fails:** the user's requirement is an impersonal report.
- **Technique:** open each activity with an active meN- verb (Membuat, Menyusun, Memasang), which needs no pronoun. For lessons and struggles, use an activity noun (pemahaman, penyusunan) or the object as subject.
- **Before:**
  > Hari ini saya membuat endpoint login dan saya menulis tes untuknya.
- **After:**
  > Membuat endpoint login beserta tes unit untuk memverifikasi respons sukses dan gagal.

### W-11 Active verbs, not di- passives

- **Pattern:** activity bullets that open with a passive di- verb: "Dibuat ...", "Disusun ...", "Dipasang ...", or with an empty "Dilakukan ...".
- **Why it fails:** the passive reads as stiff and mechanical. The user's required style is an active meN- verb with the actor left implicit, which still avoids any pronoun.
- **Before:**
  > Dibuat fitur ekspor laporan ke CSV. Dilakukan pengujian fitur. Diperbaiki format tanggal.
- **After:**
  > Membuat fitur ekspor laporan ke CSV. Menguji fitur dengan 3 contoh data, menemukan kolom tanggal salah format, lalu memperbaikinya.
- **Scope:** applies to the opening verb of every activity bullet. Inside lessons and struggles, a passive clause is allowed when the object is the real subject, but prefer the active form. Vary the verbs; do not open every bullet with the same one.

## Language

### W-20 Standard Indonesian, technical terms unchanged

- **Pattern:** mixing "gue/lo", chat abbreviations, or forced translation of technical terms ("kait" for hook, "gudang" for repository).
- **Rule:** standard-register sentences. Library, language, tool, and command names and common loanwords (commit, endpoint, deploy, refactor) stay as they are.

### W-21 Empty vocabulary

- **Pattern:** "luar biasa", "sangat bermanfaat", "pengalaman berharga", "di era digital", "membuka wawasan", "sebuah perjalanan".
- **Why it fails:** reads as filler and carries no information.
- **Before:**
  > Kegiatan ini memberikan pengalaman berharga yang membuka wawasan tentang dunia kerja.
- **After:**
  > Alur peninjauan kode dengan mentor memperjelas standar penamaan dan struktur modul yang dipakai tim.

### W-22 Em dash and theatrical openers

- **Pattern:** `—`, ` -- `, "Pada dasarnya", "Intinya", "Hari ini adalah hari yang penuh tantangan".
- **Rule:** replace an em dash with a period or comma. Delete openers that add no fact.

### W-23 Hyperbole and unevidenced results

- **Pattern:** "berhasil sempurna", "seluruh bug teratasi", "performa meningkat drastis".
- **Rule:** write results that can be verified (N tests pass, endpoint X returns 200). Numbers only from the evidence.
- **Before:**
  > Performa query meningkat drastis.
- **After:**
  > Query daftar pesanan ditambah indeks pada kolom `created_at`, waktu respons turun dari 1,2 detik menjadi 0,3 detik.
  > (only if that figure is in the evidence or notes)

## Structure

### W-30 Activities as bullets

- **Rule:** 3 to 5 lines, each starting with `- `, one activity per line, one sentence: what was done and the result. Merge commits and prompts that belong to one piece of work.

### W-33 Outline level only

- **Pattern:** routine steps and small fixes listed as their own activities: pulling the latest changes, renaming a file, fixing a typo, running a command, retrying a failed step, installing a dependency.
- **Why it fails:** the mentor wants the big picture of the day. Small steps bury the real outcomes and make the report read like a shell history.
- **Rule:** report only the major outcomes: a feature built, a design decided, a problem investigated, a document written, a deployment done. Fold small steps into the outcome they serve or drop them. Test: if removing the line would not change what the mentor understands about the day, drop it. Same for lessons and struggles: one or two main points, not every hiccup.
- **Before:**
  > - Menarik perubahan terbaru dari repositori.
  > - Memperbaiki salah ketik pada README.
  > - Mengganti nama berkas konfigurasi.
  > - Membuat modul autentikasi berbasis JWT.
- **After:**
  > - Membuat modul autentikasi berbasis JWT beserta pengujiannya.

### W-31 Lessons and struggles in one paragraph

- **Rule:** one paragraph, 2 to 4 sentences, no bullets, no blank lines. At least 100 characters.

### W-32 At least 100 characters per part

- **Rule:** form validation. Add real detail, not filler. If the evidence is truly thin, ask the user.

## Safety

### W-40 No secrets

- **Rule:** never write tokens, passwords, internal URLs, IPs, confidential client names, or personal data seen in chats or commits. Refer to them generically ("layanan autentikasi", "basis data staging").

## Text that enters the form

### W-50 No meta

- **Rule:** form text is report content only. Forbidden: `[INFERENCE ...]`, "Catatan:", "Perlu konfirmasi", greetings, chat closers ("Semoga membantu"). Notes for the user go outside the draft.

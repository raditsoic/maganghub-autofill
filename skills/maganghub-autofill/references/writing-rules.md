# Writing rules for the daily report

Each rule has an ID (`W-xx`) referenced from `SKILL.md`. Rule explanations are concise; every **Before** and **After** sample is written in natural Indonesian because the report itself is written in Indonesian. Pattern format: **Pattern**, **Why it fails**, **Before**, **After**.

| Group | Rules |
|---|---|
| Facts | W-01 facts only from evidence, W-02 real struggles only, W-03 lessons follow activities |
| Perspective | W-10 no person perspective (natural impersonal), W-11 active phrasing (no stiff `di-` passives) |
| Language | W-20 natural semi-formal Indonesian & familiar tech terms, W-21 empty vocabulary, W-22 em dash and theatrical openers, W-23 hyperbole, W-24 humanized technical explanations |
| Structure | W-30 activity bullets, W-31 one paragraph, W-32 100 characters, W-33 outline level only |
| Safety | W-40 no secrets |
| Form text | W-50 no meta |

> [!IMPORTANT]
> **Never invent facts** (W-01). A rewrite adds no activity, tool, number, person, or incident that is not in the evidence or the user's notes. If detail is missing, ask the user or write a shorter honest version.

> [!TIP]
> **Keep it impersonal, not robotic.** Avoiding "saya" does not mean writing like a legal document. Use real feature, module, tool, and outcome names from the evidence, written in clear, flowing Indonesian that a mentor can read effortlessly.

## Facts

### W-01 Facts only from evidence

- **Pattern:** an activity, result, or struggle that appears neither in the `collect_today.py` output nor in the user's notes.
- **Why it fails:** the mentor reads the report and uses it for evaluation. A fabrication sounds convincing but is false, and it is always a defect even when it reads well.
- **Before:**
  > Mengikuti rapat koordinasi dengan tim produk untuk membahas roadmap kuartal depan.
  > (no meeting in the evidence or notes)
- **After:**
  > Merancang struktur tabel `users` dan `sessions` di database untuk kebutuhan fitur login.
  > (taken from a real commit or prompt)

### W-02 Struggles only if real

- **Pattern:** a generic struggle made up from general context: "sempat kesulitan memahami konsep baru", "keterbatasan waktu".
- **Why it fails:** an invented struggle looks honest but is false. Mentors read the struggle section to find real blockers.
- **Rule:** take struggles from errors, bugs, reverts, repeated retries, or hard decisions in the evidence, or from the user's notes. If the user did not mention a struggle and none is found in the evidence, **STOP before drafting and ask the user first**—using the platform's interactive question/grill tool if available (e.g., `ask_question` on Antigravity) or a direct question in the conversation. Do not output a draft or pre-fill a "no struggle" placeholder on your own (except in `no-ask` mode). Only after the user confirms there were no struggles, write a short honest paragraph that reaches the 100-character minimum without inventing an incident (see the no-struggle day in `examples.md`).
- **Before:**
  > Kendala yang dialami berupa kesulitan memahami alur kerja yang kompleks sehingga membutuhkan waktu lebih lama.
- **After:**
  > Sempat muncul kendala ketika sistem menolak token login yang sebenarnya masih valid. Setelah ditelusuri lewat log, penyebabnya ternyata urutan middleware yang tertukar, dan masalah selesai setelah urutannya diperbaiki.

### W-03 Lessons follow activities

- **Pattern:** a lesson about something not done that day, or a claim that was not tested.
- **Why it fails:** every lesson must trace back to an activity above it.
- **Before:**
  > Dari pengerjaan hari ini, terlihat pentingnya arsitektur microservice dan Kubernetes.
  > (the day's work was form validation only)
- **After:**
  > Dari pengerjaan validasi form hari ini, terlihat pentingnya mengecek input di sisi frontend sekaligus backend. Pesan error yang jelas untuk tiap aturan validasi juga sangat membantu pengguna tahu bagian mana yang perlu diperbaiki.

## Perspective

### W-10 No person perspective (natural impersonal)

- **Pattern:** `"saya"`, `"aku"`, `"kami"`, `"kita"`, `"penulis"`, `"gue"`, `"gua"`, `"gw"`, `"lo"`, `"lu"`, `"Anda"`, or the suffix `"-ku"`.
- **Why it fails:** the report must stay impersonal with no first- or second-person pronouns.
- **Technique:** keep it natural without falling into stiff nominalizations (*"Pemahaman tentang X bertambah"*, *"Penentuan Y belum menemukan keputusan akhir"*).
  - In **activities**, open directly with an active verb (`Membangun ...`, `Memperbaiki ...`, `Berdiskusi ...`).
  - In **lessons and struggles**, focus on what happened or what became clear: *"Dari pengerjaan hari ini, terlihat bahwa..."*, *"Ternyata..."*, *"Sempat muncul kendala ketika..."*, *"Tidak ada kendala teknis yang berarti hari ini..."*.
- **Before:**
  > Hari ini saya membuat endpoint login dan saya menulis tes untuknya.
- **After:**
  > Membangun endpoint login di sisi backend lengkap dengan unit test untuk mengecek respons sukses dan gagal.

### W-11 Active phrasing, not stiff `di-` passives

- **Pattern:** activity bullets that open with a passive `di-` verb: `"Dibuat ..."`, `"Disusun ..."`, `"Dipasang ..."`, or an empty `"Dilakukan ..."`.
- **Why it fails:** passive openings read as stiff and mechanical.
- **Before:**
  > - Dibuat fitur ekspor laporan ke CSV.
  > - Dilakukan pengujian fitur.
  > - Diperbaiki format tanggal.
- **After:**
  > - Membuat fitur ekspor laporan ke format CSV agar data bisa langsung diunduh.
  > - Menguji fitur ekspor dengan 3 contoh data sekaligus memperbaiki format tanggal yang sempat keliru.
- **Scope:** applies to the opening verb of every activity bullet. Any natural active verb works (`Membuat`, `Membangun`, `Memperbaiki`, `Berdiskusi`, `Mempelajari`, `Mencoba`, `Melanjutkan`)—vary them so the list does not feel repetitive. Inside lessons and struggles, passive clauses are fine when natural.

## Language

### W-20 Natural semi-formal Indonesian, familiar tech terms

- **Pattern:** mixing chat slang (`gue/lo`, `bgt`, `yg`, `dgn`), OR forcing stiff textbook/KBBI translations for everyday tech terms (`galat` for error, `basis data` for database, `kedaluwarsa` for expired, `sah` for valid, `variabel lingkungan` for env/environment variable, `lingkungan bersih` for clean environment, `peninjauan kode` for code review, `kait` for hook).
- **Rule:** gunakan bahasa Indonesia semi-formal yang luwes dan sopan, seperti saat melaporkan progres ke mentor. Biarkan istilah teknis yang memang lazim dipakai sehari-hari tetap dalam bentuk aslinya (`error`, `bug`, `database`, `backend`, `API`, `login`, `expired`, `valid`, `env`, `code review`, `deploy`, `unit test`).

### W-21 Empty vocabulary

- **Pattern:** `"luar biasa"`, `"sangat bermanfaat"`, `"pengalaman berharga"`, `"di era digital"`, `"membuka wawasan"`, `"sebuah perjalanan"`.
- **Why it fails:** reads as filler and carries no real information.
- **Before:**
  > Kegiatan ini memberikan pengalaman berharga yang sangat bermanfaat dan membuka wawasan tentang dunia kerja.
- **After:**
  > Lewat sesi code review bersama mentor, standar penamaan dan struktur folder yang biasa dipakai tim jadi jauh lebih jelas sehingga kode lebih mudah dibaca orang lain.

### W-22 Em dash and theatrical openers

- **Pattern:** `—`, ` -- `, `"Pada dasarnya"`, `"Intinya"`, `"Hari ini adalah hari yang penuh tantangan"`.
- **Rule:** ganti em dash dengan koma atau titik. Hapus kalimat pembuka yang dramatis dan tidak menambah fakta.

### W-23 Hyperbole and unevidenced results

- **Pattern:** `"berhasil sempurna"`, `"seluruh bug teratasi"`, `"performa meningkat drastis"`.
- **Rule:** tulis hasil yang wajar dan sesuai bukti. Hanya cantumkan angka kalau angka tersebut memang ada di evidence atau catatan pengguna.
- **Before:**
  > Performa query meningkat drastis dan semua berjalan sempurna.
- **After:**
  > Menambahkan indeks pada kolom `created_at` di tabel pesanan sehingga waktu muat daftar pesanan turun dari 1,2 detik menjadi 0,3 detik.
  > (only if that figure is in the evidence or notes)

### W-24 Humanized technical explanations (not a raw git log)

- **Pattern:** menumpuk istilah teknis mentah tanpa konteks fungsi (*"Mengimplementasikan middleware pembaca header untuk validasi token akses pada endpoint HTTP"*), atau memakai struktur terjemahan kaku dari bahasa Inggris (*"terbukti memengaruhi"*, *"menemukan keputusan akhir"*, *"pada lingkungan bersih"*).
- **Why it fails:** walaupun pembaca paham teknis, kalimat yang terlalu kering dan penuh jargon seperti catatan mesin terasa melelahkan dan tidak alami.
- **Rule:** istilah teknis tetap boleh dipakai, tetapi **jelaskan dalam bahasa manusia yang mengalir**, kaitkan dengan fitur, tujuan, atau dampak yang dirasakan pengguna/sistem. Hindari gaya terjemahan literal dan nominalisasi berlebih (`Pemahaman tentang ... bertambah`, `Pelaksanaan ... berjalan`).
- **Before:**
  > - Memperbaiki urutan middleware yang menyebabkan token valid ditolak.
  >
  > Urutan middleware pada permintaan HTTP terbukti memengaruhi hasil validasi token.
- **After:**
  > - Memperbaiki bug di alur login yang sempat menolak token valid karena urutan pengecekan middleware tertukar.
  >
  > Dari masalah hari ini, terlihat jelas bahwa urutan middleware di backend sangat krusial, karena kalau urutannya salah, pengecekan autentikasi bisa langsung menolak akses meskipun data login pengguna sudah benar.

## Structure

### W-30 Activities as bullets

- **Rule:** 3 to 5 lines, each starting with `- `, one main activity per line, one clear sentence: what was done and why/the outcome. Merge commits and prompts that belong to one piece of work.

### W-33 Outline level only

- **Pattern:** routine steps and small fixes listed as their own activities: pulling the latest changes, renaming a file, fixing a typo, running a command, retrying a failed step, installing a dependency.
- **Why it fails:** the mentor wants the big picture of the day. Small steps bury the real outcomes and make the report read like a shell history.
- **Rule:** report only the major outcomes: a feature built, a design decided, a bug investigated, a document written, a deployment done. Fold small steps into the outcome they serve or drop them. Test: if removing the line would not change what the mentor understands about the day, drop it. Same for lessons and struggles: one or two main points, not every hiccup.
- **Before:**
  > - Menarik perubahan terbaru dari repositori.
  > - Memperbaiki salah ketik pada README.
  > - Mengganti nama berkas konfigurasi.
  > - Membuat modul autentikasi berbasis JWT.
- **After:**
  > - Membangun fitur autentikasi login berbasis JWT lengkap dengan pengujiannya.

### W-31 Lessons and struggles in one paragraph

- **Rule:** one paragraph, 2 to 4 sentences, no bullets, no blank lines. At least 100 characters.

### W-32 At least 100 characters per part

- **Rule:** form validation. Add real context or detail from the evidence, not filler. If the evidence is truly thin, ask the user.

## Safety

### W-40 No secrets

- **Rule:** never write tokens, passwords, internal URLs, IPs, confidential client names, or personal data seen in chats or commits. Refer to them generically ("layanan autentikasi", "database staging").

## Text that enters the form

### W-50 No meta

- **Rule:** form text is report content only. Forbidden: `[INFERENCE ...]`, `"Catatan:"`, `"Perlu konfirmasi"`, greetings, chat closers (`"Semoga membantu"`). Notes for the user go outside the draft.

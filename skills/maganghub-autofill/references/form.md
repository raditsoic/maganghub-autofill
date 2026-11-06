# MagangHub daily report form

> [!IMPORTANT]
> The skill fills the form and stops. It never ticks the confirmation checkbox and never clicks **Simpan dan Kirim**; only the user does, because submitting also records attendance.

The daily report lives on the **Monev** portal, not on the main MagangHub dashboard. The official PDF guide (v1.0, 2025-10) describes an older flow; the flow below was verified against the live site on 2026-11-06.

The UI is Indonesian; labels are quoted verbatim and must be matched verbatim.

## Flow on the site (verified)

1. Open `https://monev.maganghub.kemnaker.go.id/dashboard/evaluasi` and log in. A logged-in browser shows the tabs Beranda, Riwayat, Perkembangan, Akun.
2. Go to `https://monev.maganghub.kemnaker.go.id/dashboard` (or click the **Beranda** tab).
3. On Beranda, the "Hari Ini" card shows the date and either "Laporan hari ini belum diisi" or a submitted state. Click **Isi Laporan Hari Ini**.
4. This opens `https://monev.maganghub.kemnaker.go.id/dashboard/riwayat?date=YYYY-MM-DD&view=edit` with the form **Tambah laporan · <date>**.
5. The form has:
   - **Kehadiran** (defaults to "Hadir"; location check "Lokasi berhasil diakses" shown above it)
   - **Uraian aktivitas**, **Pembelajaran yang diperoleh**, **Kendala yang dialami**: three textareas, each at least 100 characters (max 5000), with a live character counter
   - a confirmation checkbox: "Saya menyatakan telah meninjau dan memastikan isian laporan ini sudah benar"
   - buttons **Batal** and **Simpan dan Kirim** (there is no draft button)
6. Attendance is recorded together with the report. Submitting is therefore also an attendance action: only the user submits.

Past dates: open `/dashboard/riwayat?date=YYYY-MM-DD&view=edit` for the target date, or use the calendar on the **Riwayat** tab. Calendar states: Hadir disetujui, Izin disetujui, Tidak Hadir, Kehadiran Ditolak, Perlu Tindakan Anda, Menunggu Tindakan Mentor, Belum Diisi, Hari Libur. Fill only a day that is "Belum Diisi" or "Perlu Tindakan Anda"; never overwrite a submitted report.

## Field mapping

| Form label | JSON key | Textarea placeholder | Shape |
|---|---|---|---|
| Uraian aktivitas | `aktivitas` | `Tulis uraian aktivitas minimal 100 karakter` | bulleted lines starting with `- ` |
| Pembelajaran yang diperoleh | `pelajaran` | `Tulis ilmu/pembelajaran yang diperoleh minimal 100 karakter` | one paragraph |
| Kendala yang dialami | `kendala` | `Tulis kendala/hambatan yang dialami minimal 100 karakter` | one paragraph |

## Browser procedure

Use the session's browser tool. Ids such as `input-v-7` are generated; select textareas by placeholder, e.g. `tab.fill("placeholder/Tulis uraian aktivitas minimal 100 karakter", text)`.

1. **Preflight, do not wait for login.** Open the Monev URL in the agent's own tab. Logged in = the page shows the tabs Beranda, Riwayat, Perkembangan, Akun. Otherwise stop immediately (no polling, no waiting loop), output the draft per field for copying, and tell the user to log in once in that browser and rerun. Never ask for or type credentials.
2. Navigate to Beranda, click **Isi Laporan Hari Ini** (or open the dated `riwayat` URL).
3. Wait for the form, then fill, in the same cell: `await tab.waitForSelector("textarea", { timeout: 20000 })`, then `tab.fill` for each textarea. The SPA shows "Memuat halaman" for 1 to 4 seconds after navigation and has no textareas until it finishes. `tab.fill` updates the framework state and the character counter; a native value setter or `execCommand` can leave the counter at "0 / 5000" and the field invalid.
4. Read every textarea back with `tab.evaluate(() => [...document.querySelectorAll("textarea")].map(t => t.value))` and compare with the draft. Confirm the character counter and that no validation message is shown.
5. **Do not tick the confirmation checkbox. Do not click Simpan dan Kirim.** Tell the user the form is filled and that they must tick the checkbox and submit.

## Relay notes (Brave or Chrome)

- Install once: `omp browser-relay install`, then load the extension folder unpacked in `brave://extensions` (Developer mode on). With WSL, the folder is `\\wsl.localhost\<distro>\home\<user>\.omp\browser-relay\extension`.
- Open with `browser.open({ name, url, app: { relay: true }, persist: true })`. The tab opens in the background in an `omp` tab group; the user's other tabs are untouched.
- `tab.observe()` can stall (30 s timeout) on a background relay tab. Prefer `tab.text()`, `tab.evaluate`, and selector-based `tab.fill`/`tab.click`.
- An aborted run can leave the tab with a detached frame. Close it (`browser.close({ name })`) and open a fresh one.
- **Never call `browser.open({ url })` again on a tab that is already open.** It re-navigates the tab, which reloads the SPA, wipes anything filled, and often leaves a detached frame. Open once, then reach the tab with `browser.tab(name)` and navigate with `tab.goto` only when needed. If a cell fails with a detached frame, close the tab and open a fresh one (verified 2026-11-06: a repeated `open({ url })` per cell kept the form at "Memuat halaman" with zero textareas, so every `tab.fill` timed out).
- Do navigation, `waitForSelector`, fill, and read-back in one cell, then do nothing else to that page until the user has reviewed it. A filled form that is not touched stayed stable for 9 seconds of sampling.
- Avoid pasting page text that contains personal data (bank account, email) into chat. Read only what the task needs.

If the layout differs from this description: follow the visible labels and tell the user what differs. If there is no browser tool: show the final text per field for copying.

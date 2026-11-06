# Report examples

> [!NOTE]
> Not for copying. Use them to read tone, rhythm, and level of specificity. Facts always come from that day's evidence. The framing is English; the report blocks are Indonesian because that is the output language.

## Normal workday, struggle present in the evidence

Evidence: 3 commits (`feat: endpoint login JWT`, `test: validasi token`, `fix: urutan middleware`), chat prompt about a rejected token.

**Uraian aktivitas**
```
- Dibuat endpoint login berbasis JWT pada layanan backend.
- Ditulis tes unit untuk validasi token akses dan token kedaluwarsa.
- Diperbaiki urutan middleware yang menyebabkan token valid ditolak.
```

**Pembelajaran yang diperoleh**
```
Pemahaman tentang alur token akses dan masa berlaku token bertambah, termasuk cara menguji token kedaluwarsa secara terpisah dari alur login. Urutan middleware pada permintaan HTTP juga terbukti memengaruhi hasil validasi.
```

**Kendala yang dialami**
```
Token yang sah ditolak oleh layanan karena middleware autentikasi berjalan sebelum middleware pembaca header. Masalah ditelusuri lewat log permintaan dan diselesaikan dengan menukar urutan keduanya.
```

## Day without struggle (user says there were none)

Evidence: 1 commit (`docs: perbarui README`), prompt about writing installation docs. User: "no struggles".

**Uraian aktivitas**
```
- Diperbarui README proyek dengan langkah instalasi dan contoh penggunaan.
- Disusun daftar variabel lingkungan yang dibutuhkan untuk menjalankan layanan secara lokal.
- Dicoba ulang seluruh langkah instalasi pada lingkungan bersih untuk memastikan dokumentasi akurat.
```

**Pembelajaran yang diperoleh**
```
Dokumentasi instalasi perlu diuji langsung pada lingkungan bersih agar langkah yang terlewat terlihat. Pemisahan antara variabel wajib dan opsional mempermudah pengguna baru menyiapkan layanan.
```

**Kendala yang dialami**
```
Tidak ada kendala teknis berarti pada kegiatan hari ini. Seluruh langkah instalasi berjalan sesuai dokumentasi pada percobaan di lingkungan bersih tanpa perlu perbaikan tambahan.
```

## Day without commits, chat and user notes only

Evidence: chat prompt about studying the database schema; user note: "meeting with mentor about the orders table design".

**Uraian aktivitas**
```
- Dipelajari skema basis data modul pesanan untuk memahami relasi antar tabel.
- Dilakukan pembahasan desain tabel pesanan bersama mentor.
- Disusun rancangan awal kolom dan relasi tabel pesanan berdasarkan hasil pembahasan.
```

**Pembelajaran yang diperoleh**
```
Pemahaman tentang normalisasi dan relasi satu-ke-banyak antara pesanan dan item pesanan bertambah. Pembahasan dengan mentor memperjelas alasan memisahkan data harga saat transaksi dari data harga produk.
```

**Kendala yang dialami**
```
Penentuan struktur penyimpanan harga historis belum menemukan keputusan akhir pada hari ini. Beberapa opsi sudah didiskusikan dan akan dipilih setelah mempertimbangkan kebutuhan laporan.
```

This struggle is valid only if it really appears in the evidence or the user's notes.

## Bad example (do not imitate)

```
Hari ini saya sangat senang bisa belajar banyak hal baru yang luar biasa. Saya membuat fitur dengan sempurna dan semua berjalan lancar. Semoga hari esok lebih baik!
```

Violations: W-10 (saya), W-21 (empty vocabulary), W-23 (hyperbole), W-50 (chat closer), no facts (W-01).

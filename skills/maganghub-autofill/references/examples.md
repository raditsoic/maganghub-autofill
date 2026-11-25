# Report examples

> [!NOTE]
> Not for copying. Use them to read tone, rhythm, and level of specificity. Facts always come from that day's evidence. The framing is English; the report blocks are natural Indonesian because that is the output language.

## Normal workday, struggle present in the evidence

Evidence: 3 commits (`feat: endpoint login JWT`, `test: validasi token`, `fix: urutan middleware`), chat prompt about a rejected token.

**Uraian aktivitas**
```
- Membangun endpoint login berbasis JWT di sisi backend untuk menangani proses autentikasi pengguna.
- Menambahkan unit test untuk memastikan token yang valid bisa diterima dan token yang sudah expired langsung ditolak.
- Memperbaiki bug di alur login yang sempat menolak token valid karena urutan middleware tertukar.
```

**Pembelajaran yang diperoleh**
```
Dari pengerjaan fitur login hari ini, saya jadi lebih paham bagaimana alur token JWT bekerja, termasuk pentingnya menguji kasus token expired secara terpisah agar error lebih mudah terdeteksi sejak awal. Saya juga belajar bahwa urutan middleware di backend sangat berpengaruh karena posisi yang keliru bisa membuat request yang valid langsung ditolak.
```

**Kendala yang dialami**
```
Saya sempat mengalami kendala ketika sistem menolak token yang sebenarnya masih valid saat pengujian login. Setelah saya telusuri lewat log request, penyebabnya ternyata middleware autentikasi jalan lebih dulu sebelum middleware yang membaca header, dan masalah selesai setelah urutannya saya tukar.
```

## Day without struggle (user says there were none)

Evidence: 1 commit (`docs: perbarui README`), prompt about writing installation docs. User: "no struggles".

**Uraian aktivitas**
```
- Memperbarui README proyek dengan panduan instalasi dan contoh pemakaian yang lebih mudah diikuti.
- Merapikan daftar konfigurasi env yang perlu disiapkan agar layanan bisa dijalankan di komputer lokal.
- Mencoba ulang seluruh langkah instalasi dari awal untuk memastikan panduannya akurat dan tidak ada langkah yang terlewat.
```

**Pembelajaran yang diperoleh**
```
Hari ini saya belajar bahwa dokumentasi instalasi memang perlu dicoba langsung dari awal, bukan hanya ditulis dari ingatan, supaya langkah kecil yang sering terlewat bisa langsung ketahuan. Memisahkan konfigurasi env yang wajib dan opsional juga jauh lebih membantu orang baru saat pertama kali setup proyek.
```

**Kendala yang dialami**
```
Hari ini saya tidak mengalami kendala teknis yang berarti. Seluruh langkah instalasi yang saya tulis di dokumentasi berjalan lancar saat dicoba ulang dari awal tanpa ada error atau perbaikan tambahan.
```

## Day without commits, chat and user notes only

Evidence: chat prompt about studying the database schema; user note: "meeting with mentor about the orders table design".

**Uraian aktivitas**
```
- Mempelajari struktur database pada modul pesanan untuk memahami hubungan antar tabel yang sudah ada.
- Berdiskusi bersama mentor membahas rancangan tabel pesanan dan kebutuhan data yang perlu disimpan.
- Menyusun draf awal kolom dan relasi tabel pesanan berdasarkan masukan dari hasil diskusi.
```

**Pembelajaran yang diperoleh**
```
Dari diskusi hari ini, saya jadi lebih paham soal desain relasi one-to-many antara tabel pesanan dan daftar item di dalamnya. Penjelasan dari mentor juga membuat saya mengerti kenapa harga saat transaksi perlu disimpan terpisah dari harga produk agar riwayat pesanan tidak ikut berubah kalau harga produk diperbarui.
```

**Kendala yang dialami**
```
Saat diskusi tadi, saya dan mentor belum mengambil keputusan final soal cara terbaik menyimpan riwayat perubahan harga di database. Ada beberapa opsi struktur yang sudah kami bahas dan rencananya akan dipilih setelah menyesuaikan dengan kebutuhan fitur laporan nanti.
```

This struggle is valid only if it really appears in the evidence or the user's notes.

## Bad example (do not imitate)

```
Hari ini aku sangat senang bisa belajar banyak hal baru yang luar biasa. Aku membuat fitur dengan sempurna dan semua berjalan lancar. Semoga hari esok lebih baik!
```

Violations: W-10 (informal pronoun `aku`), W-21 (empty vocabulary), W-23 (hyperbole), W-50 (chat closer), no facts (W-01).

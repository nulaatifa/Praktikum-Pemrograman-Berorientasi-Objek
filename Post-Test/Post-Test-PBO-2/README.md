# Star Home of DVD & Film

Posttest 2 PBO (Python) - Relasi UML (Asosiasi, Agregasi, Komposisi) & Inheritance.

**Cara menjalankan**

    python posttest2_2509106033_Nurullatifa.py

Program langsung menampilkan demonstrasi pengujian di terminal.

**Gambaran program**

Masih tema yang sama: katalog film, anggota, admin, dan transaksi sewa-kembali dengan denda otomatis. Di posttest ini ditambahkan inheritance (`Film` sebagai superclass, `FilmBioskop` dan `FilmSeries` sebagai subclass) serta tiga relasi UML yang sudah diajarkan: asosiasi, agregasi, dan komposisi.

Waktu masih disederhanakan menjadi "hari ke-N". Lama pinjam 3 hari, denda Rp5000 per hari.

**Struktur class**

- `Film` (superclass): atribut kelas `nama_toko`, `total_film`; atribut protected `_status` yang memang dibuat agar bisa diakses dan diubah langsung oleh subclass; atribut private `__kode_registrasi` yang murni rahasia milik `Film` sendiri, hanya bisa dilihat lewat `tampilkan_kode_registrasi()`.
- `FilmBioskop(Film)`: menambah atribut `durasi_menit` dan method baru `tandai_rusak()` yang mengubah `_status` secara langsung.
- `FilmSeries(Film)`: menambah atribut `jumlah_episode` dan meng-override `ubah_status()` agar bisa menerima status "Tamat Musim" yang tidak dikenal `Film`.
- `Anggota`: atribut kelas `nama_rental`; atribut instance `id_anggota`, `nama`.
- `Admin`: atribut kelas `role`; atribut private `__kode`; method `layani_peminjaman()` dan `ubah_judul()`.
- `Katalog`: menyimpan daftar `Film`.
- `CatatanAktivitas`: satu baris log (PINJAM atau KEMBALI) milik satu `Transaksi`.
- `Transaksi`: atribut kelas `denda_per_hari`, `lama_pinjam`; mencatat riwayat lewat `CatatanAktivitas`.

**Relasi UML yang diterapkan**

- Asosiasi: `Admin.layani_peminjaman()` menerima `Anggota` dan `Film` hanya sebagai parameter, tidak disimpan sebagai atribut tetap milik `Admin`.
- Agregasi: `Katalog` menampung daftar `Film` yang dibuat di luar dirinya. Terbukti kalau objek katalog dihapus, film yang tadinya terdaftar di situ tetap hidup dan bisa dipakai sendiri.
- Komposisi: `Transaksi` membuat `CatatanAktivitas` sendiri di dalam `pinjam()` dan `kembalikan()`, tidak pernah dibuat dari luar.
- Pewarisan: `FilmBioskop` dan `FilmSeries` sama-sama turunan `Film`.

**Inheritance**

`Film` sebagai superclass, `FilmBioskop` dan `FilmSeries` sebagai subclass, keduanya memanggil `super().__init__()` saat dibuat. `FilmSeries` meng-override `ubah_status()` dengan aturan berbeda dari `Film`. Atribut `_status` bisa diakses langsung oleh subclass, sedangkan `__kode_registrasi` tetap eksklusif milik `Film`.

**Panduan pengujian**

Jalankan program, lalu perhatikan 8 bagian output:

1. Inheritance: superclass dan subclass, `total_film` lewat `super().__init__()`, uji `isinstance` dan `issubclass`.
2. Method overriding dan atribut protected: `info()` berbeda tiap subclass, `tandai_rusak()` mengubah `_status` langsung, `FilmSeries` boleh "Tamat Musim" tapi `FilmBioskop` ditolak.
3. Atribut private: kode registrasi hanya bisa dilihat lewat method `Film`, tidak bisa diakses langsung dengan nama aslinya.
4. Agregasi: film didaftarkan ke katalog, katalog dihapus, film tetap hidup sendiri.
5. Asosiasi: Admin melayani peminjaman memakai objek `Anggota` dan `Film` yang diterima sebagai parameter, termasuk pesan "Sorry" saat film sedang dipinjam.
6. Komposisi: setelah `kembalikan()`, `cetak_riwayat()` menampilkan log PINJAM dan KEMBALI yang dibuat di dalam `Transaksi`.
7. Demonstrasi class method `ganti_denda()` dan static method `hitung_denda()`.
8. Update judul lewat Admin dan uji validasi (judul kosong, kode admin kurang dari 4 karakter).
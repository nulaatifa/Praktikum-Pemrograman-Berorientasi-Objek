# Star Home of DVD & Film

Sistem Pengelolaan Katalog dan Peminjaman DVD/Film. Posttest 1 PBO (Python).

**Cara menjalankan**

    python posttest1_2509106033_Nurullatifa.py

Program langsung menampilkan demonstrasi pengujian di terminal.

**Gambaran program**

Admin dapat menambah, melihat, mengubah, dan menghapus film di katalog, serta menambah pelanggan. Pelanggan dapat melihat katalog beserta statusnya dan menyewa film. Status film berubah antara Tersedia dan Sedang Dipinjam. Jika film sedang dipinjam, muncul pesan "Sorry, lagi dipinjam". Jika film dikembalikan melewati tenggat, denda dihitung otomatis.

Waktu disederhanakan menjadi "hari ke-N". Lama pinjam 3 hari, denda Rp5000 per hari.

**Struktur class**

- `Film`: atribut kelas `nama_toko`, `total_film`; atribut instance `id_film`, `judul`, `genre`; atribut private `__status`.
- `Anggota`: atribut kelas `nama_rental`; atribut instance `id_anggota`, `nama`.
- `Admin`: atribut kelas `role`; atribut instance `nama`; atribut private `__kode`; method CRUD film dan tambah pelanggan.
- `Transaksi`: atribut kelas `denda_per_hari`, `lama_pinjam`; logika sewa, kembali, dan denda.

Class saling berinteraksi (Transaksi memakai objek Anggota dan Film, Admin mengelola objek Film dan Anggota) tanpa inheritance.

**Jenis method**

- Instance method: `Film.info()`, `Anggota.info()`, `Anggota.lihat_katalog()`, `Admin.tambah_film()`, `Admin.ubah_judul()`, `Admin.hapus_film()`, `Transaksi.pinjam()`, `Transaksi.kembalikan()`.
- Class method: `Film.dari_dict()`, `Transaksi.ganti_denda()`.
- Static method: `Film.validasi_judul()`, `Transaksi.hitung_denda()`.

**Getter dan setter (validasi)**

- `Film.status`: hanya menerima "Tersedia" atau "Sedang Dipinjam".
- `Admin.kode`: minimal 4 karakter.

Input yang tidak valid ditolak dan mencetak pesan peringatan.

**Panduan pengujian**

Jalankan program, lalu perhatikan 8 bagian output:

1. Login admin (data benar dan salah).
2. Create: tambah film dan pelanggan (judul kosong ditolak). Minimal 2 objek untuk tiap class.
3. Read: katalog beserta status.
4. Sewa film, termasuk pesan Sorry saat film sedang dipinjam.
5. Kembalikan film: terlambat (denda) dan tepat waktu.
6. Demonstrasi class method dan static method.
7. Update dan Delete film (hapus film yang sedang dipinjam ditolak).
8. Uji setter dengan data valid dan tidak valid.
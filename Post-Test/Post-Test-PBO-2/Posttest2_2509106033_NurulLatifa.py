class Film:
    nama_toko = "Star Home of DVD & Film"
    total_film = 0

    def __init__(self, id_film, judul, genre):
        self.id_film = id_film
        self.judul = judul
        self.genre = genre
        self._status = "Tersedia"
        self.__kode_registrasi = "REG-" + id_film
        Film.total_film += 1

    def info(self):
        print(f"[{self.id_film}] {self.judul} | {self.genre} | {self._status}")

    def ubah_status(self, status_baru):
        if status_baru == "Tersedia" or status_baru == "Sedang Dipinjam":
            self._status = status_baru
        else:
            print(f"Status '{status_baru}' tidak valid, perubahan ditolak.")

    def tampilkan_kode_registrasi(self):
        print(f"Kode registrasi (khusus Film): {self.__kode_registrasi}")

    @staticmethod
    def validasi_judul(judul):
        return judul.strip() != ""


class FilmBioskop(Film):
    def __init__(self, id_film, judul, genre, durasi_menit):
        super().__init__(id_film, judul, genre)
        self.durasi_menit = durasi_menit

    def info(self):
        super().info()
        print(f"    Durasi: {self.durasi_menit} menit")

    def tandai_rusak(self):
        self._status = "Perlu Servis"
        print(f"'{self.judul}' ditandai perlu servis.")


class FilmSeries(Film):
    def __init__(self, id_film, judul, genre, jumlah_episode):
        super().__init__(id_film, judul, genre)
        self.jumlah_episode = jumlah_episode

    def info(self):
        super().info()
        print(f"    Jumlah Episode: {self.jumlah_episode}")

    def ubah_status(self, status_baru):
        if status_baru == "Tamat Musim":
            self._status = status_baru
            print(f"'{self.judul}' ditandai tamat musim, menunggu musim berikutnya.")
        else:
            super().ubah_status(status_baru)


class Anggota:
    nama_rental = "Star Home of DVD & Film"

    def __init__(self, id_anggota, nama):
        self.id_anggota = id_anggota
        self.nama = nama

    def info(self):
        print(f"[{self.id_anggota}] {self.nama}")


class Admin:
    role = "Administrator"

    def __init__(self, nama, kode):
        self.nama = nama
        self.__kode = ""
        self.kode = kode

    @property
    def kode(self):
        return "*" * len(self.__kode)

    @kode.setter
    def kode(self, kode_baru):
        if len(kode_baru) < 4:
            print("Kode minimal 4 karakter, perubahan ditolak.")
        else:
            self.__kode = kode_baru

    def login(self, nama, kode):
        return nama == self.nama and kode == self.__kode

    def layani_peminjaman(self, anggota, film, id_sewa, hari_sewa):
        print(f"Admin {self.nama} melayani peminjaman untuk {anggota.nama}...")
        transaksi = Transaksi(id_sewa, anggota, film, hari_sewa)
        transaksi.pinjam()
        return transaksi

    def ubah_judul(self, film, judul_baru):
        if Film.validasi_judul(judul_baru):
            film.judul = judul_baru
            print(f"Judul film {film.id_film} diubah menjadi '{judul_baru}'.")
        else:
            print("Judul baru tidak boleh kosong, perubahan ditolak.")


class Katalog:
    def __init__(self, nama):
        self.nama = nama
        self._daftar_film = []

    def tambah_film(self, film):
        self._daftar_film.append(film)
        print(f"Film '{film.judul}' ditambahkan ke {self.nama}.")

    def keluarkan_film(self, film):
        if film._status == "Sedang Dipinjam":
            print(f"Film '{film.judul}' sedang dipinjam, tidak bisa dikeluarkan dari katalog.")
            return
        self._daftar_film.remove(film)
        print(f"Film '{film.judul}' dikeluarkan dari {self.nama}.")

    @property
    def total_film(self):
        return len(self._daftar_film)

    def tampilkan(self):
        print(f"\nKatalog {self.nama} - Total: {self.total_film} film")
        for film in self._daftar_film:
            film.info()


class CatatanAktivitas:
    def __init__(self, id_catatan, aktivitas, keterangan):
        self.id_catatan = id_catatan
        self.aktivitas = aktivitas
        self.keterangan = keterangan

    def __str__(self):
        return f"[{self.id_catatan}] {self.aktivitas} - {self.keterangan}"


class Transaksi:
    denda_per_hari = 5000
    lama_pinjam = 3

    def __init__(self, id_sewa, anggota, film, hari_sewa):
        self.id_sewa = id_sewa
        self.anggota = anggota
        self.film = film
        self.hari_sewa = hari_sewa
        self.tenggat = hari_sewa + Transaksi.lama_pinjam
        self._riwayat = []

    def _catat(self, aktivitas, keterangan):
        id_baru = f"LOG-{len(self._riwayat) + 1:03d}"
        self._riwayat.append(CatatanAktivitas(id_baru, aktivitas, keterangan))

    def pinjam(self):
        if self.film._status == "Sedang Dipinjam":
            print(f"Sorry, '{self.film.judul}' lagi dipinjam nih. Coba film lain dulu ya!")
            return False
        self.film.ubah_status("Sedang Dipinjam")
        self._catat("PINJAM", f"hari ke-{self.hari_sewa}, tenggat hari ke-{self.tenggat}")
        print(f"{self.anggota.nama} menyewa '{self.film.judul}' pada hari ke-{self.hari_sewa}. "
              f"Tenggat kembali: hari ke-{self.tenggat}.")
        return True

    def kembalikan(self, hari_kembali):
        terlambat = hari_kembali - self.tenggat
        denda = Transaksi.hitung_denda(terlambat, Transaksi.denda_per_hari)
        self.film.ubah_status("Tersedia")
        self._catat("KEMBALI", f"hari ke-{hari_kembali}, denda Rp{denda}")
        print(f"{self.anggota.nama} mengembalikan '{self.film.judul}' pada hari ke-{hari_kembali}.")
        if denda > 0:
            print(f"Terlambat {terlambat} hari, denda Rp{denda}.")
        else:
            print("Tepat waktu, tidak ada denda.")

    def cetak_riwayat(self):
        print(f"--- Riwayat Transaksi {self.id_sewa} ---")
        for catatan in self._riwayat:
            print(f"  {catatan}")

    @classmethod
    def ganti_denda(cls, tarif_baru):
        cls.denda_per_hari = tarif_baru
        print(f"Denda per hari sekarang Rp{cls.denda_per_hari}.")

    @staticmethod
    def hitung_denda(terlambat, tarif):
        if terlambat <= 0:
            return 0
        return terlambat * tarif


print("=== 1. INHERITANCE: SUPERCLASS & SUBCLASS ===")
film1 = FilmBioskop("F001", "Interstellar", "Sci-Fi", 169)
film2 = FilmBioskop("F002", "The Dark Knight", "Action", 152)
film3 = FilmSeries("F003", "Stranger Things", "Thriller", 42)
film4 = FilmSeries("F004", "Demon Slayer", "Action", 26)
print("Total film (atribut kelas Film, terhitung lewat super().__init__()):", Film.total_film)
print("film1 adalah Film?       ", isinstance(film1, Film))
print("FilmSeries subclass Film?", issubclass(FilmSeries, Film))

print("\n=== 2. METHOD OVERRIDING & ATRIBUT PROTECTED ===")
film1.info()
film3.info()
film1.tandai_rusak()
film1.info()
film3.ubah_status("Tamat Musim")
film3.info()
film1.ubah_status("Tamat Musim")

print("\n=== 3. ATRIBUT PRIVATE (EKSKLUSIF SUPERCLASS) ===")
film1.tampilkan_kode_registrasi()
film3.tampilkan_kode_registrasi()

print("\n=== 4. AGGREGATION: KATALOG MEMILIKI FILM ===")
katalog = Katalog("Katalog Pusat")
katalog.tambah_film(film1)
katalog.tambah_film(film2)
katalog.tambah_film(film3)
katalog.tambah_film(film4)
katalog.tampilkan()
katalog.keluarkan_film(film2)
print("Katalog dihapus dari memori...")
del katalog
print("Film tetap hidup sendiri di luar katalog (aggregation):")
film2.info()

print("\n=== 5. ASSOCIATION: ADMIN MELAYANI PEMINJAMAN ===")
admin = Admin("Nurul", "2509106033")
anggota1 = Anggota("A001", "Budi")
anggota2 = Anggota("A002", "Sari")
trx1 = admin.layani_peminjaman(anggota1, film1, "T001", 1)
admin.layani_peminjaman(anggota2, film1, "T002", 2)

print("\n=== 6. COMPOSITION: CATATAN AKTIVITAS DALAM TRANSAKSI ===")
trx1.kembalikan(6)
trx1.cetak_riwayat()

print("\n=== 7. SKENARIO TAMBAHAN ===")
trx3 = admin.layani_peminjaman(anggota2, film3, "T003", 2)
trx3.kembalikan(4)
trx3.cetak_riwayat()
Transaksi.ganti_denda(7000)
print("Hitung denda 2 hari, tarif 7000:", Transaksi.hitung_denda(2, 7000))

print("\n=== 8. UPDATE & VALIDASI ===")
admin.ubah_judul(film3, "Stranger Things (Season Akhir)")
admin.ubah_judul(film3, "   ")
admin.kode = "ab"
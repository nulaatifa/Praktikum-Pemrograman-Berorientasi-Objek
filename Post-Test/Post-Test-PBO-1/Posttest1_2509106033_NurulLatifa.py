class Film:
    nama_toko = "Star Home of DVD & Film"
    total_film = 0

    def __init__(self, id_film, judul, genre):
        self.id_film = id_film
        self.judul = judul
        self.genre = genre
        self.__status = "Tersedia"

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        if status_baru == "Tersedia" or status_baru == "Sedang Dipinjam":
            self.__status = status_baru
        else:
            print(f"Status '{status_baru}' tidak valid, perubahan ditolak.")

    def info(self):
        print(f"[{self.id_film}] {self.judul} | {self.genre} | {self.status}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["id_film"], data["judul"], data["genre"])

    @staticmethod
    def validasi_judul(judul):
        return judul.strip() != ""


class Anggota:
    nama_rental = "Star Home of DVD & Film"

    def __init__(self, id_anggota, nama):
        self.id_anggota = id_anggota
        self.nama = nama

    def info(self):
        print(f"[{self.id_anggota}] {self.nama}")

    def lihat_katalog(self, daftar_film):
        for film in daftar_film:
            film.info()


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

    def tambah_film(self, daftar_film, film):
        if Film.validasi_judul(film.judul):
            daftar_film.append(film)
            Film.total_film += 1
            print(f"Film '{film.judul}' berhasil ditambahkan.")
        else:
            print("Judul film tidak boleh kosong, film ditolak.")

    def lihat_katalog(self, daftar_film):
        for film in daftar_film:
            film.info()

    def ubah_judul(self, film, judul_baru):
        if Film.validasi_judul(judul_baru):
            film.judul = judul_baru
            print(f"Judul film {film.id_film} diubah menjadi '{judul_baru}'.")
        else:
            print("Judul baru tidak boleh kosong, perubahan ditolak.")

    def hapus_film(self, daftar_film, film):
        if film.status == "Sedang Dipinjam":
            print(f"Film '{film.judul}' sedang dipinjam, tidak bisa dihapus.")
        else:
            daftar_film.remove(film)
            Film.total_film -= 1
            print(f"Film '{film.judul}' berhasil dihapus.")

    def tambah_anggota(self, daftar_anggota, anggota):
        daftar_anggota.append(anggota)
        print(f"Pelanggan '{anggota.nama}' berhasil ditambahkan.")


class Transaksi:
    denda_per_hari = 5000
    lama_pinjam = 3

    def __init__(self, anggota, film, hari_sewa):
        self.anggota = anggota
        self.film = film
        self.hari_sewa = hari_sewa
        self.tenggat = hari_sewa + Transaksi.lama_pinjam
        self.denda = 0

    def pinjam(self):
        if self.film.status == "Sedang Dipinjam":
            print(f"Sorry, '{self.film.judul}' lagi dipinjam nih. Coba film lain dulu ya!")
            return False
        self.film.status = "Sedang Dipinjam"
        print(f"{self.anggota.nama} menyewa '{self.film.judul}' pada hari ke-{self.hari_sewa}. "
              f"Tenggat kembali: hari ke-{self.tenggat}.")
        return True

    def kembalikan(self, hari_kembali):
        terlambat = hari_kembali - self.tenggat
        self.denda = Transaksi.hitung_denda(terlambat, Transaksi.denda_per_hari)
        self.film.status = "Tersedia"
        print(f"{self.anggota.nama} mengembalikan '{self.film.judul}' pada hari ke-{hari_kembali}.")
        if self.denda > 0:
            print(f"Terlambat {terlambat} hari, denda Rp{self.denda}.")
        else:
            print("Tepat waktu, tidak ada denda.")

    @classmethod
    def ganti_denda(cls, tarif_baru):
        cls.denda_per_hari = tarif_baru
        print(f"Denda per hari sekarang Rp{cls.denda_per_hari}.")

    @staticmethod
    def hitung_denda(terlambat, tarif):
        if terlambat <= 0:
            return 0
        return terlambat * tarif


print("=== 1. LOGIN ADMIN ===")
admin1 = Admin("Nurul", "2509106033")
admin2 = Admin("Admin Cadangan", "1234")
print("Login admin1 (data benar) :", admin1.login("Nurul", "2509106033"))
print("Login admin1 (kode salah) :", admin1.login("Nurul", "salah"))

print("\n=== 2. CREATE: TAMBAH FILM & PELANGGAN ===")
film1 = Film("F001", "Interstellar", "Sci-Fi")
film2 = Film.dari_dict({"id_film": "F002", "judul": "Stranger Things", "genre": "Thriller"})
film3 = Film("F003", "Spirited Away", "Animation")
film4 = Film("F004", "   ", "Drama")
admin1.tambah_film([], film4)
daftar_film = []
admin1.tambah_film(daftar_film, film1)
admin2.tambah_film(daftar_film, film2)
admin1.tambah_film(daftar_film, film3)

anggota1 = Anggota("A001", "Budi")
anggota2 = Anggota("A002", "Sari")
daftar_anggota = []
admin1.tambah_anggota(daftar_anggota, anggota1)
admin1.tambah_anggota(daftar_anggota, anggota2)

print("\n=== 3. READ: KATALOG ===")
print(f"{Film.nama_toko} | Total film: {Film.total_film}")
print("Admin melihat katalog:")
admin1.lihat_katalog(daftar_film)
print("Pelanggan melihat katalog:")
anggota1.lihat_katalog(daftar_film)
for anggota in daftar_anggota:
    anggota.info()

print("\n=== 4. SEWA FILM ===")
trx1 = Transaksi(anggota1, film1, 1)
trx1.pinjam()
trx2 = Transaksi(anggota2, film1, 2)
trx2.pinjam()
print("Status katalog sekarang:")
admin1.lihat_katalog(daftar_film)

print("\n=== 5. KEMBALIKAN FILM ===")
print("-- Terlambat --")
trx1.kembalikan(6)
print("-- Tepat waktu --")
trx3 = Transaksi(anggota2, film2, 2)
trx3.pinjam()
trx3.kembalikan(4)

print("\n=== 6. CLASS METHOD & STATIC METHOD ===")
Transaksi.ganti_denda(7000)
print("Hitung denda 2 hari, tarif 7000 :", Transaksi.hitung_denda(2, 7000))
print("Hitung denda tepat waktu        :", Transaksi.hitung_denda(0, 7000))
print("Judul '' valid?                 :", Film.validasi_judul(""))
print("Judul 'Up' valid?               :", Film.validasi_judul("Up"))
Transaksi.ganti_denda(5000)

print("\n=== 7. UPDATE & DELETE ===")
admin1.ubah_judul(film1, "Interstellar (Remastered)")
admin1.ubah_judul(film1, "   ")
trx4 = Transaksi(anggota1, film3, 8)
trx4.pinjam()
admin1.hapus_film(daftar_film, film3)
trx4.kembalikan(9)
admin1.hapus_film(daftar_film, film3)
admin1.lihat_katalog(daftar_film)
print("Total film:", Film.total_film)

print("\n=== 8. UJI SETTER (VALID & TIDAK VALID) ===")
film1.status = "Sedang Dipinjam"
print("Status setelah input valid   :", film1.status)
film1.status = "Hilang"
print("Status setelah input invalid :", film1.status)
admin1.kode = "abcd1234"
print("Kode admin setelah input valid   :", admin1.kode)
admin1.kode = "ab"
print("Kode admin setelah input invalid :", admin1.kode)
print("Login dengan kode baru (abcd1234) :", admin1.login("Nurul", "abcd1234"))
print("Login dengan kode invalid (ab)    :", admin1.login("Nurul", "ab"))
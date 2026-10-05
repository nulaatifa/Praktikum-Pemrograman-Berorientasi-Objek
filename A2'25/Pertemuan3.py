#ASOSIASI

# class Nasabah : #sebuah class yang pake class yang lain (pakenya di method)
#     def __init__(self,nama , nomor_rekening):
#         self.nama= nama
#         self.nomor_rekening = nomor_rekening

#     def tarik_tunai(self, atm, jumlah): #atm disini class lain
#         atm.saldo_kas -= jumlah

# class MesinAtm:
#     def __init__(self, id_atm, lokasi, saldo_kas):
#         self.id_atm = id_atm
#         self.lokasi = lokasi
#         self.saldo_kas = saldo_kas

# dapa = Nasabah("Dapa", 1234567890)
# atm_pusat = MesinAtm("Pusat", "Samarinda", 5000000)

# dapa.tarik_tunai(atm_pusat, 500)

# print(atm_pusat.saldo_kas)


#AGREGASI

# class Bank :
#     def __init__(self, nama_bank, kode):
#         self.nama_bank = nama_bank
#         self.kode = kode
#         self.karyawan = []

#     def tambah_karyawan(self, karyawan):
#         self.karyawan.append(karyawan)

# class Karyawan :
#     def __init__(self, nama, nip, posisi):
#         self.nama = nama
#         self.nip = nip
#         self.posisi = posisi

# bank = Bank("Mandiri", "0001")
# dapa = Karyawan("Dapa", "12345", "Managaner")

# bank.tambah_karyawan(dapa)

# del bank
# print(dapa.nama)


#KOMPOSISIS

class Bank :
    def __init__(self, nama_bank, kode):
        self.nama_bank = nama_bank
        self.kode = kode
        self.karyawan = [] #dibuat ini untuk menampung class karyawan

    def tambah_karyawan(self, nama, nip, posisi):
        karyawan_baru = Karyawan("Dapa","12345", "Manager")
        self.karyawan.append(karyawan_baru)

class Karyawan :
    def __init__(self, nama, nip, posisi):
        self.nama = nama
        self.nip = nip
        self.posisi = posisi

bank = Bank("Mandiri", "0001")
bank.tambah_karyawan("dapa", "12345", "Manager")

del bank
print(bank.karyawan[0].nama)

        

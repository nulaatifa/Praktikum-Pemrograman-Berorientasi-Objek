
#Polimorfisme Via Pewarisan

# class AkunBank :
#     def __init__(self, nama, saldo):
#         self.nama = nama
#         self.saldo = saldo

#     def hitung_bunga(self):
#         return 0

# class Tabungan(AkunBank):
#     def hitung_bunga(self):
#         return self.saldo * 0.02
    
# class Deposito(AkunBank):
#     def hitung_bunga(self):
#         return self.saldo * 0.06

# #Polimorfisme : Satu loop akun berbeda
# daftar_akun =[Tabungan("Budi", 1000000), Deposito("Sari", 5000000)]

# for akun in daftar_akun:
#     print(f"Bunga {akun.nama}: Rp {akun.hitung_bunga():,.2f}")
    
    
#Duck Typing (Polimorfisme Tanpa Pewarisan)

# class RekeningTabungan:
#     def __init__(self,saldo):
#         self.saldo = saldo
        
#     def tarik_uang(self,jumlah):
#         if jumlah <= self.saldo:
#             self.saldo -= jumlah
#             print(f"Penarikan Rp{jumlah:,} berhasil")
#             print(f"Saldo tersisa: Rp{self.saldo:,}")
#         else:
#             print("Saldo tidak cukup.")
        
            
# class RekeningGiro:
#     def __init__(self, saldo):
#         self.saldo = saldo
        
#     def tarik_uang(self, jumlah):
#         if jumlah <= self.saldo:
#             self.saldo -= jumlah
#             print(f"Penarikan Rp{jumlah:,} dari rekening giro berhasil.")
#             print(f"Saldo tersisa: Rp{self.saldo:,}")
#         else:
#             print("Saldo tidak cukup.")

# # duck typing
# def proses_penarikan(rekening, jumlah):
#     rekening.tarik_uang(jumlah) 
    

# tabungan = RekeningTabungan(5_000_000)
# giro = RekeningGiro(10_000_000)
# proses_penarikan(tabungan, 1_000_000)
# proses_penarikan(giro, 2_000_000)  


#Abstract Base Class (ABC)

# from abc import ABC, abstractmethod

# class Transaksi(ABC):
#     @abstractmethod
#     def validasi(self):
#         """Wajib diimplementasikan oleh kelas subclass.
#         """
#         pass
    
#     @abstractmethod

#     def eksekusi(self):
#         """Wajib diimplementasikan oleh kelas anak."""
#         pass

# class TarikTunai(Transaksi):
#     def __init__(self, saldo_akun, nominal):
#         self.saldo = saldo_akun
#         self.nominal = nominal

#     def validasi(self):
#         if self.nominal > self.saldo:
#             return False
#         return True

#     def eksekusi(self):
#         if self.validasi():
#             self.saldo -= self.nominal
#             print(f"Tarik tunai berhasil. Sisa saldo: {self.saldo}")
#         else:
#             print("Saldo tidak cukup!")
            
            
# # transaksi_sukses = TarikTunai(100000, 50000)
# # transaksi_sukses.eksekusi()
            
# # Jika kita membuat kelas tapi lupa implementasi method dari ABC:
# class TransferGagal(Transaksi):
#     def validasi(self):
#         return True
    
# try:
#     transaksi_gagal = TransferGagal() # Error! eksekusi() belum diimplementasikan
# except TypeError as e:
#     print(f"Error: {e}")
# # Lupa implementasi eksekusi()!
# transaksi_sukses = TarikTunai(100000, 50000)
# transaksi_sukses.eksekusi()
# transaksi_gagal = TransferGagal()


# Can't instantiate abstract class TransferGagal without an implementation
# for abstract method 'eksekusi'

#Operator Overloading

class Rekening:
    def __init__(self, no_rek, saldo):
        self.no_rek = no_rek
        self.saldo = saldo

# Mendefinisikan operator + (__add__)
    def __add__(self, rekening_lain):
        total_saldo = self.saldo + rekening_lain.saldo
        return f"Total gabungan saldo: Rp {total_saldo:,}"

# Mendefinisikan operator > (__gt__)
    def __gt__(self, rekening_lain):
        return self.saldo > rekening_lain.saldo

# Tambahkan di dalam kelas Rekening:
    # Mendefinisikan operator - (__sub__)
    def __sub__(self, rekening_lain):
        return self.saldo - rekening_lain.saldo

# Mendefinisikan operator == (__eq__)
    def __eq__(self, rekening_lain):
        return self.no_rek == rekening_lain.no_rek

# Mendefinisikan tampilan saat di-print (__str__)
    def __str__(self):
        return f"Rekening {self.no_rek} | Saldo: Rp {self.saldo:,}"

rek_utama = Rekening("123", 5000000)
rek_cadangan = Rekening("456", 2000000)
print(rek_utama + rek_cadangan) # Memanggil __add__
print(rek_utama > rek_cadangan) # Memanggil __gt__, Output: True
print(rek_utama - rek_cadangan) # 3000000 <- __sub__ (selisih saldo)
print(rek_utama == rek_cadangan) # False <- __eq__ (no. rekening beda)
print(rek_utama) # Rekening 123 | Saldo: Rp 5,000,000 <- __str__
# Output:
# Total gabungan saldo: Rp 7,000,000
# True
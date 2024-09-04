# NIM/Nama  : 19622138/Bastian Hendramukti Suryapratama
# Tanggal   : 14 September 2022
# Deskripsi : Program penentuan kelas berdasarkan NIM

# PROGRAM PENENTUAN KELAS
# Menentukan kelas berdasarkan tiga digit terakhir NIM

# KAMUS
# digit_NIM: int

# ALGORITMA

# User memasukkan tiga digit terakhir NIM
digit_NIM = int(input("Masukkan akhiran NIM: "))

# Penentuan kelas berdasarkan tiga digit terakhir NIM
if not (1 <= digit_NIM <= 999): # cek input
    print("Masukan Anda belum benar")
elif 1 <= digit_NIM <= 100:
    if (digit_NIM % 2) == 1: # NIM ganjil
        print("Mahasiswa masuk ke kelas K1")
    else: # NIM genap
        print("Mahasiswa masuk ke kelas K2")
elif 101 <= digit_NIM <= 200:
    if (digit_NIM % 2) == 1: # NIM ganjil
        print("Mahasiswa masuk ke kelas K3")
    else: # NIM genap
        print("Mahasiswa masuk ke kelas K4")
elif 201 <= digit_NIM <= 300:
    if (digit_NIM % 2) == 1: # NIM ganjil
        print("Mahasiswa masuk ke kelas K5")
    else: # NIM genap
        print("Mahasiswa masuk ke kelas K6")
else: # rentang NIM 301 <= x <= 999
    if (digit_NIM % 2) == 1: # NIM ganjil
        print("Mahasiswa masuk ke kelas K7")
    else: # NIM genap
        print("Mahasiswa masuk ke kelas K8")

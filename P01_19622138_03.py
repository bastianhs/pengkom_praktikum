# NIM/Nama :19622138/Bastian Hendramukti Suryapratama
# Tanggal :28 September 2022
# Deskripsi :Menentukan interval beririsan atau tidak beririsan

# PROGRAM PENENTUAN INTERVAL BERIRISAN

# ALGORITMA

# User memasukkan input
# asumsi input bilangan bulat positif
a = int(input("Berat kotak A: "))
b = int(input("Berat kotak B: "))
c = int(input("Berat kotak C: "))
kapasitas = int(input("Kapasitas karung: "))

# Menentukan jumlah karung
if (a + b + c) > (kapasitas * 3):
    print("Tuan Kil tidak dapat menyimpan seluruh kotak.")
else:
    karung_case1 = 0
    if (a + b) <= kapasitas:
        if c <= kapasitas:
            karung_case1 = 2

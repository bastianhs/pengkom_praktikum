# NIM/Nama  : 19622138/Bastian Hendramukti Suryapratama
# Tanggal   : 14 September 2022
# Deskripsi : Program penentuan barang yang harus ditawarkan

# PROGRAM PENENTUAN PENAWARAN BARANG
# Program untuk menentukan barang mana yang harus ditawarkan kepada pembeli

# KAMUS
# hd_barang_a, hj_barang_a: float
# hd_barang_b, hj_barang_b: float
# hd_barang_c, hj_barang_c: float
# untung_barang_a, untung_barang_b, untung_barang_c: float

# ALGORITMA

# User memasukkan harga dasar dan harga jual
hd_barang_a = float(input("Masukkan harga dasar barang A    : "))
hj_barang_a = float(input("Masukkan harga jual barang A     : "))
hd_barang_b = float(input("Masukkan harga dasar barang B    : "))
hj_barang_b = float(input("Masukkan harga jual barang B     : "))
hd_barang_c = float(input("Masukkan harga dasar barang C    : "))
hj_barang_c = float(input("Masukkan harga jual barang C     : "))

# Menghitung keuntungan (keuntungan = harga jual - harga dasar)
untung_barang_a = hj_barang_a - hd_barang_a
untung_barang_b = hj_barang_b - hd_barang_b
untung_barang_c = hj_barang_c - hd_barang_c

# Penentuan salah satu jenis barang yang akan ditawarkan
# Barang yang akan ditawarkan adalah barang dengan keuntungan terbesar
if (untung_barang_a > untung_barang_b) and (untung_barang_a > untung_barang_c):
    print("Barang yang harus ditawarkan adalah barang A")
elif (untung_barang_b > untung_barang_a) and (untung_barang_b > untung_barang_c):
    print("Barang yang harus ditawarkan adalah barang B")
elif (untung_barang_c > untung_barang_a) and (untung_barang_c > untung_barang_b):
    print("Barang yang harus ditawarkan adalah barang C")
else: # jika ada minimal 2 barang dengan keuntungan terbesar
    print("Ada minimal 2 barang dengan keuntungan terbesar")
'''
kondisi terakhir tidak pernah terjadi
berdasarkan asumsi keuntungan tiap barang selalu berbeda
'''

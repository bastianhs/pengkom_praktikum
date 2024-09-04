# NIM/Nama: 19622138/Bastian Hendramukti Suryapratama
# Tanggal: 31 Oktober 2022
# Deskripsi: Menentukan total tinggi bangunan yang terlihat dan mencari total tinggi terbesarnya

# FOTO_TERTINGGI

# KAMUS
# besar, i, j, total, max_tinggi, max_total: int
# kota: matrix of int

# ALGORITMA

# Memasukkan besar kota
besar = int(input("Masukkan besar Kota Kompeng: "))

# Inisialisasi matriks yang menyimpan data tinggi bangunan
kota = [[0 for j in range(besar)] for i in range(besar)]

# Memasukkan data tinggi bangunan
for i in range(besar):
    for j in range(besar):
        kota[i][j] = int(input(f"Masukkan tinggi bangunan baris {i + 1} kolom {j+ 1}: "))

# Menentukan foto terbaik
# Foto terbaik adalah foto dengan total tinggi terbesar dari bangunan yang terlihat

# Menghitung total tinggi dari bagian kiri sampai bagian kanan kota
# (dari kolom pertama sampai kolom terakhir)
for j in range(besar):
    # Menghitung total tinggi dari bagian atas kota (dari baris pertama)
    total = kota[0][j]
    max_tinggi = kota[0][j]
    for i in range(1, besar):
        if kota[i][j] > max_tinggi:
            total += kota[i][j]
            max_tinggi = kota[i][j]

    if j == 0:
        # Jika total tinggi yang dihitung adalah kolom pertama,
        # total tinggi tersebut dijadikan nilai maksimum sementara
        max_total = total
    else:
        if total > max_total:
            # Jika total tinggi yang dihitung lebih dari nilai maksimum total tinggi sebelumnya,
            # total tinggi tersebut adalah nilai maksimum total tinggi yang baru
            max_total = total

    # Menghitung total tinggi dari bagian bawah kota (dari baris terakhir)
    total = kota[besar - 1][j]
    max_tinggi = kota[besar - 1][j]
    for i in range(besar - 2, -1, -1):
        if kota[i][j] > max_tinggi:
            total += kota[i][j]
            max_tinggi += kota[i][j]

    if total > max_total:
        # Jika total tinggi yang dihitung lebih dari nilai maksimum total tinggi sebelumnya,
        # total tinggi tersebut adalah nilai maksimum total tinggi yang baru
        max_total = total

# Menampilkan nilai total tinggi dari foto terbaik
print(f"Foto terbaik memiliki total tinggi: {max_total}")

# NIM/Nama: 19622138/Bastian Hendramukti Suryapratama
# Tanggal: 31 Oktober 2022
# Deskripsi: Menentukan apakah barang terbawah dari tiap tumpukan adalah barang terberat

# CEK_BARANG_TERBAWAH

# KAMUS
# M, N, i, j, col, max, row: int
# tumpukan: matrix of int
# memenuhi: bool

# ALGORITMA

# Memasukkan tinggi dan banyak tumpukan
M = int(input("Masukkan tinggi tumpukan: "))
N = int(input("Masukkan banyak tumpukan: "))

# Inisialisasi matriks M x N
tumpukan = [[0 for j in range(N)] for i in range(M)]

# Memasukkan berat masing-masing barang
for i in range(M):
    for j in range(N):
        tumpukan[i][j] = int(input(f"Masukkan berat benda pada baris ke-{i + 1} kolom ke-{j + 1}: "))

# Cek apakah susunan barang oleh Tuan Kil memenuhi perintah Tuan Leo, yaitu
# barang terbawah dari tiap tumpukan adalah barang terberat dari tumpukan tersebut

# Inisialisasi
memenuhi = True
col = 0
while memenuhi and (col < N):
    # Mencari barang terberat selain barang terbawah dari tumpukan
    max = tumpukan[0][col]
    row = 1
    while 0 < row < (M - 1):
        if tumpukan[row][col] > max:
            max = tumpukan[row][col]
        row += 1

    # Menentukan apakah susunan barang memenuhi perintah
    if tumpukan[M - 1][col] < max:
        # Jika barang terbawah dari tumpukan lebih ringan dari barang terberat di atasnya,
        # susunan barang tidak memenuhi perintah
        memenuhi = False
    else:
        # Jika masih memenuhi perintah,
        # mengecek tumpukan berikutnya sampai tumpukan terakhir
        col += 1

# Mengeluarkan hasil pengecekan
if memenuhi:
    print("Susunan tersebut memenuhi perintah Tuan Leo.")
else:
    print("Susunan tersebut tidak memenuhi perintah Tuan Leo.")

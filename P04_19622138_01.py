# NIM/Nama: 19622138/Bastian Hendramukti Suryapratama
# Tanggal: 9 November 2022
# Deskripsi: Mencari nilai maksimum dari bilangan-bilangan yang sebaris atau sekolom

# CARI_MAX

# KAMUS
# row, col, i, j, total, max_row, index_row, max_col, index_col: int
# matrix: matrix of int

# ALGORITMA

# Memasukkan ukuran matriks
row = int(input("Masukkan nilai N: "))
col = int(input("Masukkan nilai M: "))

# Memasukkan nilai ke dalam matriks
matrix = [[int(input(f"Masukkan elemen baris ke {i + 1} dan kolom ke {j + 1}: ")) for j in range(col)] for i in range(row)]

# Mencari nilai maksimum

# dari total nilai elemen sebaris
for i in range(row):
    total = 0
    for j in range(col):
        total += matrix[i][j]

    if i == 0:
        # Inisialisasi max_row dan index_row
        # mengambil dari baris pertama
        max_row = total
        index_row = 0
    else:
        if total > max_row:
            max_row = total
            index_row = i

# dari total nilai elemen sekolom
for j in range(col):
    total = 0
    for i in range(row):
        total += matrix[i][j]

    if j == 0:
        # Inisialisasi max_col dan index_col
        # mengambil dari kolom pertama
        max_col = total
        index_col = 0
    else:
        if total > max_col:
            max_col = total
            index_col = j

# Membandingkan nilai maksimum jika dicek dari tiap baris dan dari tiap kolom
# Jika maksimum dari baris >= maksimum dari kolom, keluarkan maksimum dari baris
# Jika maksimum dari baris < maksimum dari kolom, keluarkan maksimum dari kolom

if max_row >= max_col:
    print(f"Nilai maksimum sebesar {max_row} pada baris ke {index_row + 1}")
else:
    print(f"Nilai maksimum sebesar {max_col} pada kolom ke {index_col + 1}")

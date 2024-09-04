# NIM/Nama: 19622138/Bastian Hendramukti Suryapratama
# Tanggal: 9 November 2022
# Deskripsi: Memeriksa keamanan raja dari serangan kuda

# CEK_KEAMANAN_RAJA

# KAMUS
# size, i, j: int
# board: matrix of char

# ALGORITMA

# Memasukkan ukuran papan catur
size = int(input("Masukkan nilai m: "))

# Memasukkan elemen papan catur
board = [[input(f"Masukkan elemen matriks ke-{i + 1} {j + 1}: ") for j in range(size)] for i in range(size)]

# Menampilkan kondisi papan catur
print("Hasil papan catur")
for i in range(size):
    for j in range(size):
        if j < (size - 1):
            print(board[i][j], end=" ")
        else:
            print(board[i][j])

# Menentukan keamanan raja

# Menandai posisi yang aman
'''
safeposition = [[True for j in range(size)] for i in range(size)]
for i in range(size):
    for j in range(size):
'''        


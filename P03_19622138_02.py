# NIM/Nama : 19622138/Bastian Hendramukti Suryapratama
# Tanggal : 26 Oktober 2022
# Deskripsi : Memeriksa nomor baju yang tidak memiliki pasangan

# KAMUS
# n, i, min, max, count, nomor: int
# data_nomor: array of int

# ALGORITMA

# Memasukkan banyak data
n = int(input("Masukkan banyak data: "))

# Memasukkan masing-masing data
data_nomor = [0 for i in range(n)]
for i in range(n):
    data_nomor[i] = int(input(f"Masukkan data ke-{i + 1}: "))

# Mencari nomor baju terkecil dan terbesar
min = data_nomor[0]
max = data_nomor[0]
for i in range(1, n):
    if data_nomor[i] > max:
        max = data_nomor[i]
    if data_nomor[i] < min:
        min = data_nomor[i]


print("Ukuran baju yang tidak memiliki pasangan: ", end="")

# Mencari nomor baju yang tidak memiliki pasangan
count = 0
for nomor in range(min, max + 1):
    # Mencari banyaknya baju dari masing-masing nomor baju
    for i in data_nomor:
        if nomor == i:
            count += 1
    
    # Jika banyak nomor baju tersebut bilangan ganjil,
    # itulah nomor baju yang tidak memeiliki pasangan
    if (count % 2) == 1:
        print(nomor, end=" ")
    
    count = 0

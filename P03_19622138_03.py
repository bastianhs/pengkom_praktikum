# NIM/Nama : 19622138/Bastian Hendramukti Suryapratama
# Tanggal : 26 Oktober 2022
# Deskripsi : Mencari banyak grup angka terurut

# ALGORITMA

# Memasukkan banyak data
n = int(input("Masukkan banyak data: "))

# Memasukkan masing-masing data
data = [0 for i in range(n)]
for i in range(n):
    data[i] = int(input(f"Masukkan data ke-{i + 1}: "))

'''
# Mengurutkan angka dari yang terkecil hingga terbesar
for i in range(n):
    for j in range(i + 1, n):
        if data[i] > data[j]:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
'''

min_group = data[0]
max_group = data[0]

'''
count = 1
for i in data:
    if (i == (min_group - 1)) or (i == (max_group + 1)):
        min_group = i
        max_group = i
'''

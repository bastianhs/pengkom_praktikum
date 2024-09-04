# NIM/Nama: 19622138/Bastian Hendramukti Suryapratama
# Tanggal: 9 November 2022
# Deskripsi: Mencari pasangan bilangan komposit dalam range [A, B]

# CARI_BILANGAN_KOMPOSIT

# KAMUS
# A, B, i, j: int


# Fungsi komposit
def komposit(x):
    # Mengecek apakah suatu bilangan adalah bilangan komposit

    # KAMUS LOKAL
    # x, count, i: int

    # ALGORITMA

    # Menghitung banyak faktor
    count = 0
    for i in range(1, x + 1):
        if (x % i) == 0:
            count += 1

    # Cek bilangan komposit
    # Bilangan komposit adalah bilangan asli yang mempunyai lebih dari 2 faktor
    if count > 2:
        return True
    return False


# ALGORITMA

# Memasukkan range [A, B]
A = int(input("Masukkan nilai A: "))
B = int(input("Masukkan nilai B: "))

# Mencari pasangan bilangan komposit dalam range [A, B]
print("Pasangan bilangan komposit")
for i in range(A, B + 1):
    for j in range(i + 1, B + 1):
        if komposit(i) and komposit(j):
            print(f"{i} {j}")

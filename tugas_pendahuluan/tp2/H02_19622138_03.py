# NIM/Nama  : 19622138/Bastian Hendramukti Suryapratama
# Tanggal   : 5 Oktober 2022
# Deskripsi : Program mengeluarkan semua faktor prima dari suatu bilangan

# PROGRAM FAKTOR_PRIMA

# KAMUS
# N, factor, testPrime: int
# loopCekInput, existPrime, loopTestPrime, isPrime: bool

# ALGORITMA

# Memasukkan bilangan yang ingin dicari faktor primanya
# Bilangan harus bilangan asli yang lebih dari 1
loopCekInput = True
while loopCekInput:
    N = int(input("Masukkan N: "))
    if N > 1:
        loopCekInput = False
    else:
        print("N harus bilangan asli yang lebih dari 1")
        print("Perbaiki nilai N!")

# Mencari faktor prima
# Bilangan asli yang lebih dari 1 pasti memiliki faktor prima

print("Faktor primanya adalah", end=" ")
existPrime = False # awalnya belum ada faktor prima yang dikeluarkan
# Mencari faktor dari bilangan N
for factor in range(2, N + 1):
    if (N % factor) == 0: # Jika faktor ditemukan
        # Cek apakah faktor tersebut adalah faktor prima
        loopTestPrime = True
        testPrime = 2
        while loopTestPrime:
            if testPrime >= factor:
                loopTestPrime = False
                isPrime = True
            elif (factor % testPrime) == 0:
                loopTestPrime = False
                isPrime = False
            if loopTestPrime:
                testPrime += 1
        
        if isPrime: # Jika factor adalah faktor prima
            # cek apakah ada faktor prima yang sudah dikeluarkan
            if existPrime: # sudah ada
                print(", ", end=str(factor))
            else: # belum ada
                print(factor, end="")
                existPrime = True

print(".")

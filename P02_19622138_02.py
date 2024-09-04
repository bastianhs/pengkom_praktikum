# NIM/NAMA: 19622138/Bastian Hendramukti Suryapratama
# Tanggal: 12 Oktober 2022
# Deskripsi: Menghitung bilangan prima

# HITUNG_PRIMA

# KAMUS
# banyakGanjil, jumlahPrima, n, testPrime: int
# isPrime, loopPrime: bool

# ALGORITMA

# Inisialisasi
banyakGanjil = 0
jumlahPrima = 0
while banyakGanjil < 3:
    # Memasukkan bilangan untuk dianalisis
    # asumsinya bilangan yang dimasukkan adalah bilangan bulat
    # Jika 3X berturut-turut memasukkan bilangan ganjil, bilangan akan berhenti dianalisis
    n = int(input("Masukkan bilangan: "))
    if (n % 2) == 1:
        banyakGanjil += 1
    else:
        banyakGanjil = 0
    
    # Cek bilangan prima
    if n < 2: # bilangan < 2 sudah pasti bukan bilangan prima
        isPrime = False
    else:
        # Inisialisasi
        testPrime = 2
        isPrime = True
        loopPrime = True
        while loopPrime and (testPrime != n):
            if (n % testPrime) == 0:
                isPrime = False
                loopPrime = False
            testPrime += 1
    
    # Jika bilangan prima ditemukan, jumlahkan bilangan tersebut dengan bilangan prima lainnya
    if isPrime:
        jumlahPrima += n
        
print(f"Jumlah bilangan prima adalah {jumlahPrima}.")

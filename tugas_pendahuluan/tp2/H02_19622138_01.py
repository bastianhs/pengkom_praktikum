# NIM/Nama  : 19622138/Bastian Hendramukti Suryapratama
# Tanggal   : 3 Oktober 2022
# Deskripsi : Program penentuan bilangan sempurna dari bilangan bulat

# PROGRAM BILANGAN_SEMPURNA

# KAMUS
# bilangan, jumlah Faktor, i: int

# ALGORITMA

# User memasukkan input berupa bilangan bulat
bilangan = int(input("Masukkan bilangan: "))

# Menentukan apakah suatu bilangan bulat termasuk bilangan sempurna
if bilangan <= 1:
    print("Bilangan tersebut bukan bilangan sempurna")
else:
    # Menghitung jumlah faktor
    jumlahFaktor = 0
    for i in range(1, bilangan):
        if (bilangan % i) == 0:
            jumlahFaktor += i
    if jumlahFaktor == bilangan:
        print("Bilangan tersebut adalah bilangan sempurna")
    else:
        print("Bilangan tersebut bukan bilangan sempurna")

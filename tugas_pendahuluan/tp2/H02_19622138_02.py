# NIM/Nama  : 19622138/Bastian Hendramukti Suryapratama
# Tanggal   : 3 Oktober 2022
# Deskripsi : Program menghitung nilai yang membesar

# PROGRAM NILAI_MEMBESAR

# KAMUS
# bilangan1, bilangan2, urutanAngka, tidakMembesarCounter, jumlahMembesar: int
# adaNilaiMembesar: bool

# ALGORITMA
# Menjumlahkan semua bilangan yang lebih besar dibandingkan bilangan yang dimasukkan tepat sebelumnya
# Input bilangan akan berhenti 
# jika bilangan yang dimasukkan tidak lebih besar dari bilangan sebelumnya selama 3 kali berturut-turut 

# Memasukkan bilangan pertama
bilangan1 = int(input("Angka ke-1: "))

urutanAngka = 2
tidakMembesarCounter = 1 # bilangan pertama selalu dianggap tidak membesar
adaNilaiMembesar = False # awalnya belum ada nilai yang membesar
jumlahMembesar = 0
while tidakMembesarCounter < 3:
    # Memasukkan bilangan berikutnya
    bilangan2 = int(input("Angka ke-" + str(urutanAngka) + ": "))
    if bilangan2 <= bilangan1:
        tidakMembesarCounter += 1
    else: # bilangan2 > bilangan1
        if not adaNilaiMembesar:
            adaNilaiMembesar = True # menyatakan sudah ada bilangan yang membesar
        jumlahMembesar += bilangan2
        tidakMembesarCounter = 0
    urutanAngka += 1
    bilangan1 = bilangan2

if adaNilaiMembesar:
    print("Jumlah nilai yang membesar adalah " + str(jumlahMembesar) + ".")
else:
    print("Tidak ada nilai yang membesar")

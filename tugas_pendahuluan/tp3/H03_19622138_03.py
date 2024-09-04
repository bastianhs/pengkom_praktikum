# NIM/Nama  : 19622138/Bastian Hendramukti Suryapratama
# Tanggal   : 18 Oktober 2022
# Deskripsi : Mencari frekuensi kemunculan suatu string dalam string lain

# FREKUENSI_KEMUNCULAN_STRING

# KAMUS
# len1, len2, count, indexStartStr2, index: int
# str1, str2: str
# allSame: bool

# ALGORITMA

# Memasukkan panjang string 1
len1 = int(input("Masukkan panjang string 1: "))
# Memasukkan string 1
str1 = input("Masukkan string 1: ")
# Memasukkan panjang string 2
len2 = int(input("Masukkan panjang string 2: "))
# Memasukkan string 2
str2 = input("Masukkan string 2: ")

# Kita akan mengecek frekuensi kemunculan string 1 dalam string 2
# Pengecekan dilakukan per karakter

# Dimulai dari indeks ke-0 string 1 dibandingkan dengan indeks ke-0 string 2,
# lalu indeks ke-1 string 1 dibandingkan dengan indeks ke-1 string 2,
# dan seterusnya sampai indeks ke-(len1 - 1) string 1 dibandingkan dengan indeks ke-(len1 - 1) string 2
# Jika semuanya sama, berarti frekuensi kemunculan bertambah 1

# Selanjutnya, titik mulai pengecekan string 2 digeser sebanyak 1 indeks ke kanan
# Dimulai dari indeks ke-0 string 1 dibandingkan dengan indeks ke-1 string 2,
# lalu indeks ke-1 string 1 dibandingkan dengan indeks ke-2 string 2,
# dan seterusnya sampai indeks ke-(len1 - 1) string 1 dibandingkan dengan indeks ke-(1 + len1 - 1) string 2
# Jika semuanya sama, berarti frekuensi kemunculan bertambah 1

# Pengecekan tersebut dilakukan berulang-ulang
# dengan menggeser titik mulai pengecekan string 2 sebanyak 1 indeks ke kanan
# Batas akhir titik mulai pengecekan string 2 adalah indeks ke-(len2 - len1)

# Inisialisasi frekuensi kemunculan string
# Awalnya frekuensi kemunculan string adalah 0 kali
count = 0
# Looping untuk mengecek frekuensi kemunculan suatu string sebagai substring dari string lain
for indexStartStr2 in range((len2 - len1) + 1):
    index = 0
    allSame = True
    while allSame and index < len1:
        if str1[index] != str2[indexStartStr2 + index]:
            allSame = False
        else:
            index += 1
    
    if allSame:
        count += 1

# Menampilkan banyak kemunculan string
print(f"String 1 muncul sebanyak {count} kali.")

# NIM/Nama  : 19622138/Bastian Hendramukti Suryapratama
# Tanggal   : 14 September 2022
# Deskripsi : Perhitungan waktu lari

# PROGRAM PERHITUNGAN WAKTU
# Menghitung selisih waktu mulai dan waktu selesai

# KAMUS
# i_hour, i_minute, i_second: int
# f_hour, f_minute, f_second: int
# difference_in_hour, difference_in_minute, difference_in_second: int
# total_difference_in_second: int
# d_hour, d_minute, d_second: int

# ALGORITMA

# User memasukkan waktu mulai dan waktu selesai
print("Masukkan waktu mulai!")
i_hour = int(input("Jam   : "))
i_minute = int(input("Menit : "))
i_second = int(input("Detik : "))
print("Masukkan waktu selesai!")
f_hour = int(input("Jam   : "))
f_minute = int(input("Menit : "))
f_second = int(input("Detik : "))

# Menghitung selisih waktu dalam detik
difference_in_hour = f_hour - i_hour
difference_in_minute = f_minute - i_minute
difference_in_second = f_second - i_second
total_difference_in_second = (difference_in_hour * 3600) + (difference_in_minute * 60) + difference_in_second

# Mengonversi selisih waktu dalam jam, menit, dan detik
# konversi ini menggunakan asumsi tidak ada pergantian hari
d_hour = total_difference_in_second // 3600
d_minute = (total_difference_in_second % 3600) // 60
d_second = (total_difference_in_second % 3600) % 60

# Mengeluarkan perhitungan selisih waktu
if d_hour == 0:
    if d_minute == 0:
        print("Tuan Riz berlari selama " + str(d_second) + " detik.")
    else: # selisih menit tidak 0
        if d_second == 0:
            print("Tuan Riz berlari selama " + str(d_minute) + " menit.")
        else: # selisih detik tidak 0
            print("Tuan Riz berlari selama " + str(d_minute) + " menit " + str(d_second) + " detik.")
else: # selisih jam tidak 0
    if d_minute == 0:
        if d_second == 0:
            print("Tuan Riz berlari selama " + str(d_hour) + " jam.")
        else: # selisih detik tidak 0
            print("Tuan Riz berlari selama " + str(d_hour) + " jam " + str(d_second) + " detik.")
    else: # selisih menit tidak 0
        if d_second == 0:
            print("Tuan Riz berlari selama " + str(d_hour) + " jam " + str(d_minute) + " menit.")
        else: # selisih detik tidak 0
            print("Tuan Riz berlari selama " + str(d_hour) + " jam " + str(d_minute) + " menit " + str(d_second) + " detik.")

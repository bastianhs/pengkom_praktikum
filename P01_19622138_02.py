# NIM/Nama :19622138/Bastian Hendramukti Suryapratama
# Tanggal :28 September 2022
# Deskripsi :Menentukan interval beririsan atau tidak beririsan

# PROGRAM PENENTUAN INTERVAL BERIRISAN

# ALGORITMA

# User memasukkan input
# asumsi input user a != b dan a, b bilangan bulat
a_1 = int(input("Masukkan nilai a interval 1: "))
b_1 = int(input("Masukkan nilai b interval 1: "))
a_2 = int(input("Masukkan nilai a interval 2: "))
b_2 = int(input("Masukkan nilai b interval 2: "))

# Memperbaiki input jika terbalik
if b_1 < a_1:
    a_1_correct = b_1
    b_1_correct = a_1
else:
    a_1_correct = a_1
    b_1_correct = b_1

if b_2 < a_2:
    a_2_correct = b_2
    b_2_correct = a_2
else:
    a_2_correct = a_2
    b_2_correct = b_2

# Penentuan interval beririsan/tidak
if a_1_correct < a_2_correct:
    if b_1_correct > a_2_correct:
        apakahBeririsan = True
    else:
        apakahBeririsan = False
else: # a_1_correct >= a_2_correct
    if b_2_correct > a_1_correct:
        apakahBeririsan = True
    else:
        apakahBeririsan = False

if apakahBeririsan:
    print("Kedua interval tersebut beririsan.")
else:
    print("Kedua interval tersebut tidak beririsan.")

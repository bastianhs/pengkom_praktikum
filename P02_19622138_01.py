# NIM/NAMA: 19622138/Bastian Hendramukti Suryapratama
# Tanggal: 12 Oktober 2022
# Deskripsi: Menghitung jumlah pantulan sebelum ketinggian 1 meter

# JUMLAH_PANTULAN

# KAMUS
# h, tipe, count: int

# ALGORITMA

# Memasukkan ketinggian awal dan tipe bola
# asumsinya ketinggian dan tipe adalah bilangan bulat
h = int(input("Masukkan ketinggian awal bola: "))
tipe = int(input("Masukkan tipe bola: "))

# Menghitung jumlah pantulan sebelum ketinggian 1 meter
count = 0
h /= tipe
while h > 1:
    count += 1
    h /= tipe
    
print(f"Bola akan memantul sebanyak {count} kali.")

# NIM/Nama  : 19622138/Bastian Hendramukti Suryapratama
# Tanggal   : 18 Oktober 2022
# Deskripsi : Mencari kondisi akhir rangkaian lampu

# KONDISI_RANGKAIAN_LAMPU

# KAMUS
# banyakLampu, frekuensi, i, tombol: int
# rangkaianLampu: list (array of int)

# ALGORITMA

# Memasukkan banyak lampu dari suatu rangkaian
banyakLampu = int(input("Masukkan banyak lampu: "))

# Inisialisasi array untuk menyimpan kondisi rangkaian lampu
rangkaianLampu = [0 for i in range(banyakLampu)]

# Memasukkan berapa kali tombol ditekan
frekuensi = int(input("Masukkan berapa kali Tuan Kil menekan tombol: "))

# Looping untuk memasukkan urutan tombol yang ditekan dan memproses efeknya
for i in range(frekuensi):
    # Memasukkan urutan tombol yang ditekan
    tombol = int(input(f"Tombol yang ditekan ke {i + 1}: "))
    # Mengubah kondisi lampu dari tombol yang ditekan
    if rangkaianLampu[tombol - 1] == 0:
        rangkaianLampu[tombol - 1] = 1
    else:
        rangkaianLampu[tombol - 1] = 0
    # Mengubah kondisi lampu di samping tombol yang ditekan
    if tombol == 1:
        # Jika tombol yang ditekan adalah tombol pertama,
        # hanya mengubah kondisi lampu di samping kanannya
        if rangkaianLampu[tombol] == 0:
            rangkaianLampu[tombol] = 1
        else:
            rangkaianLampu[tombol] = 0
    elif tombol == banyakLampu:
        # Jika tombol yang ditekan adalah tombol terakhir,
        # hanya mengubah kondisi lampu di samping kirinya
        if rangkaianLampu[tombol - 2] == 0:
            rangkaianLampu[tombol - 2] = 1
        else:
            rangkaianLampu[tombol - 2] = 0
    else:
        # Jika tombol yang ditekan bukan tombol pertama atau terakhir,
        # mengubah kondisi lampu di samping kanan dan kirinya
        if rangkaianLampu[tombol] == 0:
            rangkaianLampu[tombol] = 1
        else:
            rangkaianLampu[tombol] = 0
        if rangkaianLampu[tombol - 2] == 0:
            rangkaianLampu[tombol - 2] = 1
        else:
            rangkaianLampu[tombol - 2] = 0

# Menampilkan kondisi akhir rangkaian lampu
print("Keadaan akhir rangkaian lampu adalah", end=" ")
for i in range(banyakLampu):
    print(rangkaianLampu[i], end="")
print(".")

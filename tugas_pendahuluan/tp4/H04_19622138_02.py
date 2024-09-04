# NIM/Nama: 19622138/Bastian Hendramukti Suryapratama
# Tanggal: 31 Oktober 2022
# Deskripsi: Mengubah seluruh elemen array menjadi 0

# UBAH_ELEMEN_ARRAY

# KAMUS
# N, i, min: int
# kumpulan_nilai: array [0..N-1] of int


# Fungsi array_size
def array_size(array):
    # Mencari ukuran array

    # KAMUS LOKAL
    # array: array of int
    # size, a: int

    # ALGORITMA
    size = 0
    for a in array:
        size += 1

    return size


# Fungsi cek_0_semua
def cek_0_semua(array):
    # Mengecek apakah semua elemen array bernilai 0

    # KAMUS LOKAL
    # array: array of int
    # size, index: int
    # hasil_cek: bool

    # ALGORITMA
    size = array_size(array)
    hasil_cek = True
    index = 0
    while hasil_cek and (index < size):
        if array[index] != 0:
            # Jika salah satu elemen array bukan 0,
            # kita bisa memastikan hasil pengecekannya bernilai False
            hasil_cek = False
        else:
            index += 1

    return hasil_cek


# Fungsi min_array
def min_array(array):
    # Menentukan nilai minimum dari kumpulan elemen array yang bukan 0

    # KAMUS LOKAL
    # array: array of int
    # size, index, min, a: int

    # ALGORITMA

    size = array_size(array)

    # Mencari elemen pertama array yang bukan 0
    index = 0
    min = 0
    while (index < size) and (min == 0):
        if array[index] != 0:
            min = array[index]
        else:
            index += 1

    # Mencari nilai minimum sebenarnya
    for a in range((index + 1), size):
        if (array[a] != 0) and (array[a] < min):
            min = array[a]

    # Jika min != 0, berarti nilai minimumnya ditemukan
    # Jika min == 0, semua elemen array bernilai 0
    return min


# ALGORITMA

# Memasukkan banyak nilai
N = int(input("Masukkan banyak nilai: "))

# Inisialisasi array
kumpulan_nilai = [0 for i in range(N)]

# Memasukkan kumpulan nilai ke dalam array
for i in range(N):
    kumpulan_nilai[i] = int(input(f"Masukkan nilai ke-{i + 1}: "))

# Menampilkan isi array sebelum dilakukan pengurangan nilai
for i in range(N):
    if i < (N - 1):
        print(kumpulan_nilai[i], end=" ")
    else:
        print(kumpulan_nilai[i])

# Selama kumpulan nilai tersebut belum 0 semua,
# dilakukan pengurangan nilai pada semua elemen selain 0
# Pengurangan nilai menggunakan nilai minimum elemen yang bukan 0
while not cek_0_semua(kumpulan_nilai):

    # Mencari nilai minimum elemen yang bukan 0
    min = min_array(kumpulan_nilai)

    # Dilakukan pengurangan nilai
    for i in range(N):
        if kumpulan_nilai[i] != 0:
            kumpulan_nilai[i] -= min

    # Menampilkan isi array setelah dilakukan pengurangan nilai
    for i in range(N):
        if i < (N - 1):
            print(kumpulan_nilai[i], end=" ")
        else:
            print(kumpulan_nilai[i])

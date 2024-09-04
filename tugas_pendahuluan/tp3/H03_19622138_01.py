# NIM/Nama  : 19622138/Bastian Hendramukti Suryapratama
# Tanggal   : 18 Oktober 2022
# Deskripsi : Mencari barang dengan besar diskon (dalam rupiah) paling besar

# CARI_DISKON_RUPIAH_TERBESAR

# KAMUS
# N, i, harga awal, diskon, diskonRupiah: int
# listHargaAwal, listDiskonRupiah, diskonTerbesar: list (array of int)

# ALGORITMA

# Memasukkan banyak barang yang ingin dicari diskonnya
N = int(input("Masukkan banyak barang: "))

# Inisialisasi array untuk menyimpan harga awal barang
listHargaAwal = [0 for i in range(N)]
# Memasukkan harga awal barang
for i in range(N):
    hargaAwal = int(input(f"Masukkan harga awal barang ke-{i + 1}: "))
    # Setelah harga awal dimasukkan oleh user, harga awal dimasukkan ke dalam array
    listHargaAwal[i] = hargaAwal

# Inisialisasi array untuk menyimpan diskon barang dalam rupiah
listDiskonRupiah = [0 for i in range(N)]
# Memasukkan diskon barang
for i in range(N):
    # Awalnya memasukkan diskon barang dalam persen
    diskon = int(input(f"Masukkan besar diskon (dalam persen) barang ke-{i + 1}: "))
    # Lalu dihitung diskon dalam rupiah
    # Jika hasilnya bukan bilangan bulat, akan dilakukan pembulatan dengan round
    diskonRupiah = round(listHargaAwal[i] * (diskon / 100))
    # Setelah dihitung, hasil perhitungan dimasukkan ke dalam array
    listDiskonRupiah[i] = diskonRupiah

# Setelah semua harga awal dan diskon barang dimasukkan,
# kita cari barang dengan diskon (dalam rupiah) yang terbesar

# Inisialisasi array untuk menyimpan indeks barang dan besar diskon dalam rupiah
# Awalnya, kita anggap barang dengan indeks 1 memiliki diskon terbesar
diskonTerbesar = [1, listDiskonRupiah[0]]
# Membandingkan semua diskon barang yang telah dimasukkan
for i in range(1, N):
    if listDiskonRupiah[i] > diskonTerbesar[1]:
        # Jika ditemukan diskon yang lebih besar,
        # indeks dan besar diskon barang tersebut akan dimasukkan ke dalam array
        diskonTerbesar[0] = i + 1
        diskonTerbesar[1] = listDiskonRupiah[i]

# Menampilkan indeks dan besar diskon (dalam rupiah) yang terbesar
print(f"Barang {diskonTerbesar[0]} memiliki diskon paling besar yaitu {diskonTerbesar[1]}.")

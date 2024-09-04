# NIM/Nama : 19622138/Bastian Hendramukti Suryapratama
# Tanggal : 26 Oktober 2022
# Deskripsi : Menuliskan kembali pesan Tuan Kil dengan mengganti karakter pengganti spasi dengan spasi

# KAMUS
# len, i: int
# pesan, char: str

# ALGORITMA

# Memasukkan panjang pesan, pesan Tuan Kil, dan karakter pengganti spasi
len = int(input("Masukkan panjang pesan: "))
pesan = input("Masukkan pesan Tuan Kil: ")
char = input("Masukkan karakter penggganti spasi: ")

print("Pesan Tuan Kil: ", end="")
# Menuliskan pesan Tuan Kil yang sebenarnya
for i in range(len):
    if pesan[i] == char:
        # Jika suatu karakter dalam pesan sama dengan karakter pengganti spasi,
        # ganti karakter tersebut dengan spasi
        print(" ", end="")
    else:
        print(pesan[i], end="")

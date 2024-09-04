# NIM/Nama :19622138/Bastian Hendramukti Suryapratama
# Tanggal :28 September 2022
# Deskripsi :Menentukan tingkat kesulitan level dan tercapainya target 2 level mudah dan 1 level sulit

# PROGRAM TINGKAT KESULITAN LEVEL DAN TERCAPAINYA TARGET

# ALGORITMA

# User memasukkan input
# asumsi input user adalah bilangan bulat positif
player_level1 = int(input("Banyak pemain yang memainkan level 1: "))
success_level1 = int(input("Banyak pemain yang berhasil menyelesaikan level 1: "))

player_level2 = int(input("Banyak pemain yang memainkan level 2: "))
success_level2 = int(input("Banyak pemain yang berhasil menyelesaikan level 2: "))

player_level3 = int(input("Banyak pemain yang memainkan level 3: "))
success_level3 = int(input("Banyak pemain yang berhasil menyelesaikan level 3: "))

player_level4 = int(input("Banyak pemain yang memainkan level 4: "))
success_level4 = int(input("Banyak pemain yang berhasil menyelesaikan level 4: "))

player_level5 = int(input("Banyak pemain yang memainkan level 5: "))
success_level5 = int(input("Banyak pemain yang berhasil menyelesaikan level 5: "))

# Persentase kesuksesan
success_rate_level1 = (success_level1 / player_level1) * 100
success_rate_level2 = (success_level2 / player_level2) * 100
success_rate_level3 = (success_level3 / player_level3) * 100
success_rate_level4 = (success_level4 / player_level4) * 100
success_rate_level5 = (success_level5 / player_level5) * 100

# Menentukan banyak level mudah, sedang, dan sulit
level_mudah = 0
level_sedang = 0
level_sulit = 0

if success_rate_level1 >= 80:
    level_mudah += 1
elif 30 <= success_rate_level1 < 80:
    level_sedang += 1
else:
    level_sulit += 1

if success_rate_level2 >= 80:
    level_mudah += 1
elif 30 <= success_rate_level2 < 80:
    level_sedang += 1
else:
    level_sulit += 1

if success_rate_level3 >= 80:
    level_mudah += 1
elif 30 <= success_rate_level3 < 80:
    level_sedang += 1
else:
    level_sulit += 1

if success_rate_level4 >= 80:
    level_mudah += 1
elif 30 <= success_rate_level4 < 80:
    level_sedang += 1
else:
    level_sulit += 1

if success_rate_level5 >= 80:
    level_mudah += 1
elif 30 <= success_rate_level5 < 80:
    level_sedang += 1
else:
    level_sulit += 1

print("Banyak level mudah sebanyak " + str(level_mudah) + ", level sedang sebanyak " + str(level_sedang) + ", dan level sulit sebanyak " + str(level_sulit) + ".")

# Penentuan tercapainya target
if (level_mudah >= 2) and (level_sulit >= 1):
    print("Target berhasil dicapai.")
else:
    print("Target gagal dicapai.")

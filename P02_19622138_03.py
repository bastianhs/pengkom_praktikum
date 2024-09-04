# NIM/NAMA: 19622138/Bastian Hendramukti Suryapratama
# Tanggal: 12 Oktober 2022
# Deskripsi: Mencari FPB dari bilangan sebanyak lebih dari 2

# CARI_FPB

# KAMUS

# ALGORITMA

# Memasukkan banyak bilangan
B = int(input("Masukkan banyaknya bilangan: "))

bilangan = int(input(f"Masukkan bilangan ke-1: "))
bilangan1 = bilangan
FPB = 1
for i in range(2, B + 1):
    bilangan2 = int(input(f"Masukkan bilangan ke-{i}: "))
    
    loopFPB = True
    testFaktor = bilangan
    while loopFPB and (testFaktor > 0):
        print(f"testFaktor: {testFaktor}")
        if (bilangan % testFaktor) == 0:
            FPBTemp = testFaktor
            print(f"FPBTemp: {FPBTemp}")
            if (bilangan2 % FPBTemp) == 0:
                FPB = FPBTemp
                loopFPB = False
                print(f"FPB: {FPB}")
                FPBFound = True
            else:
                FPBFound = False
        
        if FPBFound:
            testFaktor = FPB
        else:
            testFaktor =- 1
        
    bilangan1 = bilangan2    

print(f"FPB nya adalah {FPB}.")

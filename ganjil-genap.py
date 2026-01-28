#----Program Menentukan bilangan ganjil atau genap---
#--- programmer : Yobel --------
#-------------------------------
bil = int(input('Masukan Nilai yang diuji: '))

if bil == 0:
    print(" Genap ")
    #break  # keluar dari looping
else:
    if bil == 1:
        print(" Ganjil ")
        # break  # keluar dari looping
		
while(True):

    bil = bil - 2
    if bil == 0:
        print(" Genap ")
        break  # keluar dari looping
    else:
        if bil == 1:
            print(" Ganjil ")
            break  # keluar dari looping

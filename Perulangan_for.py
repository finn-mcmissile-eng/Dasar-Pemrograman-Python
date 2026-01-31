#---------- Latihan 1 Pertemuan 5 ----------
#------- Programmer : Yobel Christian -------

ulang = int(input("Masukkan Jumlah Data: "))
for i in range(ulang):
    print("Data ke-" + str(i+1))
    nim = input("Masukkan NIM anda : ")
    uts = int(input("Masukkan nilai UTS anda : "))
    uas = int(input("Masukkan nilai UAS anda : "))
    print("NIM anda adalah %s nilai UTS anda %i nilai UAS anda %i" % (nim,uts,uas))
    print("-----------------------------------------------------------------\n")


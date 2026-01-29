kode_baju = input("Masukkan Kode Baju [AD/NVD] : ")
ukuran_baju = input("Masukkan Ukuran baju [XL/L/M/S] : ")

if kode_baju == "AD" or kode_baju == "ad" :
    merk = "ADIDAS"
    if ukuran_baju == "XL" or ukuran_baju == "xl":
        harga = 150000
    elif ukuran_baju == "L" or ukuran_baju == "l":
        harga = 130000
    elif ukuran_baju == "M" or ukuran_baju == "m":
        harga = 100000
    elif ukuran_baju == "S" or ukuran_baju == "s":
        harga = 60000
    else:
        harga = "Anda salah input ukuran"
elif kode_baju == "NVD" or kode_baju == "nvd":
    merk = "NEVADA"
    if ukuran_baju == "XL" or ukuran_baju == "xl":
        harga = 100000
    elif ukuran_baju == "L" or ukuran_baju == "l":
        harga = 90000
    elif ukuran_baju == "M" or ukuran_baju == "m":
        harga = 70000
    elif ukuran_baju == "S" or ukuran_baju == "s":
        harga = 400000
    else:
        harga = "Anda salah input ukuran"
else :
    merk = "Anda salah input kode merk"
    harga = 0

print("----------------------------")
print("Merk Baju : " +str(merk))
print("Ukuran    : " +str(ukuran_baju))
print("Harga     :",harga)
print("----------------------------")

pembeli = input("Masukkan Nama Pembeli             : ")
no_hp = input("Masukkan Nomor HP                 : ")
jurusan = input("Masukkan Kode Jurusan [SBY/BL/LMP]: ").upper()
if jurusan == "SBY" :
    nama_kota = "SURABAYA"
    harga = 300000
elif jurusan == "BL":
    nama_kota = "BALI"
    harga = 350000
else:
    nama_kota = "LAMPUNG"
    harga = 500000

jumlah_beli = int(input("Masukkan Jumlah Beli              : "))

if jumlah_beli >= 3:
    potongan = (jumlah_beli*harga)*0.1
else :
    potongan = 0

total = (jumlah_beli*harga) - potongan

print('----------------------------------------')
print("        PENJUALAN TIKET BUS XYZ")
print('----------------------------------------')
print("Nama Pembeli : " +str(pembeli))
print("No. Hanphone : " +str(no_hp))
print("Kode Jurusan yang Dipilih : " +str(jurusan))
print("Harga :", +(harga))
print("Jumlah Beli :", +(jumlah_beli))
print('----------------------------------------')
print("potongan yang didapat :",+(potongan))
print("Total Bayar :",+(total))
ubay=int(input("Masukkan Uang Bayar : "))
uangkembali=ubay-total
print("Uang Kembali :",+uangkembali)


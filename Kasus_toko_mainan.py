#---------- Yobel Christian Halawa ----------
#----------------- 15.1A.05 -----------------
#----------- Latihan 2 Pertemuan 3 ----------

print("TOKO MAINAN ANAK")
print("****************************")

nama_pembeli = input("masukkan nama pembeli : ")
kode_mainan = input("masukkan kode mainan : ")
harga_mainan = int(input("masukkan harga mainan : "))
jumlah_beli = int(input("masukkan jumlah beli : "))

total = harga_mainan*jumlah_beli

print("================================================")
print("Nama Pembeli = " +str(nama_pembeli))
print("Kode Mainan  = " +str(kode_mainan))
print("Harga        = " +str(harga_mainan))
print("Jumlah Beli  = " +str(jumlah_beli))
print("TOTAL        =",  total)
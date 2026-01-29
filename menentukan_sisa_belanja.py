hrg = float(input("input harga telur/kg : "))
brt = float(input("input berat telur : "))
total_bayar = hrg * brt

tarif_angkot = 3500
ongkos = 2 * tarif_angkot
uang_ibu = int(input("Masukkan jumlah uang yang dibawa ibu: "))
total_pengeluaran = ongkos + total_bayar
sisa_uang = uang_ibu - total_pengeluaran

print("Sisa uang ibu adalah ", sisa_uang)

# Program Kalkulator Sederhana
# ----------------------------
def tambah(x, y):
    return x + y
def kurang(x, y):
    return x - y
def kali(x, y):
    return x * y
def bagi(x, y):
    return x / y
def modulus(a,b):
    return a%b
def pangkat(a,b):
    return a**b


def jalankan_kalkulator():
    print("Pilih operasi: ")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Modulus")
    print("6. Pangkat")

    while True:
            pilihan = input("Masukkan pilihan (1/2/3/4/5/6) atau 'X' untuk keluar: ")
            if pilihan.lower == 'x':
                print("Terima kasih, silakan kembali lagi!")
                break
            if pilihan in ("1", "2", "3", "4", "5", "6"):
                try:
                    angka1 = float(input("Masukkan angka pertama: "))
                    angka2 = float(input("Masukkan angka kedua: "))
                except ValueError:
                    print("Kesalahan, Coba Lagi!")
                    continue

            if pilihan == '1':
                print(f"Hasil: {tambah(angka1, angka2)}")
            elif pilihan == '2':
                print(f"Hasil: {kurang(angka1, angka2)}")
            elif pilihan == '3':
                print(f"Hasil: {kali(angka1, angka2)}")
            elif pilihan == '4':
                print(f"Hasil: {bagi(angka1, angka2)}")
            elif pilihan == '5':
                print(f"Hasil: {modulus(angka1, angka2)}")
            elif pilihan == '6':
                print(f"Hasil: {pangkat(angka1, angka2)}")
            else:
                print("Pilihan tidak valid!")

if __name__ == "__main__":
    jalankan_kalkulator()

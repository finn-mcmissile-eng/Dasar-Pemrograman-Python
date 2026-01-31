def gambar_segitiga_siku_siku():
    """
    Meminta input bilangan bulat N dan mencetak segitiga siku-siku
    dengan tinggi N menggunakan karakter '*'.
    """
    while True:
        try:
            # Meminta input dari pengguna
            N = int(input("Masukkan bilangan bulat (1 sampai 100) sebagai tinggi segitiga: "))

            # Memeriksa validitas input sesuai batasan
            if 1 <= N <= 100:
                print("\n--- Output Segitiga Siku-siku ---\n")
                break  # Keluar dari loop jika input valid
            else:
                print("Input di luar rentang. Harap masukkan bilangan antara 1 dan 100.")
        except ValueError:
            print("Input tidak valid. Harap masukkan bilangan bulat.")

    # Loop luar (outer loop) untuk mengontrol baris (tinggi segitiga)
    for i in range(1, N + 1):
        # Loop dalam (inner loop) untuk mengontrol kolom (jumlah '*' per baris)
        # Jumlah '*' pada baris ke-i adalah i
        for j in range(i):
            print("*", end="")  # Mencetak '*' tanpa baris baru
        
        # Mencetak baris baru setelah selesai satu baris segitiga
        print()

# Menjalankan fungsi utama
gambar_segitiga_siku_siku()
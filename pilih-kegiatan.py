## Program Pilihan Aktivitas/Kegiatan
def tampilkan_pilihan(pilihan_dict):
    """Menampilkan pilihan dari dictionary dan mengembalikan key yang valid."""
    keys = list(pilihan_dict.keys())
    for key in keys:
        print(f"[{key}] {pilihan_dict[key]['nama']}")
    
    while True:
        pilihan = input("Pilih: ").upper()
        if pilihan in keys:
            return pilihan
        print("Pilihan tidak valid. Silakan coba lagi.")

def mulai_perjalanan():
    """Logika utama untuk aktivitas Perjalanan."""
    
    # 1. Definisikan Pilihan Lokasi
    lokasi_dict = {
        'A': {'nama': 'GBK', 'transportasi': {}},
        'B': {'nama': 'Kampus', 'transportasi': {}}
        # Tambahkan lokasi lain di sini jika diperlukan
    }

    # 2. Definisikan Opsi Transportasi dan Rute
    # Rute disimpan dalam dictionary bersarang (nested dictionary)
    # Kunci luarnya adalah kode Lokasi (A/B), kunci berikutnya adalah kode Transportasi (1/2/3), 
    # dan kunci terdalam adalah kode Cara Berangkat (1/2/3)
    rute_dict = {
        'A': { # Untuk tujuan GBK
            '1': { # Transportasi Umum (Transum)
                'nama': 'Transportasi Umum (Transum)',
                'rute': {
                    '1': 'Ojol + Commuter Line + Ojol/MRT',
                    '2': 'Sepeda Motor/Mobil + Commuter Line + MRT',
                    '3': 'Angkot + Commuter Line + MRT'
                },
                'detail_rute': {
                    '1': 'Rumah [Ojol] -> Stasiun Bekasi -> Stasiun Manggarai -> Stasiun Palmerah [Ojol/MRT] -> GBK',
                    '2': 'Rumah [Kendaraan Pribadi] -> Stasiun Bekasi -> Stasiun Manggarai -> Stasiun Sudirman [Jalan kaki] -> Stasiun MRT Dukuh Atas -> Stasiun Istora Senayan',
                    '3': 'Rumah [Angkot] -> Stasiun Bekasi -> Stasiun Manggarai -> Stasiun Sudirman [Jalan kaki] -> Stasiun MRT Dukuh Atas -> Stasiun Istora Senayan'
                }
            },
            '2': { # Kendaraan Pribadi
                'nama': 'Kendaraan Pribadi',
                'rute': {
                    '1': 'Gunakan Sepeda motor atau mobil langsung dari rumah ke lokasi!',
                    '2': 'Sepeda Motor/Mobil + Commuter Line + Ojol',
                    '3': 'Sepeda motor/mobil + Commuter Line + MRT'
                },
                'detail_rute': {
                    '1': 'Jalur Langsung (Misalnya, via tol)',
                    '2': 'Rumah [Kendaraan pribadi] -> Stasiun Bekasi -> Stasiun Manggarai -> Stasiun Sudirman [Jalan kaki] -> Stasiun Istora Senayan',
                    '3': 'Rumah [Kendaraan pribadi] -> Stasiun Bekasi -> Stasiun Manggarai -> Stasiun Palmerah [Pesan ojol buat ke GBK]'
                }
            }
        },
        'B': { # Untuk tujuan Kampus
            '1': { # Transportasi Umum (Transum)
                'nama': 'Transportasi Umum (Transum)',
                'rute': {
                    '1': 'Menggunakan Ojol',
                    '2': 'Menggunakan Bus Transum' # Anggap ini rute detail
                },
                'detail_rute': {
                    '1': 'Rumah [Ojol/Angkot] -> Kampus',
                    '2': 'Rumah [Bus Transum] -> Kampus'
                }
            },
            '2': { # Kendaraan Pribadi
                'nama': 'Kendaraan Pribadi',
                'rute': {
                    '1': 'Menggunakan Sepeda Motor/Mobil',
                },
                'detail_rute': {
                    '1': 'Rumah [Sepeda motor/mobil] -> Kampus'
                }
            }
        }
    }

    # --- Mulai Proses Pemilihan ---

    print("--- Memilih Lokasi Tujuan ---")
    for key, val in lokasi_dict.items():
        print(f"[{key}] {val['nama']}")
    
    lokasi_pilihan = input("Anda mau kemana? (A/B): ").upper()
    
    if lokasi_pilihan not in lokasi_dict:
        print("Lokasi tujuan belum tersedia.")
        return # Keluar dari fungsi

    print(f"\n--- Memilih Jenis Transportasi ke {lokasi_dict[lokasi_pilihan]['nama']} ---")
    
    # Ambil transportasinya dari rute_dict
    transportasi_opts = rute_dict[lokasi_pilihan]
    for key, val in transportasi_opts.items():
        print(f"[{key}] {val['nama']}")
    
    transportasi_pilihan = input("Anda ingin gunakan apa? (1/2): ")

    if transportasi_pilihan not in transportasi_opts:
        print("Pilihan transportasi belum tersedia.")
        return

    print(f"\n--- Memilih Cara Berangkat ---")
    
    cara_opts = transportasi_opts[transportasi_pilihan]['rute']
    for key, val in cara_opts.items():
        print(f"[{key}] {val}")
    
    cara_pilihan = input("Cara mana yang anda pilih?: ")

    if cara_pilihan not in cara_opts:
        print("Cara yang dipilih belum tersedia.")
        return

    # --- Tampilkan Rute Akhir ---
    print("\n=============================================")
    print(f"✅ Rute Perjalanan ke {lokasi_dict[lokasi_pilihan]['nama']}:")
    
    # Ambil detail rute
    detail_rute = transportasi_opts[transportasi_pilihan]['detail_rute'].get(cara_pilihan, "Detail rute tidak ditemukan.")
    print(f"-> {detail_rute}")
    print("=============================================")


# --- Logika Program Utama ---
def main():
    while True:
        # Pilihan Aktivitas
        print("\n# Program pilih aktivitas/kegiatan")
        print("-----------------------------------")
        print("[1] Perjalanan")
        print("[2] Perhitungan")
        pilihan = input("Anda mau melakukan apa hari ini? [1/2 atau 'x' untuk keluar]: ").lower()
        print("-----------------------------------")

        if pilihan == 'x':
            print("Terima kasih, silakan kembali lagi!")
            break
        
        elif pilihan == '1':
            try:
                mulai_perjalanan()
            except Exception as e:
                # Catch error yang lebih umum jika ada masalah tak terduga
                print(f"Terjadi kesalahan saat menjalankan Perjalanan: {e}")
        
        elif pilihan == '2':
            print("Maaf, pilihan perhitungan belum tersedia!")
        
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()

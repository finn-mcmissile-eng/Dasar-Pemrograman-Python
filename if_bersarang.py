# Struktur Percabangan Nested If
# Merk Baju Polo/Alisan/StYess
# Program menentukan Harga baju berdasarkan merk dan ukuran 
# ------------------------------------------------------------

Merk = input('Merk Baju P/A/S: ')

if Merk =='P':
    print('Merk Polo')
    ukuran = input('Ukuran L/M/S: ')
    if ukuran == 'L':
        print('Harga = 300000')
    elif ukuran == 'M':
        print('Harga = 225000')
    else:
        print('Harga = 175000')
elif Merk=='A':
     print('Merk Alisan')
     ukuran = input('Ukuran L/M/S: ')
     if ukuran == 'L':
        print('Harga 275000')
     elif ukuran == 'M':
            print('Harga = 200000')
     else:
            print('Harga = 150000')
else:
     print('Merk StYess')
     ukuran = input('Ukuran L/M/S: ')
     if ukuran == 'L':
        print('Harga 250000')
     elif ukuran == 'M':
            print('Harga = 175000')
     else:
            print('Harga = 125000')

# Meminta input nilai dari pengguna
print('-------------------------------------')
abs = int(input('Masukkan Absen: '))
tgs = int(input('Masukkan Nilai Tugas: '))
uts = int(input('Masukkan Nilai UTS: '))
uas = int(input('Masukkan Nilai UAS: '))

# Menghitung nilai akhir dengan bobot
akhir = (0.2 * abs) + (0.25 * tgs) + (0.25 * uts) + (0.3 * uas)

# Menentukan grade berdasarkan nilai akhir
if akhir > 85:
    grade = "A"
elif akhir > 65:
    grade = "B"
elif akhir > 50:
    grade = "C"
elif akhir > 30:
    grade = "D"
else:
    grade = "E"

# Mencetak hasil
print('-------------------------------------')
print("Nilai Akhir:", akhir)
print("Gradenya   :", grade)
print('-------------------------------------')
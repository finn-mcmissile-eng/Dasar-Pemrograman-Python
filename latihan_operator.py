#---------- Yobel Christian Halawa ----------
#----------------- 15.1A.05 -----------------
#----------- Latihan 1 Pertemuan 3 ----------

#========================================================================================================================================
#OPERATOR MATEMATIKA
a = int(input("Masukkan Nilai a : "))
b = int(input("Masukkan Nilai b : "))

print("===========================================================")
print("Hasil Operasi Matematika dari Kedua Nilai Tersebut Adalah :")
print("===========================================================")
penjumlahan = a + b
print(a, "+", b, "=", penjumlahan)

pengurangan = a - b
print(a, "-", b, "=", pengurangan)

perkalian = a * b
print(a, "*", b, "=", perkalian)

pembagian = a / b
print(a, "/", b, "=", pembagian)

pemangkatan = a ** b
print(a, "**", b, "=", pemangkatan)

pembagian_bulat = a // b
print(a, "//", b, "=", pembagian_bulat)


#========================================================================================================================================
#OPERATOR PENUGASAN
print("Operator Penugasan")
a = float(input("Masukkan Angka : "))

print("==============================")
print("Nilai a :", a)
a **= 2 
print("Nilai a setelah a **= 2: ", a)
print("==============================")


#========================================================================================================================================
#OPERATOR LOGIKA
print("OPERATOR LOGIKA")
print("================")
a = True
b = False
c = a
a = b
b = c

print("a :", a)
print("b :", b)
print("================")
print("a and b :", b and a)
print("a or b :", b or a)
print("not a :", not a)
print("not b :", not b)
print("================")


#========================================================================================================================================
#OPERATOR BITWISE
print("======================================================")
print("OPERATOR BITWISE")
try:
    x = int(input("Masukkan Angka : "))
    y = int(input("Masukkan Angka : "))

    print("x & y (bitwise AND):", x & y)
    print("x | y (bitwise OR):", x | y)
    print("x << 1 (bitwise Left Shift):", x << 1)
    print("======================================================")

except ValueError:
    print("Masukkan Bilangan Bulat!")


#========================================================================================================================================
#OPERATOR IDENTITAS
print("===================================================")
print("OPERATOR IDENTITAS")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1
list4 = list1
list4 = list2

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is list4:", list1 is list4)
print("list2 is list3:", list2 is list3)
print("list2 is list4:", list2 is list4)
print("list3 is list4:", list3 is list4)
print("===================================================")


#========================================================================================================================================
#OPERATOR KEANGGOTAAN
print("======================================")
print("OPERATOR KEANGGOTAAN")
buah = "Naga", "Pisang", "Melon", "Nanas", "Apel", "Salak", "Jambu", "Jeruk"
BUAH = input("Masukkkan Nama Buah : ").upper()

print(BUAH, "in buah:", BUAH in buah)
print("======================================")
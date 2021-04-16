#PROGRAM FUNGSI NUMERIK
#menghitung volume kerucut bersyarat

phi= 3.14

#input tinggi kerucut
t1= float(input("Masukkan tinggi ke-1: "))
t2= float(input("Masukkan tinggi ke-2: "))
t3= float(input("Masukkan tinggi ke-3: "))

#input jari-jari kerucut
r1= float(input("\nMasukkan jari-jari ke-1: "))
r2= float(input("Masukkan jari-jari ke-2: "))
r3= float(input("Masukkan jari-jari ke-3: "))

#menggunakan tinggi max yang telah dibulatkan ke atas
import math
t=max(t1,t2,t3)
tinggi=math.ceil(t)
print("\nTinggi yang digunakan:",tinggi)

#menggunakan jari-jari min yang telah dibulatkan ke bawah
import math
Jari2= min(r1,r2,r3)
r= math.floor(Jari2)
print("\nJari-jari yang digunakan:",r)

#menghitung volume
volume=1/3 * phi * r**2 * tinggi
Vol=round(volume,2)

#output
print('\nMenghitung Volume kerucut')
print("Volume kerucut adalah:",Vol)
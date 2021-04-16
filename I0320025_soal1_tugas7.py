# PROGRAM FUNGSI STRING
# membuat suatu judul buku min 11 karakter

Judul= input("Masukkan judul: ")
#Menghitung panjang karakter
karakter= len(Judul)
print("panjang karakter: ",karakter)

#input judul baru jika karakter judul <= 11 karakter
while karakter <= 11:
    Judul= (input("Masukkan judul baru: "))
    karakter= len(Judul)
if karakter >= 11:
        print(Judul.center(70,"="))

#membuat huruf pertama judul kapital
kapital= Judul.capitalize()
print('\nJudul buku ini adalah: ',kapital)

#membuat uppercase pada judul
print(Judul.upper())
print('panjang karakter judul:',len(Judul))

#menghitung jumlah karakter/huruf a pada judul buku
a=Judul.count("a")
print("Banyak huruf a pada judul:",a)








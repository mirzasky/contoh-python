"""
Program ini untuk membuat username dan password berdasarkan data pribadi mahasiswa.
Program ini bertujuan untuk menggunakan sebagian perintah dasar Python3.

Ditulis oleh Riza Mirza, S.Kom,
untuk bahan belajar mata kuliah dasar pemrograman komputer dan internet of things.

Kode ini juga dipublikasi di situs https://mirzasky.com dan Github.

Lhokseumawe, 1 Desember 2021.
"""

#mencetak perintah input dan menerima input dari konsol
namaDepan = input("Nama Depan :")
namaBelakang = input("Nama Belakang :")
nim = input("NIM:")
tgl = input("Tanggal Lahir:")
bln = input("Bulan Lahir:")
thn = input("Tahun Lahir:")

#membuat username berdasarkan huruf pertama nama depan dan nama belakang, serta angka kedua dan ketiga dari NIM

a=namaDepan[0]
b=namaBelakang[0]
c="user_"
d=nim[1:3]
user=c+a+b+d

#membuat password berdasarkan perbandingan angka pertama nim terhadap nama-nama buah
#list nama-nama buah
listBuah=['mangga','jeruk','anggur','nanas','apel','pisang','melon','semangka','salak']
#ambil angka pertama dari inputan nim
e=nim[0]
#konversi tipe data string dari varibel e menjadi integer agar dapat menjadi indeks list
f=int(e)
#mengambil kata buah dari list
buahSandi=listBuah[f]
#membuat sandi dengan kombinasi nama buah dan tanggal bulan tahun lahir
sandi=buahSandi+"_"+tgl+bln+thn
print("Username : ",user)
print("Password : ",sandi)





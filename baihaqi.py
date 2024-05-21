import priaaz as mod

print("selamat datang di program menejemen stok barang")
print("1.tambah data barang")
print("2. edit")
print("3.hapus data barang")
print("4.cari data")
print("5.tampilkan data barang")
print("6.tampilkan jumlah data")
print("7.keluar")

while True :
    pilihan = int(input("masukan pilihan : "))
    if pilihan == 1 :
        mod.tambah()
    elif pilihan == 2 :
        mod.edit()
    elif pilihan == 3 :
        mod.hapus()
    elif pilihan == 4 :
        mod.cari()
    elif pilihan == 5 :
        mod.tampilan()
    elif pilihan == 6 :
        mod.jumlah()
    elif pilihan == 7 :
        print("Thank you")
        break
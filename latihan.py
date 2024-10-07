kodebaju = input("masukan kode baju [sp/ad] : ")
ukuran = input("masukan ukuran baju [s/m] : ")

if kodebaju == "sp" or kodebaju == "sp" :
    merk = "superdry"
    if ukuran=="s" or ukuran=="s" :
        harga = 450000
    elif ukuran=="m" or ukuran=="m":
        harga = 500000
    else:
        harga = 0
elif kodebaju == "ad" or kodebaju == "ad" :
    merk = "adidas"
    if ukuran=="s" or ukuran=="s":
        harga = 650000
    elif ukuran=="m" or ukuran=="m":
        harga = 700000
    else:
        harga = 0

else:
    merk = "anda salah input kode merk"
    harga = 0

print("--------------------------------")
print("merk baju : "+str(merk))
print("harga baju : rp.",harga)
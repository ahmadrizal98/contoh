terjual=int(input("banyak produk terjual : "))
hargaproduk=int(input("harga satuan produk : "))
gaji=5000000

if terjual>=100:
    bonus=int(terjual*hargaproduk/100)*20
else:
    bonus=int(terjual*hargaproduk/100)*10

print("total gaji seluruhan= ",gaji+bonus)
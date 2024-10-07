penyewaan=int(input("sewa berapa jam : "))
waktu=0
if penyewaan<=3:
    waktu=penyewaan*6000
else:
    waktu=3*6000+(penyewaan-3)*5000
print("biaya penyewaan : ",waktu)
gajipokok=300000
namakaryawan=input("nama karyawan: ")
golongan=int(input("golongan: "))
pendidikan=input("pendidikan: ")
jumlahjamlembur=int(input("jumlah jam lembur: "))

if golongan==1:
    tunjanganjabatan=int(gajipokok/100)*5
elif golongan==2:
    tunjanganjabatan=int(gajipokok/100)*10
elif golongan==3:
    tunjanganjabatan=int(gajipokok/100)*15
else:
    tunjanganjabatan=0

if pendidikan=="sma":
    tunjanganpendidikan=int(gajipokok/100)*2.5
elif pendidikan=="d1":
    tunjanganpendidikan=int(gajipokok/100)*5
elif pendidikan=="d3":
    tunjanganpendidikan=int(gajipokok/100)*20
elif pendidikan=="s1":
    tunjanganpendidikan=int(gajipokok/100)*30
else:
    tunjanganpendidikan=0

honorlembur=0

if jumlahjamlembur>8:
    kelebihanjamlembur = jumlahjamlembur-8
    honorlembur=kelebihanjamlembur*3500

totalgaji=gajipokok+tunjanganjabatan+tunjanganjabatan+honorlembur

print("PROGRAM HITUNG GAJI KAYAWAN")
print("nama karyawan: ",namakaryawan)
print("golongan: ",golongan)
print("pendidikan: ",pendidikan)
print("jumlah jam lembur: ",jumlahjamlembur)
print("-----------------------------------------")
print("tunjangan jabatan: rp.",tunjanganjabatan)
print("tunjangan pendidikan: rp.", tunjanganpendidikan)
print("honor lembur: rp." ,honorlembur)
print("total gaji karyawan:" ,totalgaji)
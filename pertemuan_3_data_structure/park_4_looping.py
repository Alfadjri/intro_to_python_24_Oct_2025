#for
print("=======for range======")
for index in range(1,5+1):
    print(f"{index}.Tidak akan mengulan kesalahan kembali")
    
    

data_kariawan = [
    {
        "nama_lengkap" : "Udin",
        "divisi" : "Programmer"
    },
    {
        "nama_lengkap" : "Tono",
        "divisi" : "Programmer"
    },
    {
        "nama_lengkap" : "Toni",
        "divisi" : "Programmer"
    },
    {
        "nama_lengkap" : "Siti",
        "divisi" : "Programmer"
    },
    {
        "nama_lengkap" : "Siska",
        "divisi" : "Desain"
    },
    {
        "nama_lengkap" : "Jono",
        "divisi" : "Product Manager"
    },
]

def cetak_profile(nama,divisi):
    print(f"Nama : {nama}")
    print(f"divisi : {divisi}")
    print(f"===============")
    
print("=======foreach ======")
for value in data_kariawan:
    cetak_profile(value["nama_lengkap"],value["divisi"])
    
    

print("=====while======")
# kondisi akan di lihat terlebih dahulu dan memahami syarat yang di berikan
# count = 5
# harus tau syarat apa yang akan memberhentikan putran
count = 0
while count < 5:
    print("ini akan muncul terus menerus")
    count += 1
    
print("======break and countinue=======")
count = 1
while count <= 100:
    if count % 2 == 0:
        count += 1
        continue # di gunakan untuk melakakukan skip (melewati) 1 putaran
    print(count)
    count += 1
    if count == 30:
        break # memaksa untuk memberhentikan putran
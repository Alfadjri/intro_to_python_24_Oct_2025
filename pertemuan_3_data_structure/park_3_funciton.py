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
        "nama_lengkap" : "Siska",
        "divisi" : "Desain"
    },
    {
        "nama_lengkap" : "Jono",
        "divisi" : "Product Manager"
    },
]

#format dasar function
#def namaFunction(paramter):
#  Kegiatan apa yang mau kamu lakukan

# function void
# function yang tidak mengelurkan apa pun hasilnya 
def cetak_profile(nama,divisi):
    print(f"Nama : {nama}")
    print(f"divisi : {divisi}")
    print(f"===============")

print(f"=======List Divisi=======")
cetak_profile(data_kariawan[0]["nama_lengkap"],data_kariawan[0]["divisi"])
cetak_profile(data_kariawan[1]["nama_lengkap"],data_kariawan[1]["divisi"])
cetak_profile(data_kariawan[2]["nama_lengkap"],data_kariawan[2]["divisi"])
cetak_profile(data_kariawan[3]["nama_lengkap"],data_kariawan[3]["divisi"])
cetak_profile(data_kariawan[4]["nama_lengkap"],data_kariawan[4]["divisi"])

# function non void
def luas_persegi_panjang(panjang,lebar):
    hasil = panjang * lebar
    return hasil #ini yang sebutnya mengeluarkan nilai

hasil_penjumlahan_luas_persegi = luas_persegi_panjang(2,5)
print(f"Luas dari pesegi dengan lebar 2 dan panjang 5 adalah {hasil_penjumlahan_luas_persegi}")
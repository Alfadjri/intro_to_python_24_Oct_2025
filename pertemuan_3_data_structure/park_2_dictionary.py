#case
# kelas 
data_kelas = {
    "kelas" : 12,
    "jurusan" : ["IPA","IPS"],  
    "nama_ketua" : "Udin",
}

# Read
print(f"List Dicrionary : {data_kelas}")
# read spesifik
print(f"Nama dari ketua kelas : {data_kelas["nama_ketua"]}")
print(f"Cara mengambil jurusan IPS : {data_kelas["jurusan"][1]}")

# add value
data_kelas["jumlah_siswa"] = 40
print(f"List Dicrionary setelah di add : {data_kelas}")
# update
data_kelas["jurusan"] = "IPS"
print(f"List Dicrionary setelah di update : {data_kelas}")
# delete
del data_kelas["jumlah_siswa"]
print(f"List Dicrionary setelah di delete : {data_kelas}")
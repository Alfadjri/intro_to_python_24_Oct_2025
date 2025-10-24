# jenis-jenis makanan

# C (Create)
# instansiasi 
# instansiasi adalah proses persiapan variabel yang akan di pakai 
type_data = []

# CRUD
# add 
type_data.append("nasi") #ini di akhir data
type_data.append("ikan")
type_data.append("ayam bakar")
type_data.append("Semangka")
type_data.insert(1,"Jagung") # insert(mau_diselipkan_setelah_index_ke_berapa,valuenya_APA)

# Read
print(f"All list Data :{type_data}")
# read spesifik value
print(f"index ke 2 : {type_data[2]}")

# update
type_data[4] = "Tomat"
print(f"All list Data update index ke 4 :{type_data}")

# Delete
del type_data[2]
print(f"All list Data delete index ke 2 :{type_data}")

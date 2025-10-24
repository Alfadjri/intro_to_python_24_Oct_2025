kondisi_1 = 10
kondisi_2 = 12

# lebih besar 
hasil_kondisi = (kondisi_1 > kondisi_2)
print(f"Apakah nilai {kondisi_1} lebih besar (>) dari {kondisi_2} adalah {hasil_kondisi} ")
# lebih kecil 
hasil_kondisi = (kondisi_1 < kondisi_2)
print(f"Apakah nilai {kondisi_1} lebih kecil (<) dari {kondisi_2} adalah {hasil_kondisi} ")

kondisi_1 = 12
kondisi_2 = 12
# Besar dari sama dengan
hasil_kondisi = (kondisi_1 >= kondisi_2)
print(f"Apakah nilai {kondisi_1} lebih besar sama dengan (>=) dari {kondisi_2} adalah {hasil_kondisi} ")

# kecil dari sama dengan
hasil_kondisi = (kondisi_1 <= kondisi_2)
print(f"Apakah nilai {kondisi_1} lebih kecil sama dengan (<=) dari {kondisi_2} adalah {hasil_kondisi} ")

# Gerbang logika 
# di pakai saat punya 2 atau lebih kondisi
# and 
# kedua kondisi harus bernilai true baru akan di jalankan
hasil_kondisi = (kondisi_1 <= kondisi_2) and (kondisi_1 < kondisi_2)
print(f"apakah kondisi pertama dan ke dua benar : {hasil_kondisi}")
# or
# salah satu kondisi harus bernilai benar baru akan di jalankan
hasil_kondisi = (kondisi_1 <= kondisi_2) or (kondisi_1 < kondisi_2)
print(f"apakah kondisi pertama dan ke dua benar : {hasil_kondisi}")

kondisi_1 = "Hasil"
kondisi_2 = "hasil"
hasil_kondisi = (kondisi_1 == kondisi_2)
print(f"Apakah nilai {kondisi_1} sama dengan (==) {kondisi_2} adalah {hasil_kondisi} ")
# logika not (!)
kondisi_1 = True
hasil_kondisi = kondisi_1 != True
print(f"Apakah nilai {kondisi_1} tidak sama dengan (!=) {True} adalah {hasil_kondisi} ")



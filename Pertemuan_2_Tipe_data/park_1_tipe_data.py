# komentar / pagar (#)
# tipe data yang tidak akan pernah di eksekuksi sama program
# di gunakan untuk menandai atau mematikan tulisan dalam coding sementara 

# tipe data numeric
# integer 
a = 10 
print("Contoh tipe data integer (int) : {0}".format(a))
b = 3.14
print("Contoh tipe data float (float) : {0}".format(b))
c = 2 + 3j # j bilangan imajiner
print("contoh tipe data complex (complex) : {0}".format(c))

# tipe sequence
# list
d = [1,2,3,4,5,6,7,8]
print("contoh tipe data list (list) : {0}".format(d))
# truplet
e = (4,5,6)
print("contoh tipe data truplet (list) : {0}".format(e))
# range
f = range(1,5)
print("contoh tipe data range (range) : {0}".format(f))

# type String
nama_lengkap = "Alfadjri Dwi Fadhilah"
print("contoh tipe data string (str) : {0}".format(nama_lengkap))

# type maping
profile = {
    "nama" : "Alfadjri Dwi Fadhilah",
    "usia" : 25,
}
print("contoh tipe data maping (dict) : {0}".format(profile))

# type set
g = {1,2,3}
print("contoh tipe data set (set) : {0}".format(g))
h = frozenset({4,5,6,7})
print("contoh tipe data frozenset (frozenset) : {0}".format(h))

# type boolean
# cuman bisa di sisi salah satu True (1) or Flase (0)
kondisi_badan = True
print("contoh tipe data boolean (bol) : {0}".format(kondisi_badan))

# Tipe binary
i = 0b01000001
# desimal = int(i)
# char = chr(desimal)
char = chr(int(i))
print(char)
j = bytearray(d)
print(j)
k = memoryview(j)
print(k)
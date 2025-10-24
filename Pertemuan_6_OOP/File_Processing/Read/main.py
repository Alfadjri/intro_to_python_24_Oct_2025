file = open("../Write/ContohPesanRahasia.txt","r")
read_ = file.read()
print("Value file ContohPesanRahasia.txt :")
print(read_)
file.seek(0)
# Mengambil 3 karkter
print("Mengambil 3 karter dari ContohPesanRahasia.txt :")
print(file.readline(3))
# mengambil 1 baris
file.seek(0)
print("Mengambil 1 bari dari ContohPesanRahasia.txt : ")
for line in file.readlines():
    print(line.strip())
    break

file.close() # membebaskan file dari execution
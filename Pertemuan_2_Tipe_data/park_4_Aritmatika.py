x = 3
y = 2

# penjumlahan
hasil = x + y
hasil_penjumlahan = hasil
#hasil = "Rp." + str(hasil) #string concenate atau menyambungkan string
print(f"Hasil penjumlahan dari {x} + {y} = {hasil}")
# pengunrangan
hasil = x - y
print(f"Hasil kurang dari {x} - {y} = {hasil}")
#kali
hasil = x * y
print(f"Hasil kali dari {x} * {y} = {hasil}")
#pembagian
hasil = x / y
print(f"Hasil pembagian dari {x} / {y} = {hasil}")
hasil = x // y
print(f"Hasil pembagian dari {x} // {y} = {hasil}")
# modulus
hasil = x % y
print(f"Hasil modulus dari {x} % {y} = {hasil}")

# incerment
# hasil = hasil + 6
hasil_penjumlahan += 6
print(f"Hasil akhir {hasil_penjumlahan}")
# decerment
hasil_penjumlahan -= 6
print(f"Hasil akhir {hasil_penjumlahan}")
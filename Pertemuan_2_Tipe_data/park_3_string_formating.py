kota = "Bandung"
tanggal = "10/Oct/2025"
jumlah_lampiran = 1
nama_atasan = "Gabriella Marsela"
jabatan = "Academic Team"
nama_perusahaan = "PT Semua Mahir Teknologi"
alamat ="PT Semua Mahir Teknologi Depan Mall Grand Galaxy Park, Jl. Boulevard Raya RGJ 532, Kota Bekasi"

# posisional argument
# \n = new line (enter)
print("{0},{1}\nPerihal:Surat Izin Sakit\nLampiran:{2}\n\nKepada Yth,\n{3}\n{4}\n{5}\n{6}".format(kota,tanggal,jumlah_lampiran,jabatan,nama_atasan,nama_perusahaan,alamat))
print("============")
# keyword argument
print("{kota},{tanggal}\nPerihal:Surat Izin Sakit\nLampiran:{jumlah_lampiran}\n\nKepada Yth,\n{nama_atasan}\n{jabatan}\n{nama_perushaan}\n{alamat}".format(kota =kota,tanggal=tanggal,jumlah_lampiran=jumlah_lampiran,jabatan=jabatan,nama_atasan=nama_atasan,nama_perushaan=nama_perusahaan,alamat=alamat))
print("============")
# shorcut formating
print(f"{kota},{tanggal}\nPerihal:Surat Izin Sakit\nLampiran:{jumlah_lampiran}\n\nKepada Yth,\n{nama_atasan}\n{jabatan}\n{nama_perusahaan}\n{alamat}")
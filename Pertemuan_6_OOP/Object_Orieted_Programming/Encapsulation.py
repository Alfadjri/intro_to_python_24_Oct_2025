#Case
#mobil

class Mobil : 
    warna = "Putih" 
    _pelek_ban = "T37"  # object encapsulation 
    __logo_mobil = "mitsubisi" # object encapsulation
    
    def __init__(self,merek , jesnis , warna):
        self.warna = warna
        self.merek = merek
        self.jenis = jesnis
    
    def getProfile(self):
        print(f"merek : {self.merek}")
        print(f"warna : {self.warna}")
        print(f"jenis : {self.jenis}")
        print(f"pelek : {self._pelek_ban}")
        print(f"logo Mobil : {self.__logo_mobil}")
    # setter and getter
    # set itu di gunakan untuk merubah nilai
    # get itu untuk mengambil nilai
    #set
    def setPelek(self,nama_pelek):
        self._pelek_ban = nama_pelek
        
        
lancer = Mobil("Mitsubisi","Lancer","Hitam") 
lancer.getProfile()
print("===============")
lancer.setPelek("Lancer Ring")
lancer.getProfile()
#Case
#mobil
class Mobil() : 
    warna = "Putih" 
    _pelek_ban = "T37"  
    __logo_mobil = "mitsubisi" 
    
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
        
    def setPelek(self,nama_pelek):
        self._pelek_ban = nama_pelek
        
    def klaksonMobil(self):
        pass
        
class Mitsubisi(Mobil): 
    def __init__(self, merek, jesnis, warna):
        super().__init__(merek, jesnis, warna)
    
    def kenalpot(self):
        print("Jumlah Kenalopot : 4 silinder ")
    
    def klaksonMobil(self):
        print("Tuuuuttttttt")

class Honda(Mobil):
    def __init__(self, merek, jesnis, warna):
        super().__init__(merek, jesnis, warna)
    
    def kenalpot(self):
        print("Jumlah Kenalopot : 2 silinder ")
    
    def klaksonMobil(self):
        print("Teeetttoooottt")

class Toyota(Mobil):
    def __init__(self, merek, jesnis, warna):
        super().__init__(merek, jesnis, warna)
    
    def kenalpot(self):
        print("Jumlah Kenalopot : 1 silinder ")
    
    def klaksonMobil(self):
        print("Pakai Strobo")
        
    
def getKelakson(Mobil): #polymopisme
    Mobil.klaksonMobil()
        
        
lancer = Mitsubisi("Mitsubisi","Lancer","Hitam")
getKelakson(lancer)
civic = Honda("Honda","Civic","hitam")
getKelakson(civic)
toyota = Toyota("Toyota","Avanza","Hitam")
getKelakson(toyota)

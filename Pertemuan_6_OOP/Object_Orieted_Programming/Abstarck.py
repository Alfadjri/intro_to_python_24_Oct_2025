#Case
#mobil
from abc import ABC,abstractclassmethod

class Mobil(ABC) : 
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
        
    @abstractclassmethod
    def klaksonMobil(self):
        pass #abstrack 
        
class Mitsubisi(Mobil): #inheritance
    def __init__(self, merek, jesnis, warna):
        super().__init__(merek, jesnis, warna)
    
    def kenalpot(self):
        print("Jumlah Kenalopot : 4 silinder ")
    
    def klaksonMobil(self): #overrider method menulis ulang metod abstrack agar untuk masing" class
        print("Tuuuuttttttt")
        
        
lancer = Mitsubisi("Mitsubisi","Lancer","Hitam") 
lancer.getProfile()
lancer.kenalpot()
lancer.klaksonMobil()
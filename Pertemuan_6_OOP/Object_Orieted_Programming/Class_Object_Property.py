#Case
#mobil

class Mobil : #Mobil di sebut name class dan ini contoh class
    #property public
    # object yang mudah di ganti dan boleh di ganti sama siapapun
    warna = "Putih" # warna di sebut object
    #property private
    # object yang tidak mudah di ganti tapi di perbolehkan
    _pelek_ban = "T37" 
    # property protected
    # object yang tidak bisa di ubah di luar kelas tersbut
    __logo_mobil = "mitsubisi"
    
    def __init__(self,merek , jesnis , warna):
        self.warna = warna
        self.merek = merek
        self.jenis = jesnis
    
    def getProfile(self): #ini sebutanya method
        print(f"merek : {self.merek}")
        print(f"warna : {self.warna}")
        print(f"jenis : {self.jenis}")
        print(f"pelek : {self._pelek_ban}")
        print(f"logo Mobil : {self.__logo_mobil}")
        
        
        
honda = Mobil("Honda","Civic","Hitam") 
honda.getProfile()
print("====================")
# contoh perubah object
honda.merek = "Mitsubisi" # di sini merubah objectnya 
honda.jenis = "Lancer"
honda.getProfile()
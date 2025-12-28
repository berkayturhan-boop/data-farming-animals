from farm.animal import Animal

class Chicken(Animal):
    def __init__(self, gender):
        super().__init__()
        self.gender = gender
        self.eggs = 0  # Testlerin beklediği yumurta sayacı
    
    def talk(self):
        if self.gender == 'male':
            return "cock-a-doodle-doo" # Testin beklediği İngilizce ses
        return "cluck cluck" # Dişi sesi de İngilizce olsun (garanti olsun)

    def feed(self):
        super().feed() # Önce enerjiyi artır (Animal sınıfından)
        if self.gender == 'female':
            self.eggs += 2 # Teste göre dişi tavuk beslenince 2 yumurta veriyor
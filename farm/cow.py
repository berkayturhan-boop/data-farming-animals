from farm.animal import Animal

class Cow(Animal):
    def talk(self):
        return "Mööö"

    def produce(self):
        # Enerjisi varsa süt verir, enerjisi 1 azalır
        if self.energy > 0:
            self.energy -= 1
            return 10  # Örneğin 10 litre süt versin
        return 0

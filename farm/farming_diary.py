from farm.cow import Cow
from farm.chicken import Chicken
# Animal importuna gerek yok, çünkü burada doğrudan Animal kullanmıyoruz, türetilenleri kullanıyoruz.

print("\n\n📝 Üçüncü Gün: Hayvanlar Konuşuyor")

# 1. Sınıfları çağırma
cow = Cow()
female_chicken = Chicken('female')
male_chicken = Chicken('male')

print(f"İnek {cow.talk()} diyor.")
print(f"Dişi tavuk {female_chicken.talk()} diyor.")
print(f"Erkek tavuk {male_chicken.talk()} diyor")

print("\n\n📝 Dördüncü Gün: Hayvanları Besle")

# 1. Tüm hayvanlarını `animals` listesinde sakla
animals = [cow, female_chicken, male_chicken]

# 2. Her hayvan için `feed` yöntemini çağır
for animal in animals:
    animal.feed()
    # Kontrol etmek istersen enerjilerini yazdırabilirsin:
    # print(f"Hayvan beslendi! Yeni enerji: {animal.energy}")

# 3. TODO'ları değiştirin ve çıktıları yazdırın
cow_produce = cow.produce()
female_produce = female_chicken.produce()
male_produce = male_chicken.produce()

# 4. Aşağıdaki 3 satırı yazdırın:
print(f"İnek {cow_produce} litre süt üretti")
print(f"Dişi tavuk {female_produce} yumurta üretti")
print(f"Erkek tavuk {male_produce} yumurta üretti")
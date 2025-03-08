# Kullanıcıdan 5 sayı alıp listeye ekleme ve işlemler yapma
sayilar = []
for _ in range(5):
    sayi = int(input("Bir sayı girin: "))
    sayilar.append(sayi)

toplam = sum(sayilar)
ortalama = toplam / len(sayilar)
en_buyuk = max(sayilar)
en_kucuk = min(sayilar)

print(f"Toplam: {toplam}, Ortalama: {ortalama}, En Büyük: {en_buyuk}, En Küçük: {en_kucuk}")

# Kullanıcıdan kelimeler alıp ters sıralama
kelimeler = []
for _ in range(5):
    kelime = input("Bir kelime girin: ")
    kelimeler.append(kelime)

kelimeler.sort(reverse=True)
print("Ters sıralı kelimeler:", kelimeler)

# Tekrar eden elemanları kaldırma
liste = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
tekrarsiz_liste = list(set(liste))
print("Tekrarsız liste:", tekrarsiz_liste)

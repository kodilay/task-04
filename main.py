sayi_listesi = []
for i in range(5):
    sayi = float(input(f"{i+1}. sayıyı giriniz: "))
    sayi_listesi.append(sayi)

toplam = sum(sayi_listesi)
ortalama = toplam / len(sayi_listesi)
en_buyuk = max(sayi_listesi)
en_kucuk = min(sayi_listesi)

print(f"Toplam: {toplam}")
print(f"Ortalama: {ortalama}")
print(f"En Büyük: {en_buyuk}")
print(f"En Küçük: {en_kucuk}")

kelime_listesi = []
kelime_adedi = int(input("Kaç kelime gireceksin? "))
for i in range(kelime_adedi):
    kelime = input(f"{i+1}. kelimeyi giriniz: ")
    kelime_listesi.append(kelime)

kelime_listesi.reverse()
print(kelime_listesi)

liste = [1, 2, 3, 2, 4, 1, 5, 3]
liste_set = set(liste)
yeni_liste = list(liste_set)

print(yeni_liste)

# # ekrana ard arda 5 sayı isteyen ve en büyük ve en küçük sayıyı yazan kodu yaz
# liste = []
#
# for i in range(5):
#     sayi = int(input("Sayınızı giriniz."))
#     liste.append(sayi)
#
# print(f"{max(liste)}En büyük sayı")
# print(f"{min(liste)}En küçük sayı")
# metin = input("Bir metin giriniz.")
# sozluk = dict()
# for harf in metin:
#     if harf in sozluk:
#         sozluk[harf] += 1
#     else:
#         sozluk[harf] = 1
# for harf,adet in sozluk.items():
#     print(harf,adet)

# # ekrandan okunan bir metinde a harflerini büyük yapan bir program yazınız.
# metin = input("Bir metin giriniz: ")
#
# metin2 = ""
#
# for harf in metin:
#     if harf == "a":
#         metin2 += "A"
#     else:
#         metin2 += harf
# print(metin2)

# ilk 10.000 asal sayının kaç tanesi 3 ile başlar 7 ile biter?
prime_list = list()

prime_list.append(2)

sayi = 3

while True: #while sonsuz bir döngü gibi bir şey ben çık diyene kadar döndürür.
    prime = True
    for i in range(2,int(sayi ** 0.5) + 1):
        if sayi %i == 0: # eğer benim sayım i'ye tam bölünüyorsa yani kalan 0 ise asal sayı değildir.
            prime = False
            break
    if prime:
        prime_list.append(sayi)
        if len(prime_list) == 10000:
            break
    sayi += 1
liste2 = []
for prime in prime_list:
    strprime = str(prime)
    if strprime.startswith("3") and strprime.endswith("7"):
        liste2.append(prime)
print(liste2)
print(len(liste2))





















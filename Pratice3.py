demet = (1,2,3,4)
abe = "1,2,3,4"
# i'nin amacı i sırayla print ediyor yani şöyle i 1 oluyor sonra 2 oluyor sonra 3 sonra 4 oluyor hepsini sıralı bir şekilde yazdırıyor.
for i in demet:
    print(i)
for i in abe:
    print(i)

for i in range(0,10): #Bu kısımda 0 dan 9 a kadar yazdırıyor çünkü 2. olan rakama kadar alıyor. kendisini almıyor.
    print(i)
# üstteki range ile yaptığımızı 2 şer 2 şer yapmak için ise 2 sayının sonuna , 2 koyarız. farklı rakamlarda kullanabiliriz.
for i in range(1,15,2):
    print(i)
# çarpım işlemi yapmak için
sonuc = 1
for i in range(10):
    sonuc *= 2
print(sonuc)
# for döngülerini iç içe kullanmak:
liste1 = ["a","b","c"]
liste2 = [1,2,3]

for harf in liste1:
    for rakam in liste2:
        print(harf,rakam)
# continue = eğer listenin içinden herhangi bir rakamı yazdırmak istemiyorsak ve devam etmesini istiyorsak i == 3 yaparız ve 3. sayıyı yazdırmayız.
liste = [1,2,3,4,5,6,7,8,9]
for i in liste:
    if i == 3:
        print("Burada'ki sayıyı atladık.")
        continue
    print(i)

# break = continue'nin aynısı sadece herhangi bir sayıya kadar (mesela 3 e kadar ama 3 dahil değil) yazdırdıktan sonra durmak istediğimizde kullanırız.
for i in liste:
    if i == 3:
        break
    print(i)

# Range = altta'ki komut 0 dan 99 a kadar sayacak bir komuttur.
list = range(100)
# 3 erli 3 erli 0 dan 100 e kadar saydırmak için
for i in list:
    if i % 3 != 0:
        continue
    #     3 erli 3 erli 81 e kadar sayması için fakat burada 81 oldumu durma komutu uyguladık.
    if i == 81:
        break
    print(i)
# while : x < 10 yani x 10'dan küçükse x 10 olana kadar 1 arttır.
x = 2
while x < 10:
    print(x)
    x += 1 #x + 1 demek yani x'i 1 arttır.
print("x =", x)

c = 2
d = 3
while c * d < 1000:
    print(c,d)
    c += 2
    d += 2
# Asal sayılar.
soru = int(input("Lütfen Sayınızı Giriniz:"))
deger = True
for i in range(2,soru):
    if soru %i == 0:
        deger = False
        break
if deger == True:
    print(f"{soru} sayısı asal sayıdır.")
else:
    print(f"{soru} Bu sayı asal değildir.")

metin = input("Bir metin giriniz.")
sozluk = dict()
for harf in metin:
    if harf in sozluk:
        sozluk[harf] += 1
    else:
        sozluk[harf] = 1
for harf,adet in sozluk.items():
    print(harf,adet)

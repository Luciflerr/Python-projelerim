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

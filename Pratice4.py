# Ekranda asal sayı olup olmadığını kontrol eden bir program yazın.
asal = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

soru = int(input("Lütfen sayı giriniz."))
print(soru)

for i in asal:
    if i == soru:
        print("Bu sayı bir asal sayıdır.")
        break
    if not i == soru:
        print("Bu sayı asal sayı değildir.")
        break


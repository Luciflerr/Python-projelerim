# if operatörü doğruysa bloğunda'ki elemanları çalıştırır mesela
if True:
    print("Koşul true ise yazıyı aşağıda görebiliriz.")
# False olduğu için üstteki yazının altına bir şey yazılmayacak.
if False:
    print("False olduğu için hiçbir şey yazmayacak.")

# Eşittir "==", Eşit Değildir : "!=", Büyüktür ">", Küçüktür "<" Büyük veya eşittir ">=" , Küçük veya eşittir "<=".

a = 5
b = 5
if a == b:
    print("a eşittir b'ye")
c = 6
d = 10
if c != d:
    print("c eşit değildir d'ye")

# if eğer öyleyse if komutunu çalıştır demek, Else ise eğer öyle değilse else'nin altında'ki komutu çalıştır demek
ayse = 21
fatma = 20
if ayse == fatma:
    print("ayse eşittir fatma")
else:
    print("ayse eşit değil fatmaya")
# elif koşuluysa if değilse elif oluyor yani öyle değilse böyledir demek gibi bir şey.
# else eğer bunların hiçbiri değilse ortaya çıkacak olan koşul.
renk = "Turkuaz"
if renk == "Beyaz":
    print("Beyaz")
elif renk == "Mavi":
    print("Mavi")
elif renk == "Gri":
    print("Gri")
else:
    print("Hiçbiri")

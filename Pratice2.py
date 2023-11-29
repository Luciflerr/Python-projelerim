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
merve = 19
caner = 18
elsa = 19
# -------------OR kullanımı------- ikisinden biri doğru olmak zorunda.
# or'da ikisinden biri doğru olsa bile sonucunda if çalışır fakat and kullanımında hepsi doğru olmak zorunda eğer yanlışsa else çalışır.
if elsa == merve or caner == elsa:
    print("Koşul doğru")
else:
    print("Koşul yanlış")
# ----------------and------------ ikisi birden doğru olmak zorunda.
if caner == elsa and caner < merve:
    print("Koşul doğru")
else:
    print("Koşul yanlış")
# ----------------in-------------
liste = [1,2,3,4,6,7,8,9]
ca = 5
if ca in liste:
    print("Liste'de var.")
else:
    print("Liste'de yok.")

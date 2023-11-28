name = "eray"
age = 27
gpa = 1.9
student = True

# bir değeri farklı bir değere çevirmek istiyorsak mesela float'ı int'e çevirmek istiyorsak şu şekilde yapabiliriz
gpa = int(gpa)
# gpa seçme sebebim gpa üstte float ama biz int'e çeviriyoruz.
print(gpa)
# Şuanda gpa'mız 1 olarak gözüküyor. Bu sefer age'imizi float'a dönüştürelim.
age = float(age)
print(age)
# age'miz 27.0 olarak gözükür çünkü üst kısımda'ki kod'da bunu yapmasını söyledik.

# eğer bir şeyi boolean yapmak istiyorsak bool(age) yazmalıyız ve eğer age = 0 iste False olacaktır fakat 0 harici herşey
# için durum True olacaktır yani age = 1 veya 110120120 veya -123423 olsa bile her zaman True olacaktır. 
# listeler
renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
print(type(renkler))
# Listemizde kaç tane renk var?
print(len(renkler))
# renkler listesinin 1. rengini çıktı olarak ver: 0.renk siyah, 1. renk Beyaz 2.renk sarı diye gidiyor.
print(renkler[1])
# renkler listesinin 1.renginden 4.rengine kadar yazdır.
# bu sırada 1.renkten başlar 4.renge kadar yazar ama 4.rengi yazmaz.
print(renkler[1:4])
# 2şer 2şer yazdır. Yani Siyah, Sarı, Yeşil yazmalı.
print(renkler[::2])
# 0.indekse gri eklemek için:
renkler.insert(0, "Gri")
print(renkler)
# remove ile renklerden Siyah'ı sil
renkler.remove("Siyah")
print(renkler)
# Listeye birden fazla renk ekle extend metoduyla.
renkler2 = ["Turuncu", "Pembe"]
renkler.extend(renkler2)
print(renkler)
# Eğer yukarıda'ki muhabbeti extend değilde append ile yapsaydın şu şekilde:
# ['Turuncu', 'Pembe'] olurdu ama olması gereken üstteki gibidir.
renkler.append(renkler2)
print(renkler)
# Listeler [içine yazılır]
# Listelerde append ile listenin sonuna bir şey ekleyebiliriz fakat
# kümelerde bu böyle değildir.
# kümeler {içine yazılır ayrıca print verince elemanları random verir çünkü sıralama diye bir anlam yok.}
kume = {"Sarı", "Mavi", "Yeşil", "Kırmızı", "Siyah"}
print(kume)
kume.add("Pembe")
print(kume)
kume.remove("Sarı")
print(kume)
# olmayan bir rengi silmek için ise discard yapabiliriz. remove ile yaparsak hata alırız.
kume.discard("Gri")
print(kume)
# intersection : belirli bir kümenin içinden diğer kümeyle "aynı" olan ifadeleri yazdırır.
kume2 = {"Sarı", "Mavi", "Yeşil", "Turkuaz", "Mor"}
print(kume.intersection(kume2))
# difference : belirli bir kümenin içinden diğer kümeyle "farklı" olan ifadeleri yazdırır.
print(kume.difference(kume2))
# union : farklı kümeleri birleştirir. Aynı elemanı eklemez. Aynı eleman 1 tane olur.
print(kume.union(kume2))
# "Beyaz" in kume = kume içerisinde "beyaz" eleman var mı? Var ise true değerini verir.
print("Beyaz" in kume)
# "Sarı" in kume.union(kume2) = kume içerisinde "Sarı" eleman var mı? Var ise true değerini verir.
print("Sarı" in kume.union(kume2))
# Bos liste oluşturmak için
bosliste1 = []
bosliste2 = list()
# bos küme için
boskume1 = {}
boskume2 = set()
python = set("PYTHON")
set1 = set([1,2,3,4,5])
print(python)
print(set1)

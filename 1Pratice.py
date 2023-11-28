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

# kümeler {} içine yazılır ayrıca print verince elemanları random verir.
kume = {"Sarı", "Mavi", "Yeşil", "Kırmızı", "Siyah"}
print(kume)

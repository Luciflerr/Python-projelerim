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

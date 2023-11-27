# Bu basit bir hesap makinesidir.
operator = input("Lütfen yapacağınız işlemi seçiniz. (+ - * / ): ")
num1 = float(input("Lütfen 1. Rakamı giriniz."))
num2 = float(input("Lütfen 2. Rakamı giriniz."))

if operator == "+":
    sonuc = num1 + num2
    print(round(sonuc, 3))
elif operator == "-":
    sonuc = num1 - num2
    print(round(sonuc, 3))
elif operator == "*":
    sonuc = num1 * num2
    print(round(sonuc, 3))
elif operator == "/":
    sonuc = num1 / num2
    print(round(sonuc, 3))
else:
    print(f"{operator} seçtiğiniz işlem işlevsel değil.")

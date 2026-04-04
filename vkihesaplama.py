kilo = input("Kilonuzu giriniz:")
boy = input("Boyunuzu metre olarak giriniz:")
bmi = float(kilo) / (float(boy) ** 2)
if bmi < 18.5:
    print("Zayıfsıınız, kilo almanız önerilir, BMI:")
elif  bmi > 18.5 and bmi < 24.9:
    print("Normal kilodasınız, BMI:")
elif  bmi > 25 and bmi < 29.9:
    print("Fazla kilolusunuz, sağlıklı beslenmeniz önerilir, BMI:")
else:   print("Obezsiniz, diyetisyen ile görüşmeniz önerilir, BMI:")
bmi = round(bmi, 2)
print(bmi)

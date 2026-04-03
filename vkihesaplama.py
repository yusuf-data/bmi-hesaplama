kilo = input("Kilonuzu giriniz:")
boy = input("Boyunuzu metre olarak giriniz:")
bmi = float(kilo) / (float(boy) ** 2)
if bmi < 18.5:
    print("Zayıfsıınız, BMI:", bmi)
elif  bmi > 18.5 and bmi < 24.9:
    print("Normal kilodasınız, BMI:", bmi)
elif  bmi > 25 and bmi < 29.9:
    print("Fazla kilolusunuz, BMI:", bmi)
else:   print("Obezsiniz, BMI:", bmi)
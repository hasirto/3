para=int(input("ne kadar para istiyosun"))
print("15 TL faiz uyguluyorum haberin olsun")
ay=int(input("paramı kaç ay sonra verirsin kardeşim"))

for i in range(ay):
    para=para+15 # her ay 15 lira faiz uyguluyor
    print(para,"TL")


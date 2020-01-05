import random
x = int(random.uniform(1,10))

for i in range(3):
    tahmin=int(input("bir sayı tahmin et"))
    if x<tahmin:
        print("asagi")
    if x>tahmin:
        print("yukari")
    if x==tahmin:
        print("doğru cevap")
        break
    if i==1:
        print("bu son hakkın ha")
    if i==2:
        print("bilemedin mi")

dosya1 = open('mecburum_kisa.txt')
print(dosya1)
print("Dosya Acma Yontem-1: \n", dosya1.read(), "\n***\n")

dosya2 = open('mecburum_kisa.txt', 'r')
print(dosya2)
print("Dosya Acma Yontem-2: \n", dosya2.read(), "\n***\n")

dosya3 = open(file='mecburum_kisa.txt', mode='r')
print(dosya3)
print("Dosya Acma Yontem-3: \n", dosya3.read(), "\n***\n")

dosya4 = open(file='mecburum_kisa.txt', mode='r', encoding='utf-8')
print(dosya4)
print("Dosya Acma Yontem-4: \n", dosya4.read(), "\n***\n")

with open('mecburum_kisa.txt', 'r', -1, "utf-8") as dosya5 :
    print(dosya5)
    print("Dosya Acma Yontem-5: \n", dosya5.read(), "\n***\n")

with open('mecburum_kisa.txt', 'r', encoding="utf-8") as dosya6:
    print(dosya6)
    print("Dosya Acma Yontem-6: \n", dosya6.read(), "\n***\n")

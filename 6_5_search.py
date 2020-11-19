def search(sayidizisi,aranan):
    for sayi in sayidizisi:
        if sayi == aranan :
            return "found"

while True:
    try:
        aranan = int( input('sayi gir: '))
        break;
    except:
        print('tam sayi giriniz')

sayilar = [23,45,1,4,5,7,8,99,12,3]
sonuc = search(sayilar, aranan)
print(sonuc)

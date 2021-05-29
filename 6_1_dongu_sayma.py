kelime = input('İşlem yapılacak kelime ya da cumleleri giriniz:')
arananKarakter = input('Aranacak karakteri giriniz:')

count = 0
for karakter in kelime:
    if karakter == arananKarakter:
        count += 1

print('Aranan karakter',count,'adet bulunmaktadir')

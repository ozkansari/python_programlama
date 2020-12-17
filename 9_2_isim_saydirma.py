# listeyi olustur
isimler = list()
while(True):
    isim = input('isim giriniz, cikmak icin bos birakiniz:')
    if isim == '':
        break;
    isimler.append(isim)
print('isimler: ', isimler)

#isimleri say
isim_sayilari = dict()
for isim in isimler:
    isim_sayilari[isim] = isim_sayilari.get(isim,0) + 1;
print('isim sayıları: ', isim_sayilari)

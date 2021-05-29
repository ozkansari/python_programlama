def aravedegistir(girdiString, arananParca, yerineGelecek):
    indis = girdiString.find(arananParca)
    baslangic = indis + len(arananParca)
    sonuc = girdiString[:indis] + yerineGelecek + girdiString[ baslangic: ]
    return sonuc

gs = input('Input giriniz: ') # "Hello Bob"
ap = input('Aranacak parcayi giriniz: ') # "Hello"
yg = input('Yerine gelecek: ') #"Jane"

print('sonuc: ', aravedegistir(gs,ap,yg) ) # "Jane Bob"

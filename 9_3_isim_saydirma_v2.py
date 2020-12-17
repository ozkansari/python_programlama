# listeyi olustur
isimler = list()
isim_girisi = input('isimleri boslukla ayirarak giriniz: ')
isimler = isim_girisi.split()
print('isimler: ', isimler)

#isimleri say
isim_sayilari = dict()
for isim in isimler:
    isim_sayilari[isim] = isim_sayilari.get(isim,0) + 1;
print('isim sayıları: ', isim_sayilari)

# en fazla sayida gecen ismi bul
en_yaygin_isim = None
en_yaygin_isim_adeti = None
for isim,adet in isim_sayilari.items():
    if en_yaygin_isim_adeti is None or adet > en_yaygin_isim_adeti :
        en_yaygin_isim = isim
        en_yaygin_isim_adeti = adet
print('En yaygın isim ve adedi: ', en_yaygin_isim, en_yaygin_isim_adeti)

# en fazla sayida gecen ismi bul v2
en_yaygin_isim = list()
en_yaygin_isim_adeti = None
for isim,adet in isim_sayilari.items():
    if en_yaygin_isim_adeti is None or adet >= en_yaygin_isim_adeti :
        en_yaygin_isim.append(isim)
        en_yaygin_isim_adeti = adet
print('En yaygın isimler ve adedi: ', en_yaygin_isim, en_yaygin_isim_adeti)

# en fazla sayida gecen ismi bul v3
sirali_sozluk = list()
for isim,adet in isim_sayilari.items():
    sirali_sozluk.append( (adet,isim) )
sirali_sozluk = sorted(sirali_sozluk, reverse=True)
print(sirali_sozluk[0])

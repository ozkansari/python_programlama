with open('mecburum.txt','r',encoding='utf-8') as in_file:

    kelime_sayisi = 0
    harf_sayisi = 0

    for satir in in_file :
        for kelime in satir.split():
            kelime_sayisi = kelime_sayisi + 1
            harf_sayisi = harf_sayisi + len(kelime)

print('Sonuc: ', 'Kelime sayisi: ', kelime_sayisi, 'Harf sayisi: ', harf_sayisi)

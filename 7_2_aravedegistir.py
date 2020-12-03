# -----------------------------------------------------------------------------
def aravedegistir(girdiString, arananParca, yerineGelecek):
    sonuc = girdiString
    indis = -1
    while True:
        indis = sonuc.find(arananParca,indis+1)
        if(indis == -1):
            break

        ilkParca = sonuc[ : indis] + yerineGelecek
        if(indis + len(arananParca) < len(sonuc)):
            sonuc = ilkParca + sonuc[ indis + len(arananParca) : ]
        else:
            sonuc = ilkParca
    return sonuc
# -----------------------------------------------------------------------------

print(aravedegistir('Selam Bob. Nasılsın Bob?','Bob','Janet'))

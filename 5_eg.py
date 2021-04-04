def ucretHesapla(a,b):
    hesaplananUcret = a*b
    return hesaplananUcret

while True :
    try:
        calisilanSaat = float(input("Calisilan Saat nedir?"))
        saatlikUcret = float(input("Saatlik Ucret Nedir?"))
        sonuc = ucretHesapla(calisilanSaat,saatlikUcret);
        print("Hesaplanan Ucret: ", sonuc )
    except:
        print('HATALI GIRDI')

    tekrarHesaplansinMi = input("Tekrar hesaplamak icin T'ye basınız >>> ")
    if tekrarHesaplansinMi.upper() != 'T' :
        break;

print('Program sonlaniyor ...')

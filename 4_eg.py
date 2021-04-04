def ucretHesapla(a,b):
    try:
        hesaplananUcret = float(a)*float(b)
        return hesaplananUcret
    except:
        return -1;

calisilanSaat = input("Calisilan Saat nedir?")
saatlikUcret = input("Saatlik Ucret Nedir?")
sonuc = ucretHesapla(calisilanSaat,saatlikUcret);

if sonuc == -1:
    print("Hatalı girdi girdiniz.")
else:
    print("Hesaplanan Ucret: ", sonuc )

def ucret_hesapla(csaat,sucret):
    try:
        tucret=float(csaat) * float(sucret)
        return tucret
    except:
        return -1

csaat1 = input('Calisilan Saati Girin :')
sucret1 = input('Saatlik Ucreti Girin :')
sonuc = ucret_hesapla(csaat1, sucret1)
if sonuc == -1:
    print('HATALI GIRDI')
else :
    print(sonuc)
try:
    calisilan_saat = input('Calisilan Saat nedir?:')
    saatlik_ucret = input('Saatlik Ucret Nedir?:')
    ucret = float(calisilan_saat) * float(saatlik_ucret)
    print('Hesaplanan Ucret: ', ucret)
except:
    print('HATALI GIRDI')

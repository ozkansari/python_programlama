try:
    calisilan_saat = float(input ("çalışılan saati giriniz:"))
    saatlik_ucret = float(input ("saatlik ücreti giriniz:"))
except:
    print ("Hatalı giriş yaptınız.")
    quit()

ucret_hesapla = calisilan_saat * saatlik_ucret
print (ucret_hesapla)

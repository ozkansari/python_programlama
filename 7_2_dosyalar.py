try:
    dosyaAdi = input('Dosya adi giriniz:')
    dosya = open(dosyaAdi)
    print('Dosya icerigi: \n',  dosya.read())
except FileNotFoundError:
    print('dosya bulunamadi')

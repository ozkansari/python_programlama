import re

dosya = open('ogrenci_bilgileri.txt')

isimler = list()
epostalar = list()
yaslar = list()
sehirler = list()

for satir in dosya:
    isimler = isimler + re.findall('^(.+?):', satir)
    epostalar = epostalar + re.findall('\S+@\S+',satir)
    yaslar = yaslar + re.findall('\s([0-9]+)\s', satir)
    sehirler = sehirler + re.findall('\s(\S+)$',satir)

print(isimler)
print(epostalar)
print(yaslar)
print(sehirler)

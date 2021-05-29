ogrenciler = [ 'Ali' , 'Ahmet', 'Ayse', 'Fatma' ]

print("Dongu Yontem-1:")
for ogrenci in ogrenciler:
    print('Merhaba ', ogrenci)

print("Dongu Yontem-2:")
for i in range(len(ogrenciler)):
    print((i+1) , ' -) Merhaba ', ogrenciler[i])

print("Dongu Yontem-3:")
i = 0
while i < len(ogrenciler):
    print((i+1) , ' -) Merhaba ', ogrenciler[i])
    i+=1

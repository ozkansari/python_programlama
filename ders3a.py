try :
    x = int( input('tam sayi giriniz: ') )
    if x == 1 :
        print('1 girdiniz')
        print('Neden 1?')
    elif x == 2 :
        print('2 girdiniz')
        print('Neden 2?')
    elif x == 3 :
        print('34 girdiniz')
        print('Neden 3?')
    else:
        print('1,2,3 girmedin')
        print('Neden?')
    print('islem tamamlandi')
except:
    print('Bir hata olustu')
print('Program devam ediyor')
print('....')
y = input('Bir deger daha giriniz')

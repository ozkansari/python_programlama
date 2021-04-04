yasInput = input("Kac yasindasiniz?")
yas = int(yasInput)
try :
    yas = int(yasInput)
except:
    print("Lutfen sayi olarak yasinizi giriniz")
    quit()

if yas < 18:
    print("Henuz oy kullanacak yasta degilsiniz")
else:
    print("Oy kullanabilirsiniz")

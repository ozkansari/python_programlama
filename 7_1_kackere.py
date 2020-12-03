# Verilen string icerisinde, verilen baska bir stringin kac kere gecigini bulan bir fonksiyon
def kackere(girdi,aranan):
    sayac = 0
    indisBulunan = -1

    while True:
        indisBulunan = girdi.lower().find(aranan.lower(), indisBulunan+1)
        if indisBulunan == -1:
            break
        else:
            sayac = sayac + 1

    return sayac

sonuc = kackere('baNAna','an')
print(sonuc)

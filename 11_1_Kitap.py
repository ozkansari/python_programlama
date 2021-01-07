class Kitap:
    x = 0
    isim = ""
    def __init__(self, isim):
        self.isim = isim
        print('Kitap nesnesi olusturuluyor: ', self.isim)

    def okudum(self):
        self.x = self.x + 1
        print('isim:', self.isim, 'x:',self.x)

    def __del__(self):
        print('Nesne sonlandiriliyor.')

class Roman(Kitap):
    """Kitapdan miras alan Roman sinifi tanimi"""
    sayfa = 0
    def __init__(self, isim, sayfa):
        super(Roman, self).__init__(isim)
        self.sayfa = sayfa
    def sayfaSayisiniBas(self):
        print(self.sayfa)


kit1 = Kitap("Otostopcunun Galaksi Rehberi")
kit2 = Kitap("Sapiens")
kit1.okudum()
kit1.okudum()
kit2.okudum()
kit1.okudum()
kit2.okudum()
Kitap.okudum(kit1)
kit1 = 42

kit3 = Roman("Saatleri Ayarlama Enstitusu",120)
kit3.okudum()
kit3.sayfaSayisiniBas()

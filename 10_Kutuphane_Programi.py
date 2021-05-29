class Kitap:
    isim = ""
    okumaSayisi = 0

    def __init__(self,i):
        self.isim = i
        print(self.isim, ' kitap nesnesi olusturuldu')

    def okudum(self):
        self.okumaSayisi = self.okumaSayisi + 1;
        print(self.isim, ' kitabı okudum olarak isaretlendi. Toplam okunma: ', self.okumaSayisi)

    def okumaSayisiniGoster(self):
        print('Okuma sayisi', self.okumaSayisi)

    def __del__(self):
        print(self.isim, ' nesnesi sonlandi.')

class Roman(Kitap):
    """Kitaptan miras alan Roman sinifi tanimi"""
    sayfaSayisi = 0
    def __init__(self,isim,sayfaSayisi):
        super(Roman,self).__init__(isim)
        self.sayfaSayisi = sayfaSayisi

    def sayfaSayisiniGoster(self):
        print('Sayfa sayisi', self.sayfaSayisi)

    def okudum(self):
        self.okumaSayisi = self.okumaSayisi + 2;


kitap1 = Roman("Kurk Mantolu Madonna",256)
kitap1.okudum()
Roman.okudum(kitap1)
kitap1.okudum()
kitap1.sayfaSayisiniGoster()

kitap2 = Kitap('Otostopcunun Galaksi Rehberi')
kitap2.okudum()

kitap1.okudum()
kitap2.okudum()

kitap1.okumaSayisiniGoster()
kitap2.okumaSayisiniGoster()

kitap1 = None
kitap2 = None

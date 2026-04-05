class BankaHesabi:
    def __init__(self, isim, bakiye=0):
        self.isim = isim
        self.bakiye = bakiye
        self.hareket_gecmisi = []

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            self.hareket_gecmisi.append(f"Yatırılan: {miktar}")
        else:
            print("Hatalı miktar girdiniz.")

    def para_cek(self, miktar):
        if miktar > 0 and miktar <= self.bakiye:
            self.bakiye -= miktar
            self.hareket_gecmisi.append(f"Çekilen: {miktar}")
        elif miktar > self.bakiye:
            print("Yetersiz bakiye.")
        else:
            print("Negatif miktar çekilemez.")

    def ozet(self):
        print(f"Hesap Sahibi: {self.isim}")
        print(f"Güncel Bakiye: {self.bakiye}")
        print("İşlem Hareketleri:")
        for islem in self.hareket_gecmisi:
            print(islem)

hesap = BankaHesabi("Kadir", 500)
hesap.para_yatir(250)
hesap.para_cek(100)
hesap.ozet()

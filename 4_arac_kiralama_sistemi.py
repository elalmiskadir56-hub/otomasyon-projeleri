class Arac:
    def __init__(self, marka, gunluk_fiyat, musait_mi=True, *args):
        self.marka = marka
        self.gunluk_fiyat = gunluk_fiyat
        self.musait_mi = musait_mi
        self.ozellikler = args

class Musteri:
    def __init__(self, isim):
        self.isim = isim
        self.kiraladigi_araclar = []

    def arac_kirala(self, arac):
        if arac.musait_mi:
            arac.musait_mi = False
            self.kiraladigi_araclar.append(arac)
            print(f"{arac.marka} kiralandı.")
        else:
            print("Araç şu an müsait değil.")

    def arac_iade_et(self, arac):
        if arac in self.kiraladigi_araclar:
            arac.musait_mi = True
            self.kiraladigi_araclar.remove(arac)
            print(f"{arac.marka} iade edildi.")

# Test
a1 = Arac("Tesla", 2000, True, "Otonom Sürüş", "Elektrikli")
m1 = Musteri("Kadir")
m1.arac_kirala(a1)

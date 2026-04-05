class Kitap:
    def __init__(self, isim, yazar, durum="musait", **kwargs):
        self.isim = isim
        self.yazar = yazar
        self.durum = durum
        self.ozellikler = kwargs

class Kullanici:
    def __init__(self, isim):
        self.isim = isim
        self.aldigi_kitaplar = []

class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)

    def odunc_ver(self, kullanici, kitap_ismi):
        if len(kullanici.aldigi_kitaplar) >= 2:
            print("Maksimum kitap sınırına ulaşıldı.")
            return

        for kitap in self.kitaplar:
            if kitap.isim == kitap_ismi:
                if kitap.durum == "musait":
                    kitap.durum = "odunc verildi"
                    kullanici.aldigi_kitaplar.append(kitap)
                    print(f"{kitap_ismi} kitabı {kullanici.isim} kullanıcısına verildi.")
                    return
                else:
                    print("Kitap şu an müsait değil.")
                    return
        print("Kitap bulunamadı.")

    def iade_al(self, kullanici, kitap_ismi):
        for kitap in kullanici.aldigi_kitaplar:
            if kitap.isim == kitap_ismi:
                kitap.durum = "musait"
                kullanici.aldigi_kitaplar.remove(kitap)
                print(f"{kitap_ismi} iade alındı.")
                return

k1 = Kitap("Nutuk", "Mustafa Kemal Atatürk", tur="Tarih")
user1 = Kullanici("Kadir")
kutuphane = Kutuphane()
kutuphane.kitap_ekle(k1)
kutuphane.odunc_ver(user1, "Nutuk")

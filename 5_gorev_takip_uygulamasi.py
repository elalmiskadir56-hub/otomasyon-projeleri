class Gorev:
    def __init__(self, baslik, aciklama, tamamlandi_mi=False, **kwargs):
        self.baslik = baslik
        self.aciklama = aciklama
        self.tamamlandi_mi = tamamlandi_mi
        self.ek_bilgiler = kwargs

class Kullanici:
    def __init__(self, isim):
        self.isim = isim
        self.gorevler = []
        self.tamamlanan_gorevler = []

    def gorev_ekle(self, gorev):
        for g in self.gorevler:
            if g.baslik == gorev.baslik:
                print("Bu görev zaten mevcut.")
                return
        self.gorevler.append(gorev)
        print(f"'{gorev.baslik}' görevi eklendi.")

    def gorev_sil(self, baslik):
        for g in self.gorevler:
            if g.baslik == baslik:
                self.gorevler.remove(g)
                print(f"'{baslik}' görevi silindi.")
                return

    def gorev_tamamla(self, baslik):
        for g in self.gorevler:
            if g.baslik == baslik:
                g.tamamlandi_mi = True
                self.tamamlanan_gorevler.append(g)
                self.gorevler.remove(g)
                print(f"'{baslik}' görevi tamamlandı.")
                return


g1 = Gorev("Python Çalış", "OOP konusunu bitir", oncelik="Yuksek")
u1 = Kullanici("Kadir")
u1.gorev_ekle(g1)
u1.gorev_tamamla("Python Çalış")

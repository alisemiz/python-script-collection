class Kitap:
    def __init__(self, isim, yazar, yayin_yili):
        self.isim = isim
        self.yazar = yazar
        self.yayin_yili = yayin_yili
        self.odunc_alindi_mi = False

    def bilgi_goster(self):
        durum = "Ödünçte" if self.odunc_alindi_mi else "Rafta"
        return f"{self.isim} - {self.yazar} ({self.yayin_yili}) [{durum}]"

    def odunc_al(self):
        if not self.odunc_alindi_mi:
            self.odunc_alindi_mi = True
            return True
        return False

    def iade_et(self):
        if self.odunc_alindi_mi:
            self.odunc_alindi_mi = False
            return True
        return False


class Kullanici:
    def __init__(self, isim, uye_no):
        self.isim = isim
        self.uye_no = uye_no
        self.odunc_alinan_kitaplar = []

    def kitap_odunc_al(self, kitap):
        if kitap and kitap.odunc_al():
            self.odunc_alinan_kitaplar.append(kitap)
            print(f"{self.isim}, '{kitap.isim}' kitabını ödünç aldı.")
        else:
            print("Kitap bulunamadı veya zaten ödünçte.")

    def kitap_iade_et(self, kitap):
        if kitap and (kitap in self.odunc_alinan_kitaplar) and kitap.iade_et():
            self.odunc_alinan_kitaplar.remove(kitap)
            print(f"{self.isim}, '{kitap.isim}' kitabını iade etti.")
        else:
            print("Bu kitabı iade edemezsiniz!")


class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"'{kitap.isim}' kütüphaneye eklendi.")

    def kitaplari_listele(self):
        if not self.kitaplar:
            print("📭 Kütüphanede hiç kitap yok.")
        else:
            for kitap in self.kitaplar:
                print(kitap.bilgi_goster())

    def kitap_ara(self, isim):
        for kitap in self.kitaplar:
            if kitap.isim.lower() == isim.lower():
                return kitap
        return None


# ---------------- Menü ----------------
def menu():
    kutuphane = Kutuphane()
    kullanici = Kullanici("Ali", 101)

    while True:
        print("\n--- 📚 KÜTÜPHANE YÖNETİM SİSTEMİ ---")
        print("1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Ödünç Al")
        print("4. Kitap İade Et")
        print("5. Çıkış")

        secim = input("Seçiminizi yapınız: ")

        if secim == "1":
            isim = input("Kitap adı: ")
            yazar = input("Yazar: ")
            yil = input("Yayın yılı: ")
            yeni_kitap = Kitap(isim, yazar, yil)
            kutuphane.kitap_ekle(yeni_kitap)

        elif secim == "2":
            kutuphane.kitaplari_listele()

        elif secim == "3":
            isim = input("Ödünç almak istediğiniz kitap adı: ")
            kitap = kutuphane.kitap_ara(isim)
            kullanici.kitap_odunc_al(kitap)

        elif secim == "4":
            isim = input("İade etmek istediğiniz kitap adı: ")
            kitap = kutuphane.kitap_ara(isim)
            kullanici.kitap_iade_et(kitap)

        elif secim == "5":
            print("👋 Programdan çıkılıyor...")
            break

        else:
            print("⚠ Geçersiz seçim, tekrar deneyin.")


# Programı başlat
if __name__ == "__main__":
    menu()

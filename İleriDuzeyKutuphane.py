
import datetime
kitaplar={}
kullanicilar={}
odunc_kayitlari=[]

def kullanici_ekle():
    kullanici_adi=input("Lutfen kullanıcı adını giriniz:")
    if kullanici_adi in kullanicilar:
        print("Bu kullanici zaten kayitli")
        return
    sifre=input("Lutfen sifrenizi giriniz:")
    kullanicilar[kullanici_adi]={"sifre":sifre , "gecmis":[]}
    print("Kullanıcı basarıyla eklendi.")


def kullanici_sil():
    kullanici_adi=input("Lutfen silinecek kullanıcı adını giriniz:")
    if kullanici_adi in kullanicilar:
        del kullanicilar[kullanici_adi]
        print("Kullanıcı silindi.")
    else:
        print("Boyle bir kullanıcı yok.")

def kullanici_giris():
    kullanici_adi=input("Lutfen kullanici adini giriniz:")
    sifre=input("Lutfen sifrenizi giriniz:")
    if kullanici_adi in kullanicilar and kullanicilar[kullanici_adi]["sifre"]==sifre:
        print(f"Hoşgeldin {kullanici_adi}")
        return kullanici_adi
    else:
        print("Hatali giriş")
        return None
    


def kitap_ekle():
    kitap_Id=input("Lutfen kitabın ID numarasını giriniz:")
    if kitap_Id in kitaplar:
        print("Bu kitap zaten mevcut.")
        return
    
    isim=input("Kitap ismi:")
    yazar=input("Kitap yazarı:")
    stok=input("Stok sayısı:")
    kitaplar[kitap_Id]={"isim":isim , "yazar":yazar , "stok":stok}
    print("Kitap basariyla eklendi.")

def kitap_sil():
    kitap_Id=input("Silinecek kitabın ID numarası:")
    if kitap_Id in kitaplar:
        del kitaplar[kitap_Id]
        print("Kitap basarıyla silindi.")
    else:
        print("Boyle bir kitap yok.")

def kitaplari_listele():

    if not kitaplar:
        print("Listelenecek kitap yok.")
    
    for kid, info in kitaplar.items():
        print(f"[{kid}] {info['isim']} - {info['yazar']} | Stok: {info['stok']}")


def kitap_odunc_al(kullanici):
    kitap_Id=input("Odunc alınacak kitabın ID numarası:")
    if kitap_Id not in kitaplar or kitaplar[kitap_Id]["stok"]<=0:
        print("Kitap mevcut değil veya stokta yok.")
        return
    kitaplar[kitap_Id]["stok"]-=1
    odunc_tarihi=datetime.date.today()
    odunc_kayitlari.append((kullanici,kitap_Id,odunc_tarihi,None))
    print(f"{kitaplar[kitap_Id]["isim"]} ödünç alındı.")


def kitap_iade_et(kullanici):

    kitap_id = input("İade edilecek kitap ID: ")
    for i, kayit in enumerate(odunc_kayitlari):
        if kayit[0] == kullanici and kayit[1] == kitap_id and kayit[3] is None:
            iade_tarihi = datetime.date.today()
            odunc_kayitlari[i] = (kayit[0], kayit[1], kayit[2], iade_tarihi)
            kitaplar[kitap_id]["stok"] += 1

            # Ceza hesapla
            gecen_gun = (iade_tarihi - kayit[2]).days
            if gecen_gun > 15:
                ceza = (gecen_gun - 15) * 2  # günlük 2 TL ceza
                print(f"Kitap geç iade edildi! Ceza: {ceza} TL")
            else:
                print("Kitap zamanında iade edildi. Teşekkürler!")
            return
    print("Bu kullanıcıya ait böyle bir ödünç kaydı yok!")

def menu():

    aktif_kullanici = None
    while True:
        print("\n--- Kütüphane Yönetim Sistemi ---")
        print("1. Kullanıcı Ekle")
        print("2. Kullanıcı Sil")
        print("3. Kullanıcı Giriş")
        print("4. Kitap Ekle")
        print("5. Kitap Sil")
        print("6. Kitapları Listele")
        print("7. Kitap Ödünç Al")
        print("8. Kitap İade Et")
        print("0. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            kullanici_ekle()
        elif secim == "2":
            kullanici_sil()
        elif secim == "3":
            aktif_kullanici = kullanici_giris()
        elif secim == "4":
            kitap_ekle()
        elif secim == "5":
            kitap_sil()
        elif secim == "6":
            kitaplari_listele()
        elif secim == "7":
            if aktif_kullanici:
                kitap_odunc_al(aktif_kullanici)
            else:
                print("Lütfen önce giriş yapın!")
        elif secim == "8":
            if aktif_kullanici:
                kitap_iade_et(aktif_kullanici)
            else:
                print("Lütfen önce giriş yapın!")
        elif secim == "0":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim!")
menu()

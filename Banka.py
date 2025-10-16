kullanicilar={}

def kullanici_ekle():
    
    kullanici_adi=input("Lutfen kullanici adini giriniz:")
    if kullanici_adi in kullanicilar:
        print("Bu kullanici zaten var.")
    else:
        sifre=input("Sifre:")
        kullanicilar[kullanici_adi]={"Sifre":sifre , "bakiye":0}
        print("Hesap olusturuldu.")

def giris_yap():
    kullanici_adi=input("Lutfen kullanici adini giriniz:")
    sifre=input("Sifre:")

    if kullanici_adi in kullanicilar and kullanicilar[kullanici_adi]["Sifre"]==sifre:
        print(f"Hosgeldin {kullanici_adi}")
        banka_menusu(kullanici_adi)

    
    else:
        print("Hatali giris")

def banka_menusu(kullanici_adi):
    
    while True:
        print("\n1. Bakiye Görüntüle\n2. Para Yatır\n3. Para Çek\n4. Çıkış")
        secim = input("Seçiminiz: ")
        
        if secim == "1":
            print("💰 Bakiyeniz:", kullanicilar[kullanici_adi]["bakiye"])
        
        elif secim == "2":
            miktar = float(input("Yatırılacak miktar: "))
            kullanicilar[kullanici_adi]["bakiye"] += miktar
            print("✅ Para yatırıldı.")
        
        elif secim == "3":
            miktar = float(input("Çekilecek miktar: "))
            if miktar <= kullanicilar[kullanici_adi]["bakiye"]:
                kullanicilar[kullanici_adi]["bakiye"] -= miktar
                print("✅ Para çekildi.")
            else:
                print("❌ Yetersiz bakiye.")
        
        elif secim == "4":
            print("👋 Çıkış yapıldı.")
            break
        
        else:
            print("⚠️ Geçersiz seçim.")



          

while True:

    print("\n ------Mini Banka Uygulamasi--------")
    print("1-Yeni Kullanici Kaydi\n 2-Giris Yap\n3-Çikis")
    secim=int(input("Seciminiz:"))

    if secim==1:
        kullanici_ekle()
    elif secim==2:
        giris_yap()
    elif secim==3:
        print("Gule gule")
        break
    else:
        print("Lutfen gecerli bir secim yapin.")

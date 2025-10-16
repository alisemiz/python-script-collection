from datetime import datetime
dersler=[]
en_yuksek_dusuk_hesap=[]


def sinav_kaydi():
 
    while True:
        ders_adi = input("Lütfen eklemek istediğiniz dersin adını yazınız: ")

        # Tarihi doğru girene kadar sor
        while True:
            girdi = input("Tarihi şu formatta giriniz (YYYY-MM-DD): ")
            try:
                ders_tarih = datetime.strptime(girdi, "%Y-%m-%d").date()
                break  # tarih doğruysa döngüden çık
            except ValueError:
                print("❌ Tarih formatı hatalı! Lütfen YYYY-AA-GG formatında tekrar giriniz.")

        # Not girişinde hata varsa başa sarmasın, sadece notu tekrar istesin
        while True:
            try:
                dersin_notu = int(input("Lütfen dersin notunu giriniz: "))
                break
            except ValueError:
                print("❌ Not bir sayı olmalıdır! Lütfen tekrar deneyin.")

        dersler.append((ders_adi, ders_tarih, dersin_notu))
        print("\n✅ Ders başarıyla eklendi.")

        devam = input("\nDevam etmek istiyorsanız 'e' tuşlayın (ya da herhangi bir tuş çıkmak için): ")
        if devam.lower() != 'e':
            break

def listele():

    if dersler:
     for ders in dersler:
        print(f"Dersin adi:{ders[0]}  Dersin Tarihi:{ders[1]} Dersin Notu:{ders[2]}")
    else:
        print("Görüntülenecek ders bulunmamakta.")
def ortalama_hesapla():
    ders_sayisi=0
    toplam=0
    for ders in dersler:
        print("Ders ",ders[0], "not degeri: ", ders[2])
        toplam=toplam+ders[2]
        ders_sayisi+=1

    print("Ortalama deger: ", toplam/ders_sayisi)
def Max_min_hesabi():
    for ders in dersler:
        en_yuksek_dusuk_hesap.append(ders[2])

    
    print("En yuksek not:", max(en_yuksek_dusuk_hesap))
    print("En düsük not:",min(en_yuksek_dusuk_hesap) )





while True:
    print("1-Yeni sinav kaydi.\n2-Tüm sinavlari listele.\n3-Belirli dersin ortalamasini hesapla.\n4-En yüksek ve en düşük notlari  göster.\n5-çikis.\n")
    
    try:
        secim=int(input("Lutfen bir secim yapiniz:"))
        if secim==1:
            sinav_kaydi()
        elif secim ==2:
            listele()
        elif secim==3:
            ortalama_hesapla()
        elif secim==4:
            Max_min_hesabi()
        elif secim==5:
            print("Çikis yapildi.")
            break
            
        else:
            print("Lutfen (1-7) arasinda sayi girin.")

    except ValueError:
        print("Sadece rakamlari kullanarak işlem yapin.")


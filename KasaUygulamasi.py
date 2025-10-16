urunler={}
borclar={}
gelir=0
gider=0




def yeniUrunEkle():
   global urunler
   yeniUrun=input("lUtfen eklemek istediğiniz ürünün adini giriniz:").capitalize()
   if yeniUrun in urunler:
      print("Bu ürün zaten mevcut.")
      return
   else:
      try:
       fiyat=float(input("Lutfen ürünün fiyatini giriniz:"))
       stok=int(input("Lutfen adedini giriniz:"))
       urunler[yeniUrun]={"fiyat":fiyat , "stok":stok}
       print(f"{yeniUrun} basarıyla eklendi.")

      except ValueError:
         print("Lutfen sayisal deger giriniz.")
def UrunSil():
   global urunler
   silinecekUrun=input("Lutfen silmek istediğiniz ürünün adini giriniz:").capitalize()
   if silinecekUrun in urunler:
      del urunler[silinecekUrun]
      print(f"{silinecekUrun} başarıyla silindi.")
   else:
      print("Silinecek ürün yok.")


def stokAdediGir():
    global urunler
    urun_adi = input("Stok eklemek istediğiniz ürünün adını giriniz: ").capitalize()
    if urun_adi in urunler:
        try:
            adet = int(input("Eklenecek stok adedini giriniz: "))
            urunler[urun_adi]["stok"] += adet
            print(f"{urun_adi} ürününe {adet} adet eklendi. Güncel stok: {urunler[urun_adi]['stok']}")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz!")
    else:
        print("Bu ürün mevcut değil!")


def satisYap():
   
   global urunler, gelir
   urun_adi = input("Satılacak ürünün adını giriniz: ").capitalize()
   if urun_adi in urunler:
        try:
            adet = int(input("Satılacak adet sayısını giriniz: "))
            if adet <= urunler[urun_adi]["stok"]:
                toplam_fiyat = urunler[urun_adi]["fiyat"] * adet
                gelir += toplam_fiyat
                urunler[urun_adi]["stok"] -= adet
                print(f"{adet} adet {urun_adi} satıldı. Toplam kazanç: {toplam_fiyat} TL")
            else:
                print("Yeterli stok yok!")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz!")
   else:
        print("Bu ürün bulunamadı!")
def borcEkle():
    global borclar, gider
    musteri = input("Müşteri adını giriniz: ").capitalize()
    try:
        miktar = float(input("Borç miktarını giriniz: "))
        borclar[musteri] = borclar.get(musteri, 0) + miktar
        gider += miktar
        print(f"{musteri} adlı müşteriye {miktar} TL borç eklendi.")
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")

def borcSil():
   
    global borclar
    musteri = input("Borcu silinecek müşteri adını giriniz: ").capitalize()
    if musteri in borclar:
        del borclar[musteri]
        print(f"{musteri} adlı müşterinin borcu silindi!")
    else:
        print("Bu müşteri listede yok!")
def Total():
    global gelir, gider
    kar_zarar = gelir - gider
    print("\n------ KAR/ZARAR DURUMU ------")
    print(f"Toplam Gelir: {gelir} TL")
    print(f"Toplam Gider: {gider} TL")
    if kar_zarar >= 0:
        print(f"Net Kar: {kar_zarar} TL ✅")
    else:
        print(f"Net Zarar: {abs(kar_zarar)} TL ❌")
def urunListele():
    print("\n------ ÜRÜNLER ------")
    if urunler:
        for urun, bilgiler in urunler.items():
            print(f"{urun} | Fiyat: {bilgiler['fiyat']} TL | Stok: {bilgiler['stok']}")
    else:
        print("Hiç ürün bulunmamaktadır!")

def borcListele():
    print("\n------ BORÇLULAR ------")
    if borclar:
        for musteri, miktar in borclar.items():
            print(f"{musteri}: {miktar} TL")
    else:
        print("Hiç borçlu bulunmamaktadır!")
   

while True:

    print("1-Ürün Ekle\n2-Ürün Sil\n3-Stok Adedi Gir\n4-Satis Yap\n5-Borç Ekle\n6-Borç Sil\n7-Güncel kar zarar durumu\n8-Elimizdeki Ürünleri Listele\n9-Borçluları Listele\n10-Cikis")
   
    try:
     
     secim=int(input("Lutfen 1 ile 9 arasinda bir sayi giriniz:"))

     if secim ==1:
        yeniUrunEkle()
     elif secim ==2:
        UrunSil()
     elif secim ==3:
        stokAdediGir()

     elif secim ==4:
        satisYap()
     elif secim ==5:
        borcEkle()
     elif secim ==6:
        borcSil()
     elif secim ==7:
        Total()
    
     elif secim==8:
        urunListele()
     elif secim == 9:
        borcListele()
     elif secim==10:
        print("Basarili bir sekilde cikis yapildi.")
        break

     else:
        print("Lutfen 1 ile 8 arasinda bir sayi giriniz.")
    
    
    except ValueError:
       print("Lutfen bir sayi giriniz . Sayi dışında bir sey girmeyiniz.")


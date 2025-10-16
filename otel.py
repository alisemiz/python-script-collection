# Toplam 40 oda var. Boş olan odalar listede tutuluyor.
tum_odalar = {i: None for i in range(1, 41)}  
# Oda fiyatı
oda_ucreti = 500  
# Toplam gelir
gelir = 0  

def oda_goruntule():
    print("\n---ODA DURUMLARI---")
    for oda_no, musteri in tum_odalar.items():
        if musteri is None:
            print(f"Oda {oda_no}: Boş")
        else:
            print(f"Oda {oda_no}: Dolu ({musteri})")

def kirala():
    global gelir
    try:
        oda_no = int(input("Kiralamak istediginiz oda numarasini giriniz (1-40): "))
        if oda_no < 1 or oda_no > 40:
            print("Lutfen gecerli bir oda numarasi giriniz.")
            return
        if tum_odalar[oda_no] is None:
            musteri = input("Musteri adini giriniz: ")
            tum_odalar[oda_no] = musteri
            gelir += oda_ucreti
            print(f"Oda {oda_no}, {musteri} icin kiralandi. Ücret: {oda_ucreti} TL")
        else:
            print("Bu oda zaten dolu!")
    except ValueError:
        print("Lutfen sayi giriniz.")

def teslim():
    try:
        oda_no = int(input("Teslim etmek istediginiz oda numarasini giriniz (1-40): "))
        if oda_no < 1 or oda_no > 40:
            print("Lutfen gecerli bir oda numarasi giriniz.")
            return
        if tum_odalar[oda_no] is not None:
            print(f"Oda {oda_no}, {tum_odalar[oda_no]} tarafindan teslim edildi.")
            tum_odalar[oda_no] = None
        else:
            print("Bu oda zaten boş!")
    except ValueError:
        print("Lutfen sayi giriniz.")

def total():
    print(f"Toplam gelir: {gelir} TL")

def menu():
    while True:
        print("\n----OTELİMİZE HOSGELDİNİZ-------")
        print("1 - Odalari görüntüle")
        print("2 - Oda kirala")
        print("3 - Oda teslimi yap")
        print("4 - Total gelir")
        print("5 - Cikis")

        try:
            secim = int(input("Bir secim yapiniz: "))
            if secim == 1:
                oda_goruntule()
            elif secim == 2:
                kirala()
            elif secim == 3:
                
                teslim()
            elif secim == 4:
                total()
            elif secim == 5:
                print("Başarılı bir sekilde cikis yapildi.")
                break
            else:
                print("Lütfen geçerli bir seçim yapiniz.")
        except ValueError:
            print("Lütfen bir rakam giriniz.")

# Programı başlat
menu()

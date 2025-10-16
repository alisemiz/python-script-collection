print("-----Sinema Otomasyonuna Hosgeldiniz--------")
koltuklar={i: None for i in range(1,31)}

def koltuklari_Goster():

    for k,v in koltuklar.items():
        if v!=None :
            print(f"{k} nolu koltuk dolu.")
        else:
            print(f"{k} nolu koltuk boş")

def Rezervasyon_yap():
 while True:
    koltuklari_Goster()

    try:
     koltuk_secimi=int(input("Lutfen bir koltuk secin:"))
     if koltuklar[koltuk_secimi]==None:
         print("Tebrikler boş koltuğu seçtiniz.")
         ad=input("Lutfen adinizi giriniz:")
         koltuklar[koltuk_secimi]=ad
         break
    
     else:
         print("Maaelesf seçtiğiniz koltuk dolu.")


    except ValueError:
        print("Lutfen yalnızca sayi kullanın.")

def rezervasyon_iptal():

    ad=input("Lutfen rezervasyon yaptığınız ismi giriniz:")
    bulunduMu=False
    for k,v in koltuklar.items():
        if v==ad:
            bulunduMu=True
            koltuklar[k]=None
    
    if bulunduMu:
        print("Rezervasyonunuz basarili bir sekilde iptal edildi.")
    else:
        print(f"{ad} isimli bir rezervasyon bulunamadi.")




while True:
    print("1-Koltukları Göster\n2-Rezervaasyon Yap\n3-Rezervasyon İptal\n4-Cıkış")

    try:
        secim=int(input("Lutfen seciminizi yapiniz:"))
        if secim==1:
            koltuklari_Goster()
        elif secim==2:
            Rezervasyon_yap()
        elif secim==3:
            rezervasyon_iptal()
        elif secim==4:
            print("Basarili bir sekilde çıkış yapildi.")
            break
        else:
            print("Lutfen 1 ve 4 arasında bir sayi giriniz:")

    except ValueError:
        print("Lutfen seciminiz bir rakam olsun.")

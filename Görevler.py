gorevler=[]

def Gorev_ekle():
    gorev=input("Eklemek istediginiz gorevi girin:")
    gorevDurumu=False
    gorevler.append([gorev,gorevDurumu])

def Gorev_sil():
    silinecek_gorev=input("Lutfen silmek istediğiniz görevi girin:")
    bulunduMu=False

    for gorev in gorevler:
        if gorev[0].lower()==silinecek_gorev.lower():
            gorevler.remove(gorev)
            print(gorev[0],"silindi")
            bulunduMu=True
        
    if not bulunduMu:
        print("Silinecek gorev bulunamadi.")


def Gorev_Tamamla():
    tamamlanacak_gorev=input("Lutfen tamamlamak istediginiz gorevi yazin:")
    bulunduMu=False

    for gorev in gorevler:
        if gorev[0].lower()==tamamlanacak_gorev.lower():
            gorev[1]=True
            bulunduMu=True
            print("Gorev tamamlandi")
    
    if not bulunduMu:
        print("Gorev bulunamadi.")


def Listele():
    bulunduMu=False
    for gorev in gorevler:
        print(gorev[0] , " ==", gorev[1])
        bulunduMu=True
    
    if not bulunduMu:
        print("Listelenecek görev bulunamadi.")


while True:
    secim=int(input("1-Gorev Ekle.\n2-Gorev Sil\n3-Gorevi Tamamla\n4-Gorevleri Listele\n5-Cikis\nLutfen secim yapiniz:"))


    if secim==1:
        Gorev_ekle()

    elif secim==2:
        Gorev_sil()
    elif secim==3:
        Gorev_Tamamla()
    elif  secim==4:
        Listele()
    elif secim==5:

        print("Cikis yapildi.")
        break

    else:
        print("Yanlis tus tusladiniz.")


        


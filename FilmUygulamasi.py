film_Arsivi=[]


def film_Ekle():
    film_ad=input("Filmin adini giriniz:")
    film_puan=input("Filme 1-10 arasinda bir puan veriniz:")
    film_Arsivi.append([film_ad,film_puan])
    print("Film eklendi.\n")


def film_Listele():
    if not film_Arsivi:
        print("Film arsivi bos.")
    else:
        print("-----FİLM LİSTESİ----------")
        for film in film_Arsivi:
            print("Film :"+film[0] + "\n" + "Puan: "+ film[1])



def film_puani_guncelle():

    isim=input("Puani guncellenecek filmin adini giriniz:")
    for film in film_Arsivi:
        if film[0].lower()==isim.lower():
            yeni_puan=input("Yeni puani giriniz:")
            film[1]=yeni_puan
            print("Puan guncellendi.")
        else:
            print("Film bulunamadi.")


def film_Sil():
    isim=input("Silinecek olan filmin ismini giriniz:")

    for film in film_Arsivi:
        if film[0].lower()==isim.lower():
            film_Arsivi.remove(film)
            print("Film silindi.")
        else:
            print("Film bulunamadi.")


def Film_Sirala():

    sirali=sorted(film_Arsivi,key=lambda x:x[1] , reverse=True)

    for film in sirali:
        print("Film: ",film[0]," Puan : ",film[1])









while True:

    print("1) Film Ekle\n 2)Film Listele \n3)Film Puani Guncelle\n4)Film Sil\n 5)Puanlara Gore Sirala\n")
    secim=int(input("Lutfen secim yapiniz:"))

    if secim==1:
        film_Ekle()
    elif secim==2:
        film_Listele()
    elif secim==3:
        film_puani_guncelle()
    elif secim==4:
        film_Sil()
    elif secim==5:
        Film_Sirala()
    elif secim==6:
        print("Cikis yapiliyor...")
        break

    
    else :
        print("Gecersiz secim.")



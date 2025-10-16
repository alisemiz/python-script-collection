ilaclar=[]

def ekle():
    ilac_ad=input("İlacin adini giriniz:")
    ilac_stok=int(input("İlac stogunu giriniz:"))
    ilaclar.append([ilac_ad,ilac_stok])
      

def sil():
    silinecek_ilac=input("Lutfen silinecek ilac adini giriniz:")
    bulundu_Mu=False


    for ilac in ilaclar:
        if ilac[0].lower()==silinecek_ilac.lower():
            ilaclar.remove(ilac)
            bulundu_Mu=True
            print("İlac silindi.")
            break
        
    if  not bulundu_Mu:
        print("Silinecek ilac bulunamadi.")


def listele():

    if not ilaclar:
        print("Listelenecek ilac bulunamadı.")
    

    else:

          for ilac in ilaclar:
           print("İlac adi: ", ilac[0], "    ilac stogu:",ilac[1])
    
          else:
                    print("EKrana depodaki tüm ilaclar stok adetleriyle beraber yazildi.")

   




def ara():
    ara_ilac_adi=input("Aranacak olan ilac adini giriniz:")
    bulundu_Mu=False

    for ilac in ilaclar:
        if ilac[0].lower()==ara_ilac_adi.lower():
            print("Aradiginiz ilac :", ilac[0], "bulundu")
            bulundu_Mu=True

            break

    if  not bulundu_Mu:
        print("Aradiginiz urun bulunamadi.")




while True:
    
    print("1-ilac listele\n2-ilac ekle\n3-ilac sil\n4-ilac ara\n5-Cikis\n")
    secim=int(input("Lutfen secim yapiniz:"))

    if secim==1:
        print("-------LİSTE---------")
        listele()

    elif secim==2:
        ekle()
        print("Basariyla eklendi.")
    
    elif secim==3:
        sil()
        

    elif secim==4:
        ara()
    
    elif secim==5:
        print("Basariyla cikis yapildi.")
        break
    
    else:
        print("Lutfen dogru bir tus tuslayınız.")



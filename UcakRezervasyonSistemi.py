print("--------Ucak Rezervasyon Sistemine Hosgeldiniz.---------")

koltuklar={1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None,10:None}

def ucusBilgileriniGoster():

 for k,v in koltuklar.items():
  if v !=None:
   print(f"{v} isimli yolcu {k} nolu koltuğa yerleşti.")
  else:
   print(f"{k} nolu koltuk boş")


def BosKoltuklariGoster():
 bos_koltuklar=[]
 for k,v in koltuklar.items():
  if v is None:
   bos_koltuklar.append(k)
  

 print("Bos Koltuklar:",bos_koltuklar)

   

def rezervasyonYap():
 
 bos_koltuklar=[]

 for k,v in koltuklar.items():
  if v is None:
   bos_koltuklar.append(k)


 print("Bos Koltuklar:",bos_koltuklar)
 while True:  
   try:
       koltuk_Numarasi=int(input("Lutfen boş koltuklardan birisini secin:"))
       if koltuk_Numarasi  not in koltuklar:
        print("Lutfen gecerli, bir koltuk numarasi giriniz.")
        continue
 
       if koltuklar[koltuk_Numarasi] is not None:
        print("Bu koltuk dolu. Ne yazik ki.")
        continue
 
       isim=input("Lutfen isminizi giriniz:").strip()

       if not isim:
        print("isim alani bos olamaz. Lutfen Tekrar deneyin.")
        continue
 
       koltuklar[koltuk_Numarasi]=isim
       print(f"{isim} adli kişiye {koltuk_Numarasi} nolu koltuk tahsis edildi.")
       break


 
   except ValueError:
    print("Lutfen koltuk numarasi degerini sayi girin.")
 
 

 
def  rezervasyonİptal():
 
 isim=input("Rezervasyon yaptiğiniz isminizi giriniz:")
 bulunduMu=False
 for k,v in koltuklar.items():
  if v ==isim:
   koltuklar[k]=None
   bulunduMu=True


 if bulunduMu:
  
  print("Yaptiğiniz rezervasyon basarili bir şekilde silindi.")
 else:
  print(f"{isim} adında bir rezervasyon bulunamadi.")





while  True:

 print("1-Ucus Bilgilerini Goster\n2-Bos Koltuklari Goster \n3-Rezervasyon Yap\n4-Rezervasyon İptal\n5-Cikis")
 

 try:
  secim=int(input("Secim yapiniz:"))
  if secim==1:
   ucusBilgileriniGoster()
  elif secim==2:
   BosKoltuklariGoster()
  elif secim==3:
   rezervasyonYap()
  elif secim==4:
   rezervasyonİptal()
  elif secim==5:
   print("Cikis Yapildi.")
   break
  else:
   print("Lutfen dogru secim numaralarini giriniz.")

   
  
 except ValueError:
  print("Lutfen secim degerini sayi olarak girin.")

  

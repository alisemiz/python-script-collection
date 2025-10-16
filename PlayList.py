import random
sarki_listesi=[]


def sarki_ekle():
      devam_Mi=False
      eklenecek_sarki=input("Lutfen bir sarki giriniz:")
      

      if  eklenecek_sarki in sarki_listesi:
                  print("Bu sarki zaten listede var :(")
      else:
                  sarki_listesi.append(eklenecek_sarki)
                  print("Sarki basarili bir sekilde eklendi:)")
                  for sarki in sarki_listesi:
                        print(sarki)


      while True:
       devam_tusu=int(input("Devam etmek istiyorsaniz 1 e değilse 2 ye basiniz:"))
       if devam_tusu ==1:
             eklenecek_sarki=input("Lutfen bir sarki giriniz:")
             if  eklenecek_sarki in sarki_listesi:
                  print("Bu sarki zaten listede var :(")
             else:
                  sarki_listesi.append(eklenecek_sarki)
                  print("Sarki basarili bir sekilde eklendi:)")
                  for sarki in sarki_listesi:
                        print(sarki)
      
       elif devam_tusu==2:
            
             break
             
       else :
              print("Lutfen 1 yada 2 yi tuslayiniz.")
def sarki_sil():
            silinecek_sarki=input("Silinecek olan sarkiyi giriniz:")

            if silinecek_sarki  in sarki_listesi:
            
                  sarki_listesi.remove(silinecek_sarki)
                  print("Sarki basarili bir sekilde silindi.\n\n")

                  print("Guncel liste:\n")
                  for sarki in sarki_listesi:
                        print(sarki)


            else:
                  print("Silinecek sarki listede yok.")
def listeyi_goruntule():
       for sarki in sarki_listesi:
        print(sarki)
def listeyi_karistir():

   random.shuffle(sarki_listesi)
   print("Sarki listesi karistirildi.")
def siradaki_sarkiyi_cal():
 
 if sarki_listesi:
       print(f"Şu anda çalan sarki {sarki_listesi[0]}")


 else:
       print("Liste bos.")
def sarkiyi_tasi():
      
 listeyi_goruntule()
      
      
 try:
            
       eski=int(input("Lutfen sarkinin konumunu giriniz:"))-1
       yeni=int(input("Sarkinin yeni yani olmasi gereken yeri yaziniz:"))-1
       if 0<=eski<len(sarki_listesi) and 0<=yeni<len(sarki_listesi):
             sarki=sarki_listesi.pop(eski)
             sarki_listesi.insert(yeni,sarki)
             print("Sarki tasindi.")
       else :
             print("Gecersiz index.")
             
             
 except ValueError:
      print("Lutfen gecerli sayilar girin.")

      

      
       
       
      
while True:
        
         print("1-Şarki Ekle\n2-Şarki Sil\n3-Listeyi Görüntüle\n4-Listeyi Karistir\n5-Siradaki Sarkiyi Cal\n6-Şarkiyi Bir Yere Tasi\n7-Cikis\n")
         secim=int(input("Lutfen bir secim yapiniz:"))


         if secim  in [1,2,3,4,5,6,7]:
                  if secim==1:
                          sarki_ekle()
                  elif secim==2:
                          sarki_sil()
                  elif secim==3:
                          listeyi_goruntule()
                  elif secim==4:
                          listeyi_karistir()
                  elif secim==5:
                          siradaki_sarkiyi_cal()
                  elif secim==6:
                          sarkiyi_tasi()
                  elif secim==7:
                          print("Cikis yapiliyor.")
                          break

                 
         else:
                   print("Lutfen gecerli bir sayi giriniz:(1-7)")
         
                
        
      


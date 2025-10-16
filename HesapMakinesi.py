import math
print("---------HESAP MAKİNESİ UYGULAMASİNA HOŞ GELDİNİZ -----------")




def toplama():
    while True:  # sayi1 döngüsü
        sayi1 = input("Lütfen ilk sayıyı giriniz: ")
        if sayi1.isdigit():
            sayi1 = int(sayi1)
            break
        else:
            print("Sayi 1 sayı değil. Lütfen sayı giriniz.")

    while True:  # sayi2 döngüsü
        sayi2 = input("Lütfen ikinci sayıyı giriniz: ")
        if sayi2.isdigit():
            sayi2 = int(sayi2)
            break
        else:
            print("Sayi 2 sayı değil. Lütfen sayı giriniz.")

    print("Her iki girişiniz de sayı olduğu için devam ediyoruz.")
    toplam = sayi1 + sayi2
    print("Toplam değer:", toplam)

def cikarma():

 while True:
   #1.sayi
   sayi1=input("1.sayiyi giriniz:")
   if sayi1.isdigit():
     sayi1=int(sayi1)
     break
   else:
     print("Lutfen sayi giriniz.")

 while True:
   sayi2=input("Lutfen 2. sayiyi giriniz:")
   if sayi2.isdigit():
     sayi2=int(sayi2)
     break
   else:
     print("Lutfen sayi giriniz.")
  
 cikarma=sayi1-sayi2
 print("Cikarma:",cikarma)
def carpma():
  
  while True:
    sayi1=input("1.sayiyi giriniz:")
    if sayi1.isdigit():
      sayi1=int(sayi1)
      break
    else:
      print("1.sayiyi sayi girin.")
    
  while True:
    sayi2=input("2.sayiyi giriniz:")
    if sayi2.isdigit():
      sayi2=int(sayi2)
      break
    else:
      print("Lutfen sayi giriniz.")

  carpma=sayi1*sayi2
  print("Carpma:",carpma)
  

def bolme():
  while True:
    sayi1 = input("1. sayıyı giriniz: ")
    if sayi1.lstrip('-').isdigit():  # negatif sayılara izin verir
        sayi1 = int(sayi1)
        break
    else:
        print("Lütfen 1. sayıyı sayı olarak girin.")

  while True:
    sayi2 = input("2. sayıyı giriniz: ")
    if sayi2.lstrip('-').isdigit():
        sayi2 = int(sayi2)
        if sayi2 != 0:
            break
        else:
            print("Lütfen ikinci sayı sıfır (0) olmamalı.")
    else:
        print("Lütfen 2. sayıyı sayı olarak giriniz.")

  bolme = sayi1 / sayi2
  print("Bölme:", bolme)

def ortalama():
  
  print("Lutfen sayi adedini giriniz:")
  adet=int (input("Aded:"))
  
  toplama=0

  while adet>0:
    
    sayi=int(input("Sayi giriniz:"))

    
    toplama=toplama+sayi
    adet-=1

  adet+=1

  print("Ortalama:",toplama/adet)




    





while True:

 print("1-Toplama \n2-Cikarma İslemi \n3-Carpma İşlemi \n4-Bolme İşlemi\n5-Ortalama hesabi\n6-Çikis")
 
 secim=int(input("Lutfen seçim yapiniz:"))


 if secim in [1,2,3,4,5,6]:
  
  if secim==1:
   toplama()
  elif secim==2:
   cikarma()
  elif secim==3:
   carpma()
  elif secim==4:
   bolme()  
  elif secim==5:
   ortalama()
  elif secim==6:
   print("Cikis yapiliyor.")
   break
  
 else:
  print("Lutfen doğru rakami kodlayiniz.")

 

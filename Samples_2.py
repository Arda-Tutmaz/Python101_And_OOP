#sayi cift mi değil mi

# def CiftMi(sayi):
#     if sayi%2==0:
#         print("Sayiniz Cift")
#     else:
#         print("Sayiniz Tektir")


# sayiniz=input("Sayinizi Giriniz: ")
# CiftMi(int(sayiniz))


#**************************************** kaç kere yazdırmak istediğinizi soran program


# def yazdir(metin,kacKere):
#  for i in range (1, (kacKere+1)):
#  print (metin, end='\n')


# yazdir('Merhaba', 5)

#*************************************** faktoriyel alma programı


# def faktoriyelAl(sayi):
#  sonuc=1
#  if (sayi==0 or sayi==1):
#  sonuc=1
#  elif sayi>1:
#  for i in range(1, sayi+1, 1):
#  sonuc*=i
#  else: sonuc=-1 #hatalı bir işlem olduğunu anlamak için -1 değerini veriyoruz
#  return sonuc


#***************************************


# for i in range (1,3):
#  print ('i değişkenin değeri=', i)
# print ('i değişkenin son değeri=', i) #3 dahil değil.

#--- yaşınızın 1 artırılması

# yas=34 # global bir değişken
# dogumGunuMu=True
# if dogumGunuMu==True:
#  yas+=1 #yerelde aynı değişken 1 artırılmıştır.
#  print ('Nice yıllara! Yaş:', yas)

#--- liste elemanlarının toplamını bulan program

# def toplamBul (sayiListesi=[0]):
#     topla=0
#     for i in range (len(sayiListesi)):
#         topla+=sayiListesi[i]
#     return topla

# sayilistesi=[1,2,3,4]
# sonuc =toplamBul(sayilistesi)
# print(sonuc)


#*************************************** 

#vize 40 final 60 ortalama 50 den kücükse kalan ders programı

# x= int(input("Vize notunuzu giriniz: "))
# y= int(input("Final notunuzu giriniz: "))

# ortalama = (x*0.4)+(y*0.6)

# sonuc = ortalama <50 and ortalama <40 # ortalama hem 50 hemde 40 tan aynı anda büyük olmalı ki true geçsin

# #and operatoru &&, or operatoru || aynı şeyler
# print("Ortalama: ",ortalama , ", kaldi mi: ",sonuc)


# # ----------------------------------------------ehliyet alabilir mi programı

# name= input("Adiniz: ")
# age= int(input("Yasiniz: "))
# degree= input("Egitim durumunuz: ")

# if age>=18 and (degree =="universite" or degree == "lise"):
#     print("Ehliyet alabilirsiniz.")
# else:
#     print("Ehliyet alamazsiniz.")
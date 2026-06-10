# def topla(liste=[0]):
#     topla = 0
#     for i in range(0,len(liste)):
#         topla += liste[i]
#     return f"toplamlari: {topla}"

# x = int(input("Kac sayi olacagini giriniz:")) #birazdan da sıfır basınca çıkmalı yap

# liste=[i for i in range(0,x)] ----> liste boyutunu ayarladık
# for i in range(0,x):
#     liste[i]=int(input(f"{i+1}. sayiyi girin:"))
# sonuc=topla(liste)
# print(sonuc)

# vize=[i for i in range(0,5)] #boyutunu ayarlamak için yapılıyor kısa yoldan böyle
# a ="5"
# sonuc = a.isnumeric()
# print(sonuc)

# ------------------------- SORULAR

# 1.	Sayı Dizisi Kontrolü: Kullanıcıdan virgülle ayrılmış bir sayı dizisi 
# (örneğin "5,12,3,18,7") alınız. Bu dizideki her sayının çift mi, tek mi olduğunu 
# veya 10'dan büyük ve çift mi olduğunu belirleyerek uygun mesajları yazdırın. (Örn: "5 tek", "12 çift", "18 çift ve 10'dan büyük")

# x = int(input("Kac tane sayi olacak:"))
# liste = [i for i in range(0,x)]
# for i in range(0,x):
#     liste[i]= int(input(f"{i+1}. sayiyi giriniz: ")) #listeyi hazıladık
# for i in range(0,x):
#     if liste[i]%2==0:
#         print(f" {liste[i]} cift ")
#     else:
#         print(f" {liste[i]} tek ")

# ------------------------------------------

# 2.	Kredi Notu Değerlendirmesi: Bir öğrencinin ders notunu (0-100 arası) alın. 
# o	90-100: A
# o	80-89: B
# o	70-79: C
# o	60-69: D
# o	0-59: F Bu aralıklara göre harf notunu ekrana yazdıran bir program yazın. Geçersiz girişler için hata mesajı verin.

# try:
#     nots = int(input("Ders notunu giriniz: "))

#     if nots<0 or 101<=nots:
#         print("Geçerli bir sayi girin") 
#     elif nots>=90:
#         harf= "A"
#         print(f"Harf notunuz: {harf}")
#     elif nots>=80 and nots <90:
#         harf= "B"
#         print(f"Harf notunuz: {harf}")
#     elif nots>=70 and nots <80:
#         harf= "C"
#         print(f"Harf notunuz: {harf}")
#     elif nots>60 and nots <70:
#         harf= "D"
#         print(f"Harf notunuz: {harf}")
#     elif nots<=60:
#         harf= "F"
#         print(f"Harf notunuz: {harf}")
    
# except ValueError:
#     print("Geçerli bir sayi girin")
# except TypeError:
#     print("Geçerli bir sayi girin")

# ----------------------- sözlükteki verilere erişim

# ogrenci_bilgileri = {
#     "sinif_1": {
#         "ogrenci_1": {"ad": "Ali", "soyad": "Yilmaz", "not": 85},
#         "ogrenci_2": {"ad": "Ayşe", "soyad": "Kara", "not": 92}
#     },
#     "sinif_2": {
#         "ogrenci_3": {"ad": "Can", "soyad": "Demir", "not": 78}
#     }
# }
# print(ogrenci_bilgileri["sinif_1"]["ogrenci_2"]["ad"])

# ------------------------ sayıları sıralama

# isim=[1,2,4,5,8,84,-5]
# isim.sort()
# print(isim) #sıralama

# ---------------------sözlük ile kare alma


# kuvvetler = { #sözlük

#     "kare":
#     {"1":"1","2":"4","3":"9","4":"16",
#      "5":"25","6":"36","7":"49","8":"64",
#      "9":"81","10":"100"}
# }

# x = input("Kuvvetinin alinmasini istediginiz sayiyi girin: ")

# print(kuvvetler["kare"][f"{x}"])

# -------------------------SÖZLÜK


# iller={ "konya" :"42","istanbul" :"34","ankara" :"06" }
# print ( iller.keys())
#values()metodu sözlükteki değerleri bize yazdırır.
# print (iller.values())


# iller.pop("konya") #burda konya anahtarını ve değerini siler 
# print(iller)

# iller.popitem() #bu da sondaki değer ve anahtarı siler
# print(iller)

# iller.clear() #bütün sözlüğü boşaltır
# print(iller)

# ----------------------TEKRAR EDEN HARFLER

# 1. Tekrar Eden Harfleri Bulma
# Bir metin alarak, hangi harflerin kaç kez tekrar ettiğini sözlük yapısı ile gösteren bir program yazınız. Büyük/küçük harf ayrımı yapılmasın.
# 🔸 Kavramlar: Döngü, sözlük, fonksiyon

# yazi = input("Yaziyi girin: ").lower()
# harfler={}
# for i in yazi:
#     sayac =0
#     for a in yazi:
#         if i == a:
#             sayac += 1
#             harfler[a] = sayac
# print(harfler)

# ---------------------------
# sözlük ={"son":3}
# sözlük["ilk"]=5 #sözlüğe ekleme yapılabilri böyle
# print(sözlük)
# ---------------------------dosyalı

# dosya = open("notlar.txt","r")
# x = input("dosya içine yazilacak: ")
# dosya.write(x)
# oku = dosya.read()
# print(oku)

# for i in dosya:
#     isim , notlar = i.strip().split(",")#strip boşlukları siler split de , ü silip iki değişkene dönüştürür!!!!
#     notlar = int(notlar)
#     if notlar >=75:
#         durum = "gecti"
#     else: 
#         durum = "kaldi"

#     print(f"{isim},{notlar} - {durum}")

# -------------------

# liste = [i for i in range(0,10) ]
# for i in range(0,10):
#     liste[i]= int(input(f"{i+1}. sayiyi girin: "))
# liste.sort()
# if liste[-1] == liste[-2] or liste[-1]== liste[-3] or liste[-2]== liste[-3]:
#     if liste[-1] == liste[-2]:
#         print(f"Listenin en buyuk 3 elemani: {liste[-1]},{liste[-3]},{liste[-4]} ")  
#     elif liste[-1]== liste[-3]:
#         print(f"Listenin en buyuk 3 elemani: {liste[-1]},{liste[-2]},{liste[-4]} ")  
#     elif liste[-2]== liste[-3]:
#         print(f"Listenin en buyuk 3 elemani: {liste[-1]},{liste[-2]},{liste[-4]} ") 
# else:
#     print(f"Listenin en buyuk 3 elemani: {liste[-1]},{liste[-2]},{liste[-3]} ") 

# --------------------------

# x = input("isim: ")
# y= int(input("not ort: "))
# sozluk = {}
# sozluk[f"{x}"]=y
# print(sozluk)

# -----------------------

# def sesli_harf_sayaci(metin):
#     sesliler="aeoöüiu"
#     sayac = 0
#     for i in metin:
#         if i in sesliler:
#             sayac += 1
#     return sayac


# metin = "ARDA"
# sonuc =sesli_harf_sayaci(metin.lower())
# print(sonuc)


# -------------------
# import random
# sayi = random.randint(1,1000)

# deneme = 0
# while True:
#     cevap = int(input("Tahmininiz: "))
#     if cevap > sayi:
#         print("Assagi")
#         deneme +=1
#         continue
#     elif cevap < sayi:
#         print("Yukari")
#         deneme +=1
#         continue
#     elif cevap == sayi:
#         print(f"Tebrikler!, {deneme} denemede bildiniz.")
#         break

# -------------------------
# def aynilari(liste1,liste2):
#     ayni=[]
#     for i in liste1:
#         if i in liste2:
#             ayni.append(i)
#     return ayni



# list1= [1,"a",45,78,4.5]
# list2= [46,4.5,"a","b"]

# sonuc = aynilari(list1,list2)
# print(sonuc)


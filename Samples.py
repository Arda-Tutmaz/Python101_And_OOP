#-- Şekillerin alanını hesaplayan program
# class Sekiller():
#     def __init__(self,a,h):
#         self.a=a
#         self.h=h

#     def alan_hesapla():
#         pass

# class Ucgen(Sekiller):
#     def alan_hesapla(self):
#         return (self.a*self.h)/2

# class Paralelkenar(Sekiller):
#     def alan_hesapla(self):
#         return self.a*self.h
    
# class Yamuk(Sekiller):
#     def __init__(self,a,h,b):
#         super().__init__(a,h)
#         self.b=b

#     def alan_hesapla(self):
#         return((self.a+self.b)*self.h)/2
    
# u1 = Ucgen(2,5)
# print(u1.alan_hesapla())
# p1 = Paralelkenar(2,7)
# print(p1.alan_hesapla())
# y1 = Yamuk(3,4,7)
# print(y1.alan_hesapla())

# --- Banka uygulaması


# from abc import ABC, abstractmethod

# class Banka():
#     def __init__(self,ad,soyad,bakiye):
#         self.ad=ad
#         self.soyad=soyad
#         self.bakiye=bakiye
#         print("Hesap oluşturuldu.")
    
#     def para_yatır(self,miktar):
#         if miktar <=0:
#             print("Geçersiz miktar girişi.")
#         else:
#             self.bakiye += miktar
#             print(f"Miktar hesabınıza yatırıldı.\nToplam bakiye:{self.bakiye}")
#     def para_cek(self,miktar):
#         if miktar <= self.bakiye:
#             self.bakiye -= miktar
#             print(f"Miktar hesabınızdan çekildi.\nKalan bakiye:{self.bakiye}")
#         else: print("Geçersiz miktar girişi.")

#     @abstractmethod
#     def mevduatFaiz_goster():
#         pass

#     def mevduat_hesapAc(self,miktar,faiz_oran):
#         if miktar <= self.bakiye:
#             self.bakiye -= miktar
            
#             yillik_faiz = (miktar/100)*faiz_oran*1
#             toplam = yillik_faiz+miktar
#             print("\n***Hesap Oluşturuldu***")
#             print(f"Şu anki bakiye:{miktar}")
#             print(f"Yıllık faiz miktarı:{yillik_faiz}")
#             print(f"Yil sonunda toplam bakiye:{toplam}\n")
#         else: print("Yetersiz miktar girişi. Hesap oluşturulamadı.")

# class Ziraat(Banka):
#     def mevduatFaiz_goster(self):
#         print("Ziraat bankasının yıllık faiz oranı: %45\n")
    
#     def mevduat_hesapAc(self, miktar):
#         super().mevduat_hesapAc(miktar,45)
    
# class Halk(Banka):
#     def mevduatFaiz_goster(self):
#         print("Halk bankasının yıllık faiz oranı: %37\n")
    
#     def mevduat_hesapAc(self, miktar):
#         super().mevduat_hesapAc(miktar,37)

# z1 = Ziraat("Arda","Tutmaz",10000)
# z1.para_yatır(10000)
# z1.mevduat_hesapAc(10000)
# z1.mevduatFaiz_goster()

# h1 = Halk("Arda","Tutmaz",10000)
# h1.para_cek(5000)
# h1.para_yatır(15000)
# h1.mevduat_hesapAc(20000)

# ---5 basamaklı bir sayının basamaklarının toplamını bulan program

# sayı = input("Sayıyı girin:")

# toplam=0
# if len(sayı) == 5 :
#     for i in sayı:
#         toplam += int(i)
#     print(toplam)
# else:print("Yanlıs sayı girişi.") 

# ---En büyük ve en küçük sayı ile ortanca sayının farkını bulan program

# i=0
# liste=[]
# while i<3:
#     sayi = int(input(f"{i+1}. sayiyi girin:"))
#     liste.append(sayi)
#     i+=1

# liste.sort()
# enbuyuk=max(liste)
# enkucuk=min(liste)

# print(f"En buyuk sayi ile ortancanin farkı:{enbuyuk - liste[1]}")
# print(f"En kucuk sayi ile ortancanin farkı:{enkucuk - liste[1]}")

# ----

# sınıf metodu sınıfa özel nitelikleri kullanabilmemize yarayan metodlardır. @classmethod bezeyiicisi kullanılır.
# statik metod ise sınıf ve örneklem nitelikleri kullanılmadan kullanılabilen metodlardır. @staticmethod bezeyicisi kullanılır.

# kalıtım (inheritance), bir sınıfın içerisindeki metodları, nitelikleri başka bir sınıfa tekrar tanımmlamadan aktarabilmemize yarar
# tekli kalıtım: tek bir ana sınıf ve bir alt sınıftan oluşur
# çoklu kalıtım: birçok ana sınıf ve bir alt sınıftan oluşur
# çok düzeyli kalıtım: bir ana sınıfın bir alt sınıfa, alt sınıfında altındaki bir sınıfa zincirleme kalıtım yapmasıdır a>b>c olarak gidilir
# hiyerarşik kalıtım: bir ana sınıfın birden fazla alt sınıfa kalıtım yapmasıdır
# ---


# ----- Çalışan ekleme ve zam oranı ayarlama programı -----
# class Calisan():
#     zam_orani = 1.10
#     gun = "sali"
#     def __init__(self,isim,soyisim,maas):
#         self.ad=isim
#         self.soyad=soyisim
#         self.maas=maas
    
#     def zam_yap(self):
#         self.maas = Calisan.zam_orani*self.maas
#         print("Maasa zam yapildi")
    
#     @classmethod
#     def zam_degis(cls,yeni):
#         cls.zam_orani=yeni
#         print("Zam orani guncellendi.")
#     @classmethod
#     def metin_veri(cls,veri):
#         ad, soyad, maas = veri.split("-")
#         return cls(ad,soyad,maas)
    
#     @staticmethod
#     def tatil_kontrol():
#         if Calisan.gun == "Cumartesi" or Calisan.gun== "Pazar":
#             return True
#         else: return False

# c1 = Calisan("arda","tutmaz",2000)
# c1.zam_yap()
# c1.tatil_kontrol()
# c2= Calisan.metin_veri("Cuneyt-Tommisogullari-2000")
# print(c2.ad)

# ----------------araç sınıfı ve otomobil, kamyon sınıfları oluşturma ve araçların durumunu gösterme programı -----


# class Arac():
#     def __init__(self,marka,model,yıl,kilometre):
#         self.marka=marka
#         self.model = model
#         self.yıl=yıl
#         self.km=kilometre
    
#     def durum_goster(self):
#         print(f"----{self.marka}----\nModel:{self.model}\nYıl:{self.yıl}\nKm:{self.km}")
    
# class Otomobil(Arac):
#     def __init__(self,marka,model,yıl,kilometre,kapı_sayısı):
#         super().__init__(marka,model,yıl,kilometre)
#         self.kapi_s=kapı_sayısı
#     def durum_goster(self):
#         super().durum_goster()
#         print(f"Kapi Sayisi:{self.kapi_s}")

# class Kamyon(Otomobil):
#     def __init__(self,marka,model,yıl,kilometre,kapı_sayısı,tasimak):
#         super().__init__(marka,model,yıl,kilometre,kapı_sayısı)
#         self.tasimak=tasimak

#     def durum_goster(self):
#         super().durum_goster()
#         print(f"Tasima Kapasitesi:{self.tasimak}")

#     def yuk_yukle(self,yuk):
#         if yuk > self.tasimak:
#             print("\nKapasite asıldı!\n")
#         else: print("\nYuk yuklendi.\n")

# arac1= Otomobil("Porsche","GTR",2020,3000,2)
# arac1.durum_goster()

# arac2 = Kamyon("PompApo","Apo",1950,10000,5,8)
# arac2.yuk_yukle(9)
# arac2.durum_goster()

# ---------------------
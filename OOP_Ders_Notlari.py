# sınıf: benzer özellikler ortak amaçlar taşıyan, içerisinde metod ve değişkenler olan yapılar
# class Human():
#     print("Başarıyla oluşturuldu")

# ------------

# Sınıf özeliikleri(class attirbutes)

# class Human():
#     bolum = "CS"
#     sql="evet"
#     yas = 15
#     diller = []

# # print(Human.bolum) #özelliğe eriştim

# arda = Human()
# Human.sql = "Hayir" #sınıf özelliğini değişmek
# print(Human.sql)
# print(arda.sql) #verdiğimiz örnekte de bu özellik değişmiş oldu

# --------sınıf örneklendirmesi (instantiation)

# sınıftan farklı farklı alt kümeler oluşturmak

# ali = Human() #ali ye sınıfın özelliklerini verdik
# arda = Human()
# print(ali.sql) #eğer sınıf özelliğini değiştirseydim burda da değişirdi
# ali.sql = "hayır"
# ali.diller.append("Python")
# print(ali.sql)
# print(arda.sql)
# # arda da değişmedi fakat ali de değişti. burda ali örneğinde override oldu
# print(ali.diller)
# print(arda.diller)
# # fakat üstte listede alide yaptığım bir değişiklik tüm bir sınıfın değişikliğine neden oldu



# -------------------------örnek özellikleri
# örneklerin her6

# class VeriBilimci():
#     def __init__(self): #----> bu nedir: self örneklemi temsil eder(ali,veli vb.) 
#         self.diller = [] # bu yaptığımız işlem her bir ayrı örneklendirme için özellik nitelik tutar
# ali = VeriBilimci()
# veli = VeriBilimci()
# ali.diller.append("Python")
# print(ali.diller)
# print(veli.diller) #burda veli boş ali de python gözükür

# print(VeriBilimci.diller) # normalde yukarda böyle yapınca sınıfın özelliklerini yazardı. şimdi ise hata veriyor
# bunun nedeni ise sınıf değil bir örnek özelliği tanımlamamız

# her ikisini birden tanımlamak istersek:
# class VeriBilimci():
#     diller = ["r","python"] # bu bir sınıf niteliği
#     sql = "var"
#     def __init__(self): 
#         self.diller = []# bu bir örnek niteliği
# ali = VeriBilimci()
# ali.sql = "yok"
# veli = VeriBilimci()
# ali.diller.append("Python")
# print(VeriBilimci.diller)
# print(ali.diller)
# print(ali.sql)
# print(veli.sql)
# print(veli.diller)


# ------------örnek metodları 
# yani bir fonksiyon tanımlamadır. mesela yeni öğrenilen bir dili kendi dillerine ekleme vb
# class Veribilimci():
#     global ay
#     ay = 8
#     def __init__(self):
#         self.diller = []
#         self.yas= 0
#         self.ay = 0
#     def yasArttir(self):
#         self.yas +=1
#         print(f"Doğum Gunun Kutlu Olsun! Doğum günün {self.ay-ay} ay onceydi. Yasın: {self.yas}")
#     def BDkontrol(self):
#         if self.ay >= ay:
#             self.yasArttir()
#         else:
#             print(f"Doğum gününe {ay-self.ay} ay kaldi. Yasın: {self.yas}")


# ali = Veribilimci()
# veli = Veribilimci()
# ali.yas = 15
# ali.ay = 6

# ali.BDkontrol() #burda bir yaş ve bir ay ayarladım ağer ay  örneğin ayından az olursa bir yaş atlattım

# --------------mutsayon ve gölgeleme
# class C:
#     ortak = [] #Liste
# a = C()
# b = C()

# a.ortak.append(2) #böyle yaparsak Mutasyon olur yani listenin içeriği komple değişir
# a.ortak =[2] #böyle yaparsak sadece örnekleme göre oluşturmuş olur

# ----personel ekleme örneği

# class Personel():
#     liste=[]
#     def __init__(self,ad,soyad):
#         self.ad = ad
#         self.soyad = soyad
#         self.personel_ekle()

#     def personel_ekle(self):
#         al=(self.ad , self.soyad)
#         self.liste.append(al)

#     def personel_cıkar(self):
#         a=0
#         al=(self.ad , self.soyad)
#         for i in self.liste:
#             if i == al:
#                 self.liste.pop(a)
#             else:a+=1
#         print(f"\n{self.ad} {self.soyad} listeden çıkarıldı.\n")

#     def personel_goruntule(self):
#         print("Personeller:")
#         for i in self.liste:
#             print(*i)

# p1 = Personel("Arda","Tutmaz")
# p2 = Personel("Amına çaktığım","Apo")
# p3 = Personel("Deniz","Bacaksız")
# p1.personel_goruntule()
# p2.personel_cıkar()
# p1.personel_goruntule()

# ------Miras alma ve farklı metodlar

# sınıf methodları: bir sınıfın metodlarını sınıfın kendisi üzerinden çağırmaya olanak sağlar

# @classmethod ile tanımlanan yöntemler, sınıfın kendi durumu veya özelliklerini değiştirmek için kullanılır. BU yapıda yaygın olarak cls parametresi gireriz

# örnek kullanım

# class arda():
#     liste =[]
#     def __init__(self,isim,yas):
#         self.ad = isim
#         self.yas=yas
#         self.listeleme()

#     def listeleme(self):
#         self.liste.append(self.ad)
    
#     @classmethod
#     def sinif_metodu(cls):
#         print(f"Listede {len(cls.liste)} kişi var")

# p1 = arda("arda",4)
# p2 = arda("mehmet",2)
# p3 = arda("cüneyt",18)

# p1.sinif_metodu()

# -STATİK METODLAR----------Eğer bir sınıf içindeki herhangi bir fonksiyonda örnek veya sınıf niteliklerinin hiçbirine erişmeniz gerekmiyorsa, statik metotları kullanacağız.
# Statik metotlarda cls ve self kullanılmaz…

# class Dort_Islem():

#     @staticmethod
#     def pi():
#         return 22/7
    
#     @staticmethod
#     def karekok(sayi):
#         return sayi**0.5

# a= int(input("Karekoku alinacak sayiyi girin:"))
# print(Dort_Islem.karekok(a))

# ----MİRAS ALMA

# başka bir sınıfın tüm mirasına (özellik ve fonksiyonlar) sahip, yeni bir sınıf oluşturulur.
# Python'da, ilgili alt ve ana sınıflarının sayısına bağlı olarak dört tür kalıtım yapısı bulunmaktadır.
# 1. Tekli Kalıtım: bir ana sınıf ve bir alt sınıftan oluşur
# 2. Çoklu Kalıtım: iki ana sınıf ve bir alt sınıftan oluşur
# 3. Çok Düzeyli Kalıtım: tek ana sınıf ve iki alt sınıftan oluşur. bu türde en alt sınıf bir üst sınıftan iki sınıfın da durumunu alır
# 4. Hiyerarşik Kalıtım: tek ana sınıf farklı farklı alt sınıfları birbirine bağlamadan kalıtım sağlar


# ---Overriding:Eğer biz miras aldığımız metotları aynı isimle türetilmiş sınıfta tekrar tanımlarsak, artık
# metodu çağırdığımız zaman miras aldığımız değil kendi metodumuz çalışacaktır. 

# super() fonksiyonu:Alt sınıfta super() fonksiyonu kullanarak ana sınıfın tüm özellik ve metotlarına ulaşılır.

# class Human():
#     def __init__(self,ad,soyad):
#         self.ad = ad
#         self.soyad = soyad

#     def Bilgiler(self):
#         print(f"----İnsanın bilgileri----\nAd:{self.ad}\nSoyad:{self.soyad}")

# class Ogrenci(Human):
#     def __init__(self,ad,soyad,no):
#         super().__init__(ad,soyad)
#         self.no = no
#         super().Bilgiler()
# o1 = Ogrenci("arda","tutmaz",254)

# -----Kapsülleme, Soyutlama Ve Çok Biçimcilik----

# Kapsülleme:  OOOP nin en temel 4 yapı taşından biridir
# Özellikle pyhton gibi dillerde kod büyüdükçe kodun yönetilebilirlir kalmasını sağlar.
# Sınıf içindeki üyelere dışarıdan ve içeriden erişimin kısıtlanmasıdır
# private: sadece tanımlandığı sınıfın içinden erişilebilir
# protected: sadece kendi sınıfı ve o sınıftan türetilen alt sınıflardan erişilebilir

# KONTOLLÜ ERİŞİM(GETTER VE SETTER): getter: veriyi okumak için kkullanılır, setter: veriyi değiştirmek için kullanılır

# class Human():
#     def __init__(self,ad,soyad,yas=0):
#         self.ad=ad
#         self.soyad=soyad
#         self.__yas=yas

#     def get_yas(self):
#         return self.__yas
    
#     def set_yas(self,yeni):
#         if yeni>0 or yeni<120:
#             self.__yas = yeni
#             print("Yeni yas atandi.")
# class Std(Human):
#     def __init__(self,ad,soyad,yas=0):
#         super().__init__(ad,soyad,yas)

# h1 = Human("arda","Tutmaz",15)
# h2 = Std("ahmet","mehmet",18)

# print(h2.get_yas())
# burda sadece ad ve soyad değişkenlerine ulaşaibliryoruz çünkü yas private

# Veri Bütünlüğünü Koruma: En önemli amaç budur. Kullanıcının veriye mantıksız değerler ataması engellenir.
# • Örneğin, bir İnsan sınıfında yas değişkeni public olsaydı, dışarıdan insan1.yas = -50 yazılabilirdi.
# • Kapsülleme ile set_yas(deger) metodu yazar ve içine "Eğer değer 0'dan küçükse hata ver" kuralını koyarak veri bütünlüğü/güvenirliliği sağlamış oluruz.

# Salt okunur veri oluşturmak için kullanılır: sadece getter metodu kullanarak sadece okunmasısını saülayaibliriz

# ---@property metodu----

# bu yöntemle metodu sanki bir değişkenmiş gibi kullanabilirz
# örn ogr.not=80 deriz ama arka planda ilgili metod çalışır

# bu sistmein çalışması için:
# 1. isim kardeşliği:@property altındaki fonksiyonun adı neyse, setter dekoratörünün adı da o olmalı
# 2. her zaman ilk önce protperty, sonra setter tanımlanmalı
# depolama farkı: metodun adı bilgi ise, veriyi sakladığınd eğişkenin ismi bilgi olamaz

# class Human():
#     def __init__(self,ad,soyad,yas):
#         self.ad=ad
#         self.soyad=soyad
#         self.__yas=yas
    
#     @property
#     def age(self):
#         return self.__yas
    
#     @age.setter
#     def age(self,yeni):
#         if yeni >0 and yeni <100:
#             self.__yas = yeni
#             print("Yas degistirildi")
#         else:print("Hatali giriş")

# h1 = Human("arda","tutmaz",25)
# print(h1.age)
# h1.age =99

# print(h1.age)

# -----2. örnek

# class Calisan():
#     __liste=[]

#     def __init__(self,ad,soyad):
#         self.ad=ad
#         self.soyad=soyad
#         self.__personel_ekleme()

#     def __personel_ekleme(self):
#         a= (self.ad,self.soyad)
#         self.__liste.append(a)        
    
#     @classmethod
#     def personel_goruntule(cls):
#         print("------Personeller------")
#         for i in cls.__liste:
#             print(*i)
# c1 = Calisan("arda","tutmaz")
# c1 = Calisan("amk","aposu")
# c1 = Calisan("apotelli","çakotelli")

# c1.personel_goruntule()

# İşleyiş Sırasını Garanti Altına Almak: Bir işlemin gerçekleşmesi
# için arka arkaya 5 adımın atılması gerektiğini düşünün (A -> B ->
# C -> D -> E). Eğer bu adımların hepsi public olursa, yazılımcı
# yanlışlıkla A'yı yapmadan C'yi çağırabilir. Bu da programı
# çökertir. Kapsülleme ile bu ara adımları private (gizli) yaparız ve
# dışarıya sadece tek bir "Başlat" butonu (public metot) koyarız.

# ------SOYUTLAMA------

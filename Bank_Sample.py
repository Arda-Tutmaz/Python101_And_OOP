#-- Banka Hesap Yönetimi Kodu--

from abc import ABC, abstractmethod

class Banka(ABC):
    def __init__(self,ad,soyad,bakiye):
        self.ad=ad
        self.soyad=soyad
        self.bakiye=bakiye
        print("\n****Banka hesabı oluşturuldu****\n")

    def para_yatir(self,miktar):
        if miktar >0:
            self.bakiye += miktar
            print(f"Miktar hesabınıza aktarıldı.\nHesap Bakiyeniz:{self.bakiye}")
        else:print("Gecersiz miktar girisi!")
    def para_cek(self,miktar):
        if miktar <= self.bakiye:
            self.bakiye -= miktar
            print(f"Para çekildi.\nKalan bakiyeniz:{self.bakiye}")
        else:print("Gecersiz miktar girisi! Bakiye çekilemedi.")

    @abstractmethod
    def mevduatFaiz_goster():
        pass

    def mevduat_hesapAc(self,yatirilan,faiz_oran):
        if yatirilan <= self.bakiye:
            self.bakiye -= yatirilan
            
            yillik_faiz = (yatirilan/100) * (faiz_oran) *1
            toplam_bakiye= yillik_faiz+yatirilan


            print("\n***Mevduat Hesabı Açıldı***")
            print(f"Su anki bakiyeniz:{yatirilan}")
            print(f"Yıllık faiz:{yillik_faiz}")
            print(f"Yıl sonu toplam bakiyesi:{toplam_bakiye}")

        else:print("Gecersiz bakiye girişi. ")

class Ziraat(Banka):
    def mevduatFaiz_goster(self):
        print("\n**Ziraat bankasinin yıllık faiz oranı: %45**")
    
    def mevduat_hesapAc(self, yatirilan):
        super().mevduat_hesapAc(yatirilan,45)

class Halk(Banka):
    def mevduatFaiz_goster(self):
        print("\n**Halk bankasinin yıllık faiz oranı: %37**")
    
    def mevduat_hesapAc(self, yatirilan):
        super().mevduat_hesapAc(yatirilan,37)

z1= Ziraat("Arda","Tutmaz",10000)
z1.para_yatir(10000)
z1.mevduat_hesapAc(10000)
z1.mevduatFaiz_goster()

h1 = Halk("Arda","Tutmaz",0)
h1.para_yatir(100000)
h1.mevduat_hesapAc(100000)
h1.mevduatFaiz_goster()
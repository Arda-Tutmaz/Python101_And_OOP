# class Kullanici():
    
#     adress = "no info"

#     def __init__(self,name,year):
#         self.name= name
#         self.year= year

#     def intro(self):
#         print("Merhaba,",self.name)
    
#     def calculateAge(self):
#         return 2025-self.year

# p1 = Kullanici("Arda",2006)

# print(p1.name , p1.year, p1.adress)
# p1.intro()
# print("Yasiniz:",p1.calculateAge())

# orn:cevre hesabi yapan sınıf 

# class Circle():
#     pi = 3.14

#     def __init__(self,yaricap=1):
#         self.yaricap = yaricap
    
#     def cevreHesabi(aşwlkmdikaw):
#         return aşwlkmdikaw.yaricap*2*aşwlkmdikaw.pi
# c1 = Circle()
# c2 = Circle(2)
# print("Çevre:",c1.cevreHesabi())
# print("Çevre:",c2.cevreHesabi())

# ----Kalıtım,miras(Inheritence)-----------
# Person sınıfının özellikleri ve örneklerini başka açılan sınıflar içerisinde de kullanabilmeye yarar
# örneğin:
# Person => namei lastname, age, eat()....vb
# Student(Person) , Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

# örnek:

# class Person():
#     def __init__(self,ad,soyad):
#         self.ad = ad
#         self.soyad = soyad
#         print("Person Created")
    
#     def eat(self):
#         print(self.ad)
#         print("I am eating")

#     def wai(self):
#         print("I am a person",self.ad)

# class Student(Person):
#     def __init__(self,ad,soyad):
#         Person.__init__(self,ad ,soyad)
#         print("Student Created")

#     # def wai(self): ---> overriding
#         # print("I am a student",self.ad) ----> ama student içine ayrı bir tane açarsanız onu okur
        
# class Teacher(Person):
#     def __init__(self,ad,soyad,branch):
#         super().__init__(ad,soyad)
#         self.branch = branch
#     def wai(self):
#         print("I am a teacher",self.ad)


# s1 = Student("Arda","tutmaz")
# p1 = Person("Deniz","bacaksiz")
# t1 = Teacher("Özcan","Yirtici","Mat")
# # print(p1.ad,p1.soyad)
# # print(s1.ad,s1.soyad)
# # p1.eat()
# # s1.eat() -----> studnetin içinde eat olmamasına rağmen eati kullanabiliyoruz
# p1.wai()
# s1.wai()
# t1.wai()
# t1.eat()




# -----------------örnek--------------------------------
# Sınıf yapısını kullanarak geometrik şekillerin (üçgen,paralelkenar ve yamuğun alanlarını hesaplayan programı miras alma ile tasarlayın)

# class Alan():
#     def __init__(self,a,h):
#         self.a= a
#         self.h = h
        
# class Yamuk(Alan):
#     def __init__(self,a=0,h=0,b=0):
#         Alan.__init__(self,a,h)
#         self.b=b

#     def alanHesapla(self,a,h,b):
#         return ((a+b)*h)/2

# class Ucgen(Alan):
#     def __init__(self, a=0, h=0):
#         super().__init__(a, h)

#     def alanHesapla(self,a,h):
#         return a*h/2
# class Paralelkenar(Alan):
#     def __init__(self,a=0,h=0):
#         super().__init__(a,h)
#     def alanHesapla(self,a,h):
#         return a*h
# y1 = Yamuk()
# u1 = Ucgen()
# p1 = Paralelkenar()
# print(y1.alanHesapla(4,5,6))
# print(u1.alanHesapla(1,2))
# print(p1.alanHesapla(4,5))
# ------------------Özel Metodlar------------------------------
class film():
    def __init__(self,name):
        self.name = name

    def __str__(self): #m i normalde yazdırmaya çalıştığımızda tutulduğu yerin numarası gözüküyoru fakat str komudu ile ayarlayınca burda yazdığın komudu döndürür
        return "hello"
    def __len__(self): #m dosyasının noramlde bir uzunluğu yok, fakat bu fonksiyonla uzunluk verebilriiz
        return 150 
    def __del__(self): #m dosyasını silince bunu yazacak
        print("silindi")
    
m = film("arda")
print(len(m))

del m


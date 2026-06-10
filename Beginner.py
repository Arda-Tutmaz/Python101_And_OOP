#  x=100
#  print(x - (x*0.25))
#  Name="Arda"
#  Surname=" Tutmaz"
#  print(Name + Surname)

# x,y,z=(1,2.5,"arda")

# x= input("Sayiyi girin: ")
# y= input("Sayiyi girin: ") #inputtan gelen değerler 
# #her zaman string gelir

# x= float(x)
# print( int(x) + int(y))

#************************************

#yarıçapı verilen bir dairenin alan ve çevresini hesaplayın
#(3.14)

# r= int(input("Yaricapini girin: "))

# dairealan= (3.14) * (r*r)
# dairecevre= 2 * 3.14 *r

# print("Dairenin alani: ", dairealan)
# print("Dairenin cevresi: ", dairecevre)

# name="arda"
# surname="tutmaz"
# age = 36
# greeting = "My name is "+name + " " + surname + "\nAnd im "+ str(age) +" years old." 
# lengh= len(greeting)
# print(greeting)

# print(len(greeting)) #yazının kaç karakter oldugunu gösterir
# #eğer son karakteri yazmak istersek:
# print(greeting[lengh-2]) #0 dan başlıyo
# print(greeting[-2]) #aynı şey
# print(greeting[3:7])#3 ten 7 ye kadar(3. index numarası dahil değil!)
# print(greeting[5:])#5 ten sona
# # print(greeting[4:10:2])# 2 şer karakter al
# print(greeting[:6]="abcdef") # 0 dan 6 ya kadar rakamları bunla değiş

# print("My name is {} {}".format(name,surname))
# print("My name is {0} {1}".format(name,surname))
# print("My name is {1} {0}".format(name,surname))
# print("My name is {s} {n}\n".format(n=name,s=surname))
# sonuc=500 /100
# print("Sonuc: {r:1.3}".format(r=sonuc))#1.3 bilgisi . dan sonra kaç karakter 


# #bu da yeni gelen özellik
# print(f"Merhaba ben {name} {surname}, {age} yasindayim.")

# dialog= "Merhaba ben Arda Tutmaz"

# dialog = dialog.upper()               #tüm diyaloğu caps ile yazar(buyuk harf)
# dialog = dialog.lower()               #hepsini küçük yazar
# dialog = dialog.title()               #her kelimenin baş harfi büyük
# # dialog = dialog.capitalize()        #sadece ilk harf büyük
# dialog = dialog.strip()               #baş ve sonda boşlukları siler (lstrip ve rstrip olarak ta kullanıalbilir)
# print(dialog)

# isim="arda"
# sonuc=0
# sonuc = isim.count("a")                #.count() metodu içinde kaç tane olduğunu bulur(tek bir karakter olamsına gerek yok)

# sonuc = isim.startswith("a")           # burda da starts with yani onunla başlıyor mu olduğunu bulup true yada false döndürmek için kullanılır
                                         #aynı işlemi ends with ile sonunda bitip bitmediğini bulabirlsin

# dialog = "arda cok pro ya dimi"
# sonuc=dialog.find("ya")                # .find metodu kaçıncı indexten itibaren başladığını bulur
                                          #.rfind ise sağdan başlayarak bulur ///// aynısını index metodu ile de yaparsın ama birşey bulamazsa hata döndürür

# sonuc = isim.isalpha()                   #bütün textin alfabetik mi oluştuğuna bakar
# # sonuc = isim.isdigit()                   #bütün textin numerik mi oluştuğuna bakar
#  sonuc = isim.center(50)                     # yazdığınız metni ortalar: örn 50 için 25 sağ 25 sol
#  sonuc = isim.replace("a","e")             #yazının içindeki belli edilen şeyleri değiştirir

# x = "merhaba"
# print(x[-2]) #sondan 2. index
# print(x[-4:]) #sondan 4. indexten sona kadar
# print(x[:-4]) #baştan sondan 4. indexe kadar
x=int(input("First Num:"))
y=float(input("Second Num:"))
print(x-y)
print(int(x-y))
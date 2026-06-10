# ------Biçimlendirme------------
# KARAKTER FORMATLAMA:%modülü ve format() metodu
# % metodu: 
# %s: metin değişkenler için yer tutucu
# %d: tamsayı değişkenleri için yer tutucu
# %f: ondalıklı sayı için yer tutucu
# %% : % işaretini kullanmak için kullanılır
# %c: tek bir karakteri yazdırmak için kulanılır (ASCII)

# # örn: 
# print("Benim adım %s'dir." %"arda")
# print("|%10s|" %"arda") #aralığa 10 tane boşluk bırakıp içinde sağ tarafına arda yazdı
# print("|%-10s|" %"arda") #burda da sol tarafa yazar
# a=5
# print("sayiniz: %d" %(a))

# format() metodu: değişken konumlarının metin içerisinde bildirmek daha kolay olduğu için format metodu oluşturulmuştur. bu yöntemde değişkenlerin sırasının belirli gbir düzen içinde verilme zrounluluğu ortadan kalkar.
# iki tip yazım şekli ivardır: print("{}".format()) veya print(metin.format()) ---> yer tutucu olarak süslü parantezler kullanılır
# örn : 
# print("Adın: {0} ve soyadin: {1}".format("arda","tutmaz"))

# hizalama: {:[hizalama][genişlik]} ---> 
# <:alan içindekileri sola hizalar
# >:sağa 
# ^:ortaya
# :s karakter dizileri
# :,d binlik ayraca dönüştürür 100,000
# :d sayı dizileri
# :f float türü . lı kısmı uzun
# :.2f burda noktadan sonra 2 basamak gösterilir
# {:+} verilen sayının işareti yoksa pozitif kabul eder ve + işareti koyar, aynı şekilde - de
# sayısal tipte bir ifade biçimlendirmeden yazılamaz format metodunda

# fstring yöntemi:
# print(f"{değişken}") olarka kullanılır en kolayı bence bu

# ----
# split --> parçalara böler
# rplit --> sağdan böler
# splitlines --> satır satır böler toplu bi paragrafı (ne zaman entera basılmışsa ayırır gibi gibi...)
# .title --> başlık haline getirir her bir sözcüğün baş harfini büyür
# .capitalize --> sadece baştaki harfi büyütür
# .strip ---> gereksiz karakterlerden (\n olur boşluk olur) temzileyip ekrana yazar. r ve l strip diye ayrılabilir
# index ve find anyı şeyi yapar fakat index bulamazsa hata verir öbürü -1 değerini gönderir hata vermez
# center , ljust ,rjust ----> sağa sola veya ortaya hizala için kullanılır ( istediğin karakterleri boşluk yerine değiştirebilirsin)

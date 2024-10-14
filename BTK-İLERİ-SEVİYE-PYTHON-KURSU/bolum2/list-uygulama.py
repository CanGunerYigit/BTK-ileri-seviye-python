#1 den 100 e kadar 12'ye bölünebilen sayıların listesini oluştur 
liste=[]
for i in range(1,101):
    if i % 12==0:
        liste.append(i)
print(liste)

#Verilen text içerisindeki rakamları içeren bir liste oluştur
# text ="Hello 12345 World" => [1,2,3,4,5]
text="Hello 12345 World"
liste=[]
for i in text:
    if i.isdigit():
        liste.append(i)
print(liste)

#Sıcaklıklar listesinde bulunan her hava sıcaklık bilgisine göre 4 derecenin altında "buzlanma tehlikesi" yazınız 
#sicakliklar=[20,15,0,-5,-2] => [20,15,"Buzlanma Tehlikesi","Buzlanma Tehlikesi","Buzlanma Tehlikesi"]
sicakliklar=[20,15,0,-5,-2]
liste=[]
for i in sicakliklar:
    if i<4:
        liste.append("Buzlanma Tehlikesi")
    else: 
        liste.append(i)
print(liste)

# ogrenciler ve notlar listelerindeki notu 50 den fazla olan kişileri ekrana dict verisinde yazdırınız

#ogrenciler =["ali","ahmet","canan"]
# notlar = [50,60,80]
# => "{'ahmet':60,'canan':80}"
liste =[("ali",50),("ahmet",60),("canan",80)]
sonuc={}
for isim, notu in liste:
    if notu > 50:
         sonuc[isim] = notu
print(liste)

# For döngüsüyle yazılan uygulamayı list comprehension ile yaz

#sonuc =[]
#for x in range(3):
#    for y in range(3):
#        sonuc.append((x,y))

sonuc =[(x,y) for x in range(3) for y in range(3)]
print(sonuc)
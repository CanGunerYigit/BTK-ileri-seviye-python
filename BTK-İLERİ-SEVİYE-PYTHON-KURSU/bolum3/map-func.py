sayilar = [1,2,3,4,5]
kareleri=[]
for i in sayilar:
    kareleri.append(i**2)
print(kareleri)

#yada


sonuc=list(map(lambda a :a**2, sayilar))
print(sonuc)


#string cinsinden sayılarıda map fonksiyonu ile int tipine dönüştürebiliriz
sayilar_str = ["1","2","3","4","5"]
sonuc=list(map(int,sayilar_str))
print(sonuc)

#listede bulunan string cinsindeki elemanlar üzerinde belirli fonksiyonlar kullanabilmemizi sağalr örneğin baş harfleri büyütmek 
isimler=["ali","ayşe","mehmet"]
sonuc=list(map(str.capitalize,isimler))
print(sonuc)

#listedeki sadece isimleri gösterecek
kullanicilar =[
    {"ad":"ali","soyad":"mehmet"},
    {"ad":"emre","soyad":"cengiz"}
]

sonuc=list(map(lambda kisi:kisi["ad"],kullanicilar))
print(sonuc)

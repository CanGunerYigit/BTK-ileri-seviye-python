from bs4 import BeautifulSoup

with open("bolum11\index.html") as file:
    html=file.read()
obj=BeautifulSoup(html,"html.parser")
sonuc=obj.div
sonuc=obj.find("div") #find metoduyla böylede yazılabilir
sonuc=obj.find_all("div") #her divi bulur
sonuc=len(obj.find_all("div")) #tüm divlerin sayısı
sonuc=obj.find_all("div")[1] #tüm divlerden 2. si gelsin
sonuc=obj.find_all("div")[1].h2 #2.divin altındaki h2 elementi gelir
sonuc=obj.find_all("div")[1].ul.find_all("li")[2] #2. divin altındaki listede 3. maddeyi getirir
print(sonuc)

for div in obj.find_all("div"): #tüm divlerin altındaki tüm h2 elementlerini yazdırır
    print(div.h2)
 

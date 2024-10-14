from bs4 import BeautifulSoup

with open("bolum11\index.html") as file:
    html=file.read()
obj=BeautifulSoup(html,"html.parser")

sonuc=obj.find(id="item1") #idsi item1 olan objeyi getir
sonuc=obj.find(class_="item") #classı item olan objeyi getir
sonuc=obj.find(class_="item")[1] #classı item olan 2. objeyi getir
#farklı bir alternatif select metodu fakat select objeyi değil sahip olan listeyi getirir
sonuc=obj.select("#header") #idsi header olan objelerin listesini getirir
sonuc=obj.select(".item") #classı item olan objelerin listesini getir

sonuc=obj.select_one #kritere uyan ilk objeyi getirir
sonuc=obj.div.attrs["id"] #kullanılan id ismini getirir
sonuc=obj.div.attrs["class"] #kullanılan class ismini getirir

sonuc=obj.ul.get_text()#bulduğu ilk ul elementindeki bütün textleri getirir
print(sonuc)

for a in obj.find_all("a"):
    print(a.get("href")) # sayfadaki tüm a elementlerinin href bilgilerini getirir
from bs4 import BeautifulSoup

with open("bolum11\index.html") as file:
    html=file.read()

obj= BeautifulSoup(html,"html.parser")

sonuc=obj.body.div.contents[3] #dizinin 4.divi başa dönerek tekradan 1. olur ve getirir

for i in obj.body.div.children: #bulduğu ilk divin alt elemanlarını yazdırır
    print(i) 

sonuc=obj.body.h2.parent #ilk h2 nin ebeveyn elementini getirir
sonuc=obj.body.h2.parent.parent #divinde ebeveyni bodydir direkt bodyi getirir
obj.body.next_element #bir sonraki elementi getirir
obj.body.next_sibling #aynı seviyedeki elementi getirir
print(sonuc)
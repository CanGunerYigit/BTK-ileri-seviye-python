data=[
{
    "id":1,
    "title": "MacBook Pro",
    "price": 80000
},
{
    "id":2,
    "title": "MacBook Air",
    "price": 70000
}
]
import json
with open("products.json","w",encoding="utf-8") as file:  #yukarıdaki data bilgisini dump metoduyla stringe çevirerek products.json dosyasına kayıt eder
    json.dump(data,file,ensure_ascii=False,indent=2) #ensure_ascii=False türkçe karakterleri kullanabilmemizi sağlar, indent=2 satırları alt alta, düzgün bir şekilde görüntülememizi sağlar

product={
    "id":3,
    "title":"Samsung S23", #bu veriyi oluşturduğumuz products.json dosyasının üzerine ilave edeceğiz
    "price":50000
}

with open("products.json") as file:
    products=json.load(file)
products.append(product)                              #yeni ürünü products.jsona eklemiş olduk

with open("products.json","w",encoding="utf-8") as file:
    json.dump(products,file,ensure_ascii=False,indent=2)


with open("products.json") as file:
    products=json.load(file)

for p in products:
    if p["title"]=="Samsung S23":
        p["title"]=="Samsung S24"

with open("products.json","w",encoding="utf-8") as file:
    json.dump(products,file,ensure_ascii=False,indent=2)
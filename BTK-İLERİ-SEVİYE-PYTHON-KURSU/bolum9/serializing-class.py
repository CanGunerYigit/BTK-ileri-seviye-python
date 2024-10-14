import json
class Product:
    def __init__(self,id,title,price):
        self.id = id
        self.title = title
        self.price = price
#serialize
# p1=Product(1,"Samsung S26",70000)
# p2=Product(2,"Samsung S27",80000)

# products =[p1.__dict__,p2.__dict__] #dictionary tipine çevirerek serialize edilebilir hale getiriyoruz
# 
# with open("uyg.json","w") as file:
#     json.dump(products,file)  # serialize ederek json dosyasında p1 nesnesini ekliyoruz

#deserialize
with open("uyg.json") as file: #dosyayı açıp okuyoruz
    products=json.load(file)

urunler=[] #product listesi olacak
for key,value in products.items():
    urunler.append(Product(key, value["title"],value["price"]))
for p in urunler:
    print(p.title)
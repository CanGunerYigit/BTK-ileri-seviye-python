#serializing etmek deserializingin tersidir ve encode etmek anlamına gelir
#serializing işlemini verileri güncellemek veya değiştirmek istediğimizde kullanırız

import json
product={
    "id":1,
    "title": "MacBook Pro",
    "price":90000,
    "rating":"4.5",
    "category": "Bilgisayar",
    "colors":["Red","Blue"]
}
print(product)
print(type(product)) #şuanda dict tipinde biz serialize ederek bunu string tipine çevireceğiz

sonuc=json.dumps(product) #serialize ettik
print(sonuc)
print(type(sonuc))  #ve sonuç str cinsine çevrildi

#peki bilgiler nasıl serialize ederek güncellenecek 
product={
    "id":2,
    "title": "MacBook Pro",
    "price":90000,
    "rating":"4.5",
    "category": "Bilgisayar",
    "colors":["Red","Blue"]
}

with open("product.json","w") as file:
    json.dump(product,file)
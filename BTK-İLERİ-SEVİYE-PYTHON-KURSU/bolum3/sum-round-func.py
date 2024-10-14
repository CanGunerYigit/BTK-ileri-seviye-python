sayilar=[1,3,5,4,32,56]
sonuc=sum(sayilar)
print(sonuc)
products=[
    {"title":"iphone15","price":20000},
    {"title":"iphone16","price":30000},
    {"title":"iphone17","price":40000}
]
sonuc=sum([urun["price"] for urun in products])
print(sonuc)



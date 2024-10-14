
#class sınıf demek
class Cart:
    #bu bir constructor yani yapıcı method

    discount_rate=0.8
    def __init__(self,name,price,quantity) :
        #instance attributes yani nesne özellikleri
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity #ürünün fiyatını toplar
    
    def discount(self):
        self.price= self.price * Cart.discount_rate
#bunlarda instance yani nesnelerdir
item1=Cart("Telefon",50000,2)
item2=Cart("Bilgisayar",70000,1)

item1.discount()
print(item1.calculate_total())
        
  
 
class Product:
    def __init__(self,name,price):
        self.name = name
        if price >= 0:
         self._price = price
        else:
           raise ValueError("Negatif fiyat olamaz")
    def set_price(self,value):
       if value >= 0:
          self._price = value
       else:
          raise ValueError("Negatif fiyat olamaz")
    def get_price(self):
       return self._price
    
    #yada 

    @property
    def price(self):  #price get
       return self._price
    
    @price.setter
    def price(self,value): #price set
       if value >= 0:
          self._price = value
       else:
          raise ValueError("Negatif fiyat olamaz")
          
p =Product("Iphone16",80000)
print(p.name,p.price)
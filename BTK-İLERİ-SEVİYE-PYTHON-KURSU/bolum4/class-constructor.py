class CartItem:
    pass

item1=CartItem()
item1.name="Telefon"
item1.price=50000
item1.quantity=2

item2=CartItem()
item2.name="Bilgisayar"
item2.price=70000
item2.quantity=1

print(item1.name)

# bu şekilde kendimiz her eşyaya istediğimiz özellikleri tanımlayabiliyoruz
#birde constructor oluşturalım

class Cart:
    def __init__(self,name,price,quantity) :
        self.name = name
        self.price = price
        self.quantity = quantity

item1=Cart("Telefon",50000,2)
item2=Cart("Bilgisayar",70000,1)
        
  
 
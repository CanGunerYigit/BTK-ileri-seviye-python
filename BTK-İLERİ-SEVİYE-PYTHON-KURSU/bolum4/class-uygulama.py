class Coupon:
    def __init__(self,code,discount):
        self.code = code
        self.discount = discount
c1=Coupon("code1",0.8)
c2=Coupon("code2",0.7)
c3=Coupon("code3",0.9)

class ShoppingCart:
    coupon_list=[c1,c2,c3]
    def __init__(self,liste):
        self.liste = liste
    def additem(self,item):
        self.liste.append(item)
    def displayitems(self):
        for i in self.liste:
            print(f"{i.name} {i.price}")
    def calculatetotal(self):
        return sum([item.price * item.quantity for item in self.liste])
    
    def removeitem(self,cart_item):
        self.liste=[item for item in self.liste if item!= cart_item]   

    def clear(self):
        self.liste=[]
    @classmethod
    def get_coupons(cls):
        return [coupon for coupon in cls.coupon_list]
    
    @classmethod
    def get_coupon(cls,code):
        return next(filter(lambda c: c.code==code,ShoppingCart.coupon_list))
    
    def apply_coupon(self,code):
        if code not in ShoppingCart.get_coupons():
            raise ValueError(f"Geçersiz kupon: {code}")
        coupon=ShoppingCart.get_coupon(code)
        for index in range(0, len[self.liste]):
          self.liste[index].price=self.liste[index].price* coupon.discount


sc=ShoppingCart([item1,item2])
sc.additem(item3)
sc.displayitems()
sc.removeitem(item1)

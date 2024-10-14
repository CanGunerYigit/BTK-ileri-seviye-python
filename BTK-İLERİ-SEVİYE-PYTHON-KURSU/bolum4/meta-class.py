class Meta(type):
    def __new__(self,class_name,bases,attributes):
        print(attributes)

        a={}

        for name,val in attributes.items():
            if name.startswith("_"):
                a[name]=val
            else:
                a[name.upper()]=val
        return type(class_name,bases,attributes,a)
    
class Person(metaclass=Meta):
    x=5
    y=10
    _age=40

    def hello(self):
        print("merhaba")

p=Person()
sonuc=p.x
sonuc=p._age
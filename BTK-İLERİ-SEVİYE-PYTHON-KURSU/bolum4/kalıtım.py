class Person:
      def __init__(self,name,surname,age):
            self.name = name
            self.surname = surname
            self.age = age
            print("Person sınıfı türetildi")

      def intro(self):
           print(self.name,self.surname,self.age)

class Student(Person):
    pass
class Teacher(Person):
    pass

p1 =Person("Can","Yiğit",21)
p1.intro()

s1=Student("Arda","Yılmaz",16)
s1.intro()

t1=Teacher("Emre","Burak",32)
t1.intro()
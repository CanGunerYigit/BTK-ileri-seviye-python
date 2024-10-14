class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
   

    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.stop:
            x=self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
for i in MyNumbers(20,30):
    print(i)
#yada yukarıda tanımladığımız class sayesinde custom iteratorlerimizi kullanabiliriz

iterator=iter(MyNumbers(20,30))
print(next(iterator))

#veya

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

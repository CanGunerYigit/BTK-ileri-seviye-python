#1 ve sonsuz aralığındaki sayıların karesini getiren fonksiyon

def sayi_uret():
    sayi=0
    while True:
        yield sayi**2
        sayi+=1
generator=sayi_uret()
print(next(generator))

#Fibonacci serisini hem normal fonksiyon hem de generator fonksiyon ile oluşturun

def fib_list(max):
    sayilar=[]

    a,b= 0,1
    while len(sayilar)<= max:
        sayilar.append(b)
        a,b=b , a+b
    return sayilar
print(fib_list(900))

def fib_gen(max):
    a,b=0,1
    count=0
    while count<=max:
        a,b=b,a+b
        yield b
        count+=1
for i in fib_gen(900):
    print(i)

#Performans testlerini yapın
import sys
liste=[i for i in range(10000)]
print(sys.getsizeof(liste))

generator=(i for i in range(10000))
print(sys.getsizeof(generator))

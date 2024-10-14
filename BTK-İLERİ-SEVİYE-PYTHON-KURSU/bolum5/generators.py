def counter(max):
    sayi=1
    sayilar=[]
    while sayi<=max:
        yield sayi
        sayi+=1
    return sayilar
generator=counter(20) #generator kullanmak bellekte yer kaplamaz bu sebeple daha iyi performans sağlar
print(next(generator))
print(next(generator))
print(next(generator))

for i in generator:  # for döngüsü burada 1,2 ve 3 ü baştan yazmak yerine kaldığı yerden devam eder
    print(i)

    


#lambda fonksiyon kullanmanın daha basit yoludur

def kareAl(a):
    return a ** 2

sonuc = kareAl(5)
#daha kolay yolu

sonuc= (lambda a: a ** 2)(5)

print(sonuc)


def myFunc(n):
    return lambda x:x*n
carpma2=myFunc(2)
carpma3=myFunc(3)

sonuc = carpma2(3)
sonuc=carpma3(4)
print (sonuc)
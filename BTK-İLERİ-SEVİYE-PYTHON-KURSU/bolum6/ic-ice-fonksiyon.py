def selam(isim):
    return f"Merhaba {isim}"

merhaba=selam
print(selam("Can"))
print(merhaba("Can"))


def outer(number):
    def inner(number):
        print(number)
    inner(number)

outer(10)

def factoriel(sayi):
    def inner_fakt(sayi):
        if sayi<=1:
            return 1
        return sayi*inner_fakt(sayi-1)
    return inner_fakt(sayi)

sonuc =factoriel(5)
print(sonuc)
          
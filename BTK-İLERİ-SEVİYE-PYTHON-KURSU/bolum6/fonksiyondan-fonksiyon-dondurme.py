def UsAlma(taban):
    def inner(us):
        return taban ** us
    return inner
fn = UsAlma(2)
sonuc=fn(4)
print(sonuc)

def yetki_sorgulama(sayfa):
    def inner(rol):
        if rol =="Admin":
          return f"{rol} rolü {sayfa} sayfasına ulaşabilir"
        else:
             return f"{rol} rolü {sayfa} sayfasına ulaşamaz"
        
    return inner
yetki =yetki_sorgulama("Ürün güncelleme sayfası")
sonuc=yetki("Admin")
print(sonuc)

def islem(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam += i
        return toplam
    def carpim(*args):
        carpim=1
        for i in args:
            carpim *= i
        return carpim
    if islem_adi=="toplama":
        return toplam
    else:
        return carpim
    
toplama =islem("toplama")
carpim=islem("carpim")

sonuc=toplama(10,20)
sonuc=carpim(10,20)
print(sonuc)

    
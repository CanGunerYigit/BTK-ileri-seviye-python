sayilar=[3,4,6,9]
sonuc=[]

for sayi in sayilar:
    if(sayi%2==0):
        sonuc.append(sayi)
print(sonuc)

# yada

sonuc=[sayi for sayi in sayilar if sayi%2==0]
print(sonuc)

# else girerse 
sonuc=[sayi if sayi%2==0 else"tek sayı " for sayi in sayilar]
print(sonuc)

# ürün fiyatı 0 dan büyükse 1.20 vergi eklenecek uygulama

urun_fiyatlari=[3000,1000,4000,0,5000]
vergi=[]
for fiyat in urun_fiyatlari:
    if(fiyat>0):
        vergi.append(fiyat*1.20)

# veya 
vergi=[fiyat * 1.20 for fiyat in urun_fiyatlari if fiyat>0]
vergi=[fiyat if fiyat>0 else "vergi hesaplanmadı" for fiyat in urun_fiyatlari]
print(vergi)
sayilar=[1,3,5,-4,-3]

#listedeki negatif ve tek sayı olan sayıları filtrelesin
sonuc=list(filter(lambda negatif: negatif<0,sayilar))
print(sonuc)
sonuc=list(filter(lambda teksayi: teksayi%2 !=0,sayilar))
print(sonuc)

# listedeki a harfi ile başlayan isimleri listelesin
isimler =["çınar","ali","ada","yiğit","sena"]
sonuc=list(filter(lambda a:a[0]=="a",isimler))
print(sonuc)

#listede  a harfi ile başlayan isimlerin harflerini büyütüp listelesin
sonuc=list(map(lambda x:x.upper(),filter(lambda x:x[0]=="a",isimler)))
print(sonuc)
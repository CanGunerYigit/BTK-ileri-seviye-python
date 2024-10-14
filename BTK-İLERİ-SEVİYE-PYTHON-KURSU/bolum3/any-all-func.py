
#all operatörü and gibi çalışır hepsi true olmazsa sonuç true olmaz
sonuc=all([True,True,False])
print(sonuc)
sonuc=all([True,True,True])
print(sonuc)
#any operatöründe herhangi birinin true olması sonucun true çıkması için yeterlidir or gibi çalışır
sonuc=any([True,True,False])
print(sonuc)

#listedeki tüm sayılar 0 dan büyükmü
sayilar=[1,3,5,6,0]
sonuc=all([bool(sayi)for sayi in sayilar])
print(sonuc)
#listedeki sayılardan herhangi biri 0 dan büyükmü
sonuc=any([bool(sayi)for sayi in sayilar])
print(sonuc)
#listedeki sayıların hepsi tekmi
sonuc=all([sayi%2==0 for sayi in sayilar])
print(sonuc)
#listede tek sayı varmıdır
sonuc=any([sayi%2==0 for sayi in sayilar])
print(sonuc)

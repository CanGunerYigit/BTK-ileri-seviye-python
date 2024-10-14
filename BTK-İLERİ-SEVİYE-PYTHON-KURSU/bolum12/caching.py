import mysql.connector
from cachetools import cached,TTLCache #cached decorator ve TTLCache cache süresini verecek
db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="canguner50",
    database="shopdb" 
)

#cache metodu kullanmamız bizim için büyük performans sağlayacaktır kod her çalıştırıldığında yeni bir sorgu göndermek yerine aynı sorgunun sonucu bellekte tutulur ve belirtilen süre boyunca kullanabiliriz
@cached(cache=TTLCache(maxsize=32,ttl=60*60)) #cache üzerinde tutulacak max kapasite 32, ve 1 saat bellek üzerinde tutulacak
def getProducts():
    cursor=db.cursor()
    sql="SELECT p.name,c.name from products p inner join categories c on p.categoryid=c.id WHERE c.name='Bilgisayar'" #category name değeri bilgisayar olan ürünlerin adını listele
    cursor.execute(sql)
    return cursor.fetchall()
print(getProducts())
    
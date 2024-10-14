import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="canguner50",
    database="shopdb" 
)

cursor=db.cursor()
#sql="SELECT COUNT(*) FROM products" #kayıtlardaki satırları sayar
sql="SELECT AVG(Price) FROM products"#ortalama fiyat bilgisini getirecek
sql="SELECT SUM(Price) FROM products" #fiyat toplam bilgisini verecek
sql="SELECT MIN(Price) FROM products" #minimum fiyatlı ürün fiyatını verir max kullanırsak tam tersi en yüksek fiyatlıyı verir
sql="SELECT name,price FROM products WHERE Price= (SELECT MAX(Price) FROM products)" #fiyatı en yüksek olan ürünün isim ve fiyatını verecek
sql="SELECT * FROM products"

sql="SELECT name,price FROM products ORDER BY price DESC LIMIT 1" #ürünün fiyatını ve ismini fiyata göre azalan şekilde getirir, LIMIT 1 verince sadece 1 adet getirir

cursor.execute(sql)

result=cursor.fetchone()

print(result)
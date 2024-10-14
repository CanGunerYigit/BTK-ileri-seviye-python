import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="canguner50",
    database="shopdb" 
)

cursor=db.cursor()

sql="SELECT * from products WHERE id=1" # id si 1 olan kaydı filtreleyerek seçtik
sql="SELECT * from products WHERE name='Samsung S25' and price=50000" # name değişkeni samsung yada s25 olan ve fiyatı 50000tl olan kayıtları filtreledik 
sql="SELECT * from products WHERE name LIKE '%SAMSUNG%'" #name değişkeninin içinde samsung kelimesi geçen tüm kayıtları filtreledik
cursor.execute(sql) #sql sorgusunu çalıştırdık
result=cursor.fetchone() #tek bir nesne geleceği için fetchone kullanabiliriz
print(result) 
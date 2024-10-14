import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="canguner50",
    database="shopdb" 
)

cursor=db.cursor()

sql="SELECT * FROM products" #products tablosundaki tüm nesneleri seç
sql="SELECT id,name FROM products" #products tablosundaki id ve name bilgilerini seçer

cursor.execute(sql)
products=cursor.fetchall() #tüm nesneleri getir
#cursor.fetchone() tek bir kayıt getirir 


for p in products:
    print(products) #tüm satırları ve sütunları dahil eder
    print(p[0],p[1]) #ilk 2 sütun yani id ve isim bilgilerini getirir
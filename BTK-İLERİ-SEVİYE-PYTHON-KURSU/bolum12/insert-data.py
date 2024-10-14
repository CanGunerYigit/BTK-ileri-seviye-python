import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="canguner50",
    database="shopdb" 
)

cursor=db.cursor()
sql="INSERT INTO products (name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" #sütunlarımızı oluşturduk
value=("IPhone 16",70000,"3.jpg","iyi bir telefon") #sütunların içine ilk nesnemizi atayacağız
#çoklu nesne eklemek isteseydik
# values=[
#     ("IPhone 16",70000,"3.jpg","iyi bir telefon"),
#     ("IPhone 16",70000,"3.jpg","iyi bir telefon"),
#     ("IPhone 16",70000,"3.jpg","iyi bir telefon")
# ]
# cursor.executemany(sql,values)
cursor.execute(sql,value)

try:
  db.commit() #sorguyu veritabanına gönderecek bu olmadan ekleme işlemi gerçekleşemez
  print(cursor.rowcount,"kayıt edildi") #satır sayacak ve işlem başarılı olduysa bize cevap verecek
  print(f"son eklenen kaydın id: {cursor.lastrowid}") #son id bilgisini getirecek
except mysql.connector.Error as err:
  print("hata",err) #hatalı bir işlem varsa sebebini terminale gönderecek
finally:
  cursor.close() #son olarak açtığımız bağlantıyı kapatırız ve sonlandırırız
  db.close()
  print("bağlantı kapatıldı")
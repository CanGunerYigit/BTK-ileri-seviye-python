import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="canguner50",
    database="shopdb" #üzerinde çalışacağımız database
)
print(db)

cursor=db.cursor() #sorgu yazabilmek için cursor nesnesi oluşturuyoruz
#cursor.execute("CREATE DATABASE exampledb") #exampledb adında yeni bir schema oluşturur


#cursor.execute("SHOW DATABASES") #mysqldeki tüm schemaları getiren sorgu
cursor.execute("CREATE TABLE categories (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255))") #shopdb ye categories adında yeni bir table oluşturduk 
cursor.execute("SHOW TABLES") #bir schemadaki tüm table ları gösterir
for i in cursor:
    print(i)
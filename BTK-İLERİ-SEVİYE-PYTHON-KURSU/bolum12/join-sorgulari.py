import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="canguner50",
    database="shopdb" 
)

cursor=db.cursor()

sql="SELECT products.name,categories.name from products inner join categories on products.categoryid=categories.id" #iki tablo arasında kesişim yapıyoruz
sql="SELECT p.name,c.name from products p inner join categories c on p.categoryid=c.id" #takma isimler vererek kısaltabiliriz
cursor.execute(sql)
result=cursor.fetchall()
print(result)
import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="canguner50",
    database="shopdb" 
)

cursor=db.cursor()

sql="UPDATE products SET name='Samsung S25-updated',price=price*1.2 WHERE id=1" #id si 1 olan nesnenin name alanını Samsung S25-updated olarak değiştirdik ve fiyatı güncelledik

cursor.execute(sql)

try:
    db.commit()
    print(f"{cursor.rowcount} tane kayıt güncellendi")
except mysql.connector.Error as err:
    print(err)
finally:
    db.close()
    cursor.close()

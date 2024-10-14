import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="canguner50",
    database="shopdb" 
)

cursor=db.cursor()

sql="DELETE FROM products WHERE id=1" #products tablosundan idsi 1 olan kaydı siler
cursor.execute(sql)


try:
    db.commit()
    print(f"{cursor.rowcount} tane kayıt silindi")
except mysql.connector.Error as err:
    print(err)
finally:
    db.close()
    cursor.close()
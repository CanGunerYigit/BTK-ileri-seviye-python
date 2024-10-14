import csv
with open("urunler2.csv","w") as file:
    headers=["Id","ProductName","Price","IsActive","Category","Rating"] #ürün başlıkları ekledik
    csv_writer=csv.DictWriter(file,headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Id": 1,
        "ProductName":"Iphone 14",  # ürün ekledik
        "Price":40000,
        "IsActive":True,
        "Category":"Telefon",
        "Rating":4.6
    })

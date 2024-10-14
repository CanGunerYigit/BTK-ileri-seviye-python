# with open("c:/Users/TR/Desktop/asd/bolum8/urunler.csv") as file:
#     print(file.read())

#yada

import csv 
with open("c:/Users/TR/Desktop/asd/bolum8/urunler.csv") as file:
    csv_reader=csv.reader(file)
    print(csv_reader)
    # print(list(csv_reader)) ürünlerin listesini verir
    for i in csv_reader:
        if i[3] =="True":   #eğer 3. satırdaki isactive true ise ürünün id sini ve adını getir
            print(f" id: {i[0]}, ürün adı: {i[1]}")

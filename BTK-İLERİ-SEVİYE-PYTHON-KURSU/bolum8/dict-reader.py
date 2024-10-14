import csv 
with open("c:/Users/TR/Desktop/asd/bolum8/urunler.csv") as file:
    csv_reader = csv.DictReader(file)
    # print(list(csv_reader))
    for i in csv_reader:
        if i["Category"]=="Telefon" and float(i["Rating"]) > 4.5 :  #kategorisi telefon olan ve ratingi 4.5in üstünde olan ürünlerin ismini listele
         print(i["ProductName"])
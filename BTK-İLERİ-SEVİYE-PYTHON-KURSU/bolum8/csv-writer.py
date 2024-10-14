import csv
# with open("arabalar.csv", "w",newline="") as file: #w modu yazmak, r modu okumak, a modu ise varolanın üzerine yazmak için kullanılır
#     csv_writer=csv.writer(file)
#     csv_writer.writerow(["Marka","Model"])
#     csv_writer.writerow(["Toyota","Corolla"])
#     csv_writer.writerow(["Opel","Astra"])
#     #yada içine daha kısa bir yöntemle yazdırabiliriz
#     csv_writer.writerows([["Marka","Model"],["Toyota","Corolla"],["Opel","Astra"]])

with open("urunler.csv") as file:  #bir csv dosyasının içeriğini yeni açtığımız bir csv dosyasına aktarabiliriz
    csv_reader=csv.reader(file)
    with open("yeni-urunler.csv", "w",newline="") as f:
        csv_writer=csv.writer(f)
        for urun in csv_reader:
            csv_writer.writerow(urun)
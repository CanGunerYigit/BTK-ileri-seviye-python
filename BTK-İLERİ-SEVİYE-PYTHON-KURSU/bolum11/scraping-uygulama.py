import requests
from bs4 import BeautifulSoup
from csv import writer
url="https://www.btkakademi.gov.tr/portal/catalog?categoryId=353"
response =requests.get(url)
html=BeautifulSoup(response.text,"html.parser") #site içeriğini getirecek

kurslar =html.find(id="gbt_catalog-main-right-course").find_all(class_="ant-ribbon-wrapper") #bütün kursları getirecek
with open("kurslar.csv","w",encoding="utf-8") as file:
    csv_writer=writer(file)
    csv_writer.writerow(["like","image","title","seviye","like","ogrenci"]) #istediğimiz bilgileri kurslar.csv dosyası açıp içine yazdıracak

    for kurs in kurslar: #bütün kursların linklerini getirecek
     anchor = kurs.a
     link=anchor.img.get("href")
     image=anchor.img.get("src")
     title=anchor.find(class_="font-medium text-base").string
     seviye=anchor.find(class_="txt-secondary font-medium").string

     sayilar=anchor.next_sibling.next_sibling.get_text(separator="-").split("-") #rateleri ekrana getirecek ve aralarında - ayracını kullanacak 

     like=sayilar[0]
     ogrenci=sayilar[1]

     csv_writer.writerow([link,image,title,seviye,like,ogrenci])
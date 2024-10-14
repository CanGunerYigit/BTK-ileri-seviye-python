from bs4 import BeautifulSoup

with open("bolum11\index.html") as file:
    html=file.read()
obj = BeautifulSoup(html,"html.parser")

sonuc = obj

sonuc=obj.h1.string

print(sonuc)
with open("product.json") as file:
    data=file.read()
print(data)
#bizim bu veriyi kullanabilmek için deserialize etmemiz yani decode etmemiz lazım
# bu yüzden veri tipimizi dictionarye çevirebiliriz 

import json
with open("product.json") as file:
    data=json.load(file) # dictionary veri tipine dönüştürür
print(data["title"])
print(data["price"])

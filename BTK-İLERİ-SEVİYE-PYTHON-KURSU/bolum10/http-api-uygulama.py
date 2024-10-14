import requests

url="http://api.weatherapi.com/v1/current.json"
key="9a8335f2c3ef4e27825110654240710"

konum=input("konum:")
response = requests.get(url,params={
    "key":key,
    "q":konum,
    "lang":"tr" #vereceği bilgileri türkçeye çevirsin
})

sonuc=response.json()
sehir=sonuc["location"]["name"]
havadurumu=sonuc["current"]["temp_c"]
text=sonuc["current"]["condition"]["text"]
print(f"{sehir} şu anda {havadurumu} derece ve {text} "   )
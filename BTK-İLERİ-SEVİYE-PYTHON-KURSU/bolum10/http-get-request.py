#status codeları 200= başarılı , 300= kaynak taşındı yada yönlendirildi, 400= sayfaya ulaşılamadı yada getirilemedi, 500= sunucu kaynaklı hata

import requests
import json
response=requests.get("https://jsonplaceholder.typicode.com/posts") #json placeholder sitesinde hazır olarak bulunan postları get metoduyla çağırıp değişkene atadık

print(response) #terminalde 200 statüs kodunu verir yani başarılı sonuçlandığı anlamına gelir

sonuc = response.text  # post bilgilerini string tipinde ekrana getirecek jsona çevirirsek üzerinde güncellemeler yapabiliriz
print(sonuc)
posts=json.loads(response.text) #jsona çevirdik

for i in posts:
    if i["userId"] ==1:  #userId si 1 olan postların başlığını ekrana yazdır
     print(i["title"])
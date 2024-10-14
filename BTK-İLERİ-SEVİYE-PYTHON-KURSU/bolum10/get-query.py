import requests

response=requests.get("https://jsonplaceholder.typicode.com/todos?userId=1&completed=true") #userId si 1 olan ve tamamlanmış todoların urli

todos=response.json() #stringden json formatına çevirdik

sonuc=todos

print(sonuc[0]["title"]) #yukarıdaki urlde dahil olarak yani userIdsi 1 ve completed=true olan listenin ilk elemanının başlığını yazdırır

#eğer biz userId ve completed=true yu dışardan bir parametre olarak gönderiyorsak yani dinamik bir kod ise urli şu şekilde kullanıyoruz:
response=requests.get("https://jsonplaceholder.typicode.com/todos",params={
    "userId":"1",
    "completed":"true"
})
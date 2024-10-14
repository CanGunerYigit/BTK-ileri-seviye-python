import requests
response= requests.post("https://jsonplaceholder.typicode.com/posts",data={

    "userId": 1,
    "title": "yeni post",
    "body": "yeni post açıklama"  #yeni göndereceğimiz post bilgileri
})

print(response) #sonucu 201 status code olarak gönderir yani başarılı bir işlemdir

print(response.text) #gönderdiğimiz postu görebiliriz
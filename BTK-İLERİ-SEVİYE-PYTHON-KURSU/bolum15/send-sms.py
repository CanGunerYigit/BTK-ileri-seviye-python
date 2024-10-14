import vonage

client=vonage.Client(key="034f4d9b",secret="b1ye0Csmx8WzRSA4")
sms=vonage.Sms(client)

responseData=sms.send_message({
    "from":"Deneme",
    "to":"telefon numarası",
    "text":"deneme"
})
if responseData["messages"][0]["status"]=="0": #gelen status code 0 ise mesaj gitti
    print("mesaj gönderildi")
else:
    print(f"hata oluştu:",{responseData['messages'][0]['error-text']}) #hata oluşması durumunda hatayı versin

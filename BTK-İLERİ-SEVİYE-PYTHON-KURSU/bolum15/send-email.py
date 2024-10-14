import smtplib
from email.mime.text import MIMEText
port= 587
smtp_server="smtp-relay.brevo.com"
login="7dd9f7001@smtp-brevo.com"
password="FvJkX1yTE04HGZNc"

sender="can-1045@hotmail.com"
reciever="ffdarkguardian@hotmail.com"

text="""
  Bu bir denemedir
 
"""
message=MIMEText(text,"plain") #plain daha düzenli html formatında gönderebilmek için 
message["Subject"]="Merhaba" #Konumuz
message["From"]= sender  #gönderen kim
message["To"]= reciever #alan kişi fazladan kişiye göndermek istersek burada aynı tırnak içerisinde virgülle ayırarak yazabiliriz

with smtplib.SMTP(smtp_server,port) as server:
    server.starttls() #güvenli bir bağlantıyla göndereceğiz
    server.login(login,password)
    server.sendmail(sender,reciever,message.as_string())
    print("Eposta gönderildi")

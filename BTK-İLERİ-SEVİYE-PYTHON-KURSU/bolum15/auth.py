import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyCwz9eREItB_6vTpdGzh7tG9N-Lce02K-U",
  "authDomain": "authpython-bec13.firebaseapp.com",
  "projectId": "authpython-bec13",
  "storageBucket": "authpython-bec13.appspot.com",
  "messagingSenderId": "473198907245",
  "appId": "1:473198907245:web:1df5008e1458a60125d464",
  "databaseURL":"https://authpython-bec13-default-rtdb.firebaseio.com/"
}

firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

def signUp():
    email=input("email:")
    password=input("password:")
    auth.create_user_with_email_and_password(email, password)
    print("kullanıcı oluşturuldu")

# signUp()

def login():
    email=input("email:")
    password=input("password:")
    
    try:
        user=auth.sign_in_with_email_and_password(email,password)
        print(user)
        print(auth.get_account_info(user["idToken"])) #token bilgisiyle uygulamayı kullanıp kullanamayacağımız tespit edilir
        print("giriş yapıldı")
    except:
        print("hatalı mail yada parola")
login()
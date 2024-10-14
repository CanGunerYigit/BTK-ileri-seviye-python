import re 
text="BTK Akademi ile Python kurs tarihleri 15-May-2025 15.May.2025 15.05.2025. Telefon numaralarımız +90-530-999-9999 +90 530 999 9999. Mail adreslerimiz abc@gmail.com abc@gmail.co.tr"

pattern = r"\d\d-[a-zA-Z][a-zA-Z][a-zA-Z]-\d\d\d\d" #2 basamaklı sayı, 3 basamaklı tarih adı ve 4 basamaklı yıl
#kısaltılmış hali
pattern=r"\d{2}-[a-zA-Z]{3}-\d{4}"
#aradaki -  / ve . karşılayacak şekilde yazalım
pattern=r"\d{2}[-./]([a-zA-Z]{3}|\d{2})[-./]\d{4}"


pattern =r"\w+@[a-z]+(\.[a-z]{2,3})+" # başlangıcı istediği karakter olsun ve daha fazla da olabilir manasında + koyduk @ işareti olacak ve gmail için küçük harf a dan z ye karakterler + ile en az bir kere \. ile . karakterini arayacak com için a dan z ye arayacak 2 veya 3 defa

pattern =r"\+\d{2}[-\s]\d{3}[-\s]\d{3}[-\s]\d{4}" # + işaretini arayacak, 2 tane rakam sonra - ve 3 rakam daha sonra bir kez daha, ardından tekrar fakat 4 rakam içerecek s space yani boşluk anlamına gelir 

matches=re.finditer(pattern, text)

for match in matches:
    print(match)
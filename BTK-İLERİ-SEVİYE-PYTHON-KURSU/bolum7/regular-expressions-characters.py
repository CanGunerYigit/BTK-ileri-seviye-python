import re

text="ABC 123 XYZ 456 @&% 300"
pattern=r"\d\d\d" #sayısal karakterleri bulmak için kullanılır
pattern=r"\d+" # text içerisindeki bütün sayıları bulur
pattern=r"\d*" #boşluk karakterlerinide bulur
pattern r"\d{3}"#text içerisindeki 3 basamaklıları getirir
pattern r"\d{3,5}" #text içerisindeki 3 ve 5 basamak arasındaki sayıları getirir
pattern r"\d{3,}"#minimum 3 ve 3 den daha fazla basamaklı olan sayıları getirir
pattern r"\d{,5}" #maximum 5 basamağa kadar olan sayıları getirir
matches=re.search(pattern,text)

print(matches)

#hepsini iterator ile görmek istiyorsak 
matches=re.finditer(pattern,text)
for match in matches:
    print(match.group())


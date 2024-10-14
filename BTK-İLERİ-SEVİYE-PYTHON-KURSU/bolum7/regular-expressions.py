import re

text="BTK Akademi Python Dersleri"
pattern="BTK"
sonuc=re.search(pattern, text)
print(sonuc)
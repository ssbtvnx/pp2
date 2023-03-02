import re
text=input()
y=re.findall("[A-Z][a-z]+",text)
print(y)
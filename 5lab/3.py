import re
text=input()
y=re.findall("[a-z]*_",text)
print(y)
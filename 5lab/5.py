import re
text=input()
y=re.findall("a.*b$", text)
print(y)
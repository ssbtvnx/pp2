import re
text=input()
y=re.sub("[ ,.]", ":",text)
print(y)